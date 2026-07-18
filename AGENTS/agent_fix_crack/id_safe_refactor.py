# -*- coding: utf-8 -*-
"""
全自动扫描清除 Base64 硬编码 ID

功能：
  递归扫描 .py/.json 文件，检测 auth/token/task_id/user_id 等字段，
  替换为 PLACEHOLDER。跳过无害文件和 C:\RPADATA 路径。
  输出清洗报告。

用法：
  python id_safe_refactor.py --target-dir "f:\RPA(1)\发票开具机器人"  # 指定目标目录
  python id_safe_refactor.py --target-dir "f:\RPA(1)\发票开具机器人" --dry-run  # 试运行
  python id_safe_refactor.py --report-only  # 仅检测不修改

安全规则：
  - 跳过 C:\RPADATA 路径（系统路径不修改）
  - 跳过 dependencies/ 目录（组件不修改）
  - Base64 解码后只清除 ID 相关字段，不破坏其他数据结构
  - 修改前自动备份原文件（.bak）
"""

import os
import sys
import re
import json
import base64
import shutil
import argparse
from datetime import datetime


# =============================================================================
# 配置区
# =============================================================================
ROOT_PATH = "f:\\RPA(1)"
SYSTEM_PATH = os.path.join(ROOT_PATH, "rpa-student-multi-agent-system")

# 需要扫描的文件扩展名
SCAN_EXTENSIONS = [".py", ".json"]

# 需要跳过的目录
SKIP_DIRS = ["dependencies", "node_modules", "__pycache__", ".git"]

# 跳过包含这些路径的文件
SKIP_PATH_PATTERNS = [
    r"c:\\RPADATA",
    r"C:\\RPADATA",
    r"c:\RPADATA",
    r"C:\RPADATA",
]

# 敏感字段名（用于识别ID相关字段）
SENSITIVE_FIELDS = [
    "user_id", "task_id", "UserID", "TaskID", "userId", "taskId",
    "USER_ID", "TASK_ID", "userid", "taskid",
    "auth", "token", "authorization",
    "username", "password", "secret",
]

# PLACEHOLDER
PLACEHOLDER = "__ID_PLACEHOLDER__"

# 正则模式
UUID_PATTERN = re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
HEX32_PATTERN = re.compile(r'[0-9a-fA-F]{32}')
BASE64_PATTERN = re.compile(r'[A-Za-z0-9+/]{20,}={0,2}')
ASSIGN_PATTERN = re.compile(
    r'(user_id|task_id|UserID|TaskID|userId|taskId|USER_ID|TASK_ID)\s*[=:]\s*["\']([^"\']+)["\']',
    re.IGNORECASE
)


# =============================================================================
# 核心功能
# =============================================================================
def should_skip_file(filepath):
    """判断文件是否应该跳过"""
    # 检查路径中的目录名
    parts = filepath.split(os.sep)
    for skip_dir in SKIP_DIRS:
        if skip_dir in parts:
            return True

    # 检查文件内容中是否包含系统路径
    return False


def is_id_field(key):
    """判断字段名是否为ID相关"""
    key_lower = key.lower().replace("-", "_").replace(" ", "_")
    for field in SENSITIVE_FIELDS:
        if field.lower() in key_lower:
            return True
    return False


def scan_py_file(filepath, dry_run=False):
    """扫描并清理 .py 文件中的硬编码ID"""
    findings = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="gbk") as f:
                content = f.read()
        except Exception:
            return [], content

    # 检查是否包含系统路径
    for pattern in SKIP_PATH_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return [], content

    # 查找赋值语句中的ID
    modified_content = content
    for match in ASSIGN_PATTERN.finditer(content):
        field_name = match.group(1)
        field_value = match.group(2)

        # 检查值是否是UUID或32位hex
        if UUID_PATTERN.match(field_value) or HEX32_PATTERN.match(field_value):
            findings.append({
                "type": "plain_id",
                "field": field_name,
                "value_preview": field_value[:12] + "***",
                "position": match.start(),
            })

            if not dry_run:
                old = match.group(0)
                new = f'{field_name} = "{PLACEHOLDER}"'
                modified_content = modified_content.replace(old, new, 1)

    # 查找Base64编码的ID
    for match in BASE64_PATTERN.finditer(content):
        encoded = match.group()
        try:
            decoded = base64.b64decode(encoded).decode("utf-8", errors="ignore")
            if UUID_PATTERN.search(decoded) or HEX32_PATTERN.search(decoded):
                findings.append({
                    "type": "base64_encoded_id",
                    "field": "unknown",
                    "value_preview": encoded[:20] + "...",
                    "position": match.start(),
                })
        except Exception:
            continue

    return findings, modified_content


def scan_json_file(filepath, dry_run=False):
    """扫描并清理 .json 文件中的硬编码ID"""
    findings = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="gbk") as f:
                content = f.read()
        except Exception:
            return [], content

    # 检查是否包含系统路径
    for pattern in SKIP_PATH_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return [], content

    # 尝试解析JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return [], content

    modified_data = json.loads(content)
    modified = False

    def scan_json_obj(obj, path=""):
        """递归扫描JSON对象"""
        nonlocal modified
        local_findings = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{path}.{key}" if path else key

                if is_id_field(key) and isinstance(value, str):
                    # 检查值是否是UUID或32位hex或Base64
                    if UUID_PATTERN.match(value) or HEX32_PATTERN.match(value):
                        local_findings.append({
                            "type": "json_id",
                            "field": current_path,
                            "value_preview": value[:12] + "***",
                        })
                        if not dry_run:
                            _set_nested_value(modified_data, current_path, PLACEHOLDER)
                            modified = True
                    elif len(value) > 20 and BASE64_PATTERN.match(value):
                        try:
                            decoded = base64.b64decode(value).decode("utf-8", errors="ignore")
                            if UUID_PATTERN.search(decoded) or HEX32_PATTERN.search(decoded):
                                local_findings.append({
                                    "type": "json_base64_id",
                                    "field": current_path,
                                    "value_preview": value[:20] + "...",
                                })
                                if not dry_run:
                                    _set_nested_value(modified_data, current_path, PLACEHOLDER)
                                    modified = True
                        except Exception:
                            pass

                if isinstance(value, (dict, list)):
                    local_findings.extend(scan_json_obj(value, current_path))

        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path = f"{path}[{i}]"
                if isinstance(item, (dict, list)):
                    local_findings.extend(scan_json_obj(item, current_path))

        return local_findings

    findings = scan_json_obj(data)

    modified_content = json.dumps(modified_data, ensure_ascii=False, indent=2) if modified else content

    return findings, modified_content


def _set_nested_value(obj, path, value):
    """设置嵌套JSON对象中的值"""
    parts = path.split(".")
    current = obj
    for i, part in enumerate(parts):
        if "[" in part:
            # list index
            name, idx = part.split("[")
            idx = int(idx.rstrip("]"))
            if i == len(parts) - 1:
                current[name][idx] = value
            else:
                current = current[name][idx]
        else:
            if i == len(parts) - 1:
                current[part] = value
            else:
                current = current[part]


def scan_directory(target_dir, dry_run=False):
    """扫描目录中的所有文件"""
    if not os.path.exists(target_dir):
        print(f"[ERROR] 目标目录不存在: {target_dir}")
        return [], []

    all_findings = []
    modified_files = []

    for root, dirs, files in os.walk(target_dir):
        # 跳过不需要的目录
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for filename in files:
            filepath = os.path.join(root, filename)
            ext = os.path.splitext(filename)[1].lower()

            if ext not in SCAN_EXTENSIONS:
                continue

            if should_skip_file(filepath):
                continue

            rel_path = os.path.relpath(filepath, target_dir)

            # 扫描文件
            if ext == ".py":
                findings, modified_content = scan_py_file(filepath, dry_run)
            elif ext == ".json":
                findings, modified_content = scan_json_file(filepath, dry_run)
            else:
                continue

            if findings:
                print(f"  [发现] {rel_path}: {len(findings)} 个ID字段")
                all_findings.extend([(rel_path, f) for f in findings])

                if not dry_run and modified_content:
                    # 备份原文件
                    bak_path = filepath + ".bak"
                    if not os.path.exists(bak_path):
                        shutil.copy2(filepath, bak_path)
                        print(f"    -> 已备份: {os.path.basename(filepath)}.bak")

                    # 写回修改后的内容
                    try:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(modified_content)
                        modified_files.append(filepath)
                        print(f"    -> 已清理")
                    except Exception as e:
                        print(f"    -> 写入失败: {e}")

    return all_findings, modified_files


# =============================================================================
# 报告生成
# =============================================================================
def generate_report(target_dir, findings, modified_files, dry_run):
    """生成清洗报告"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_path = os.path.join(SYSTEM_PATH, "id_clean_report.txt")

    # 按文件分组
    file_findings = {}
    for rel_path, finding in findings:
        if rel_path not in file_findings:
            file_findings[rel_path] = []
        file_findings[rel_path].append(finding)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("RPA ID 清洗报告\n")
        f.write(f"时间: {timestamp}\n")
        f.write(f"目标目录: {target_dir}\n")
        f.write(f"试运行: {'是' if dry_run else '否'}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"扫描文件数: {len(file_findings)} 个文件发现ID\n")
        f.write(f"发现ID字段: {len(findings)} 处\n")
        f.write(f"已清洗文件: {len(modified_files)} 个\n\n")

        if file_findings:
            f.write("详细发现:\n")
            for rel_path, file_finds in file_findings.items():
                f.write(f"\n  {rel_path}:\n")
                for ff in file_finds:
                    f.write(f"    - [{ff['type']}] 字段: {ff['field']}, 值: {ff['value_preview']}\n")

        f.write("\n" + "=" * 60 + "\n")

    print(f"\n[报告已保存] {report_path}")
    return report_path


# =============================================================================
# 主函数
# =============================================================================
def main():
    """主入口"""
    parser = argparse.ArgumentParser(description="RPA ID 安全清洗工具 - 全自动扫描清除Base64硬编码ID")
    parser.add_argument("--target-dir", type=str, default=None, help="目标工程目录")
    parser.add_argument("--dry-run", action="store_true", help="试运行模式（仅扫描不修改）")
    parser.add_argument("--report-only", action="store_true", help="仅检测不修改（等价于 --dry-run）")
    parser.add_argument("--auto", action="store_true", help="自动扫描ROOT_PATH下所有机器人")
    args = parser.parse_args()

    print("=" * 60)
    print("RPA ID 安全清洗工具")
    print("=" * 60)

    dry_run = args.dry_run or args.report_only

    # 确定目标目录
    if args.auto:
        # 扫描所有机器人目录
        all_findings = []
        all_modified = []

        robot_dirs = [
            "电子税务局平台登录机器人",
            "发票开具机器人",
            "发票查验机器人",
            "发票认证机器人",
            "发票单笔查验机器人（开发模板）",
            "网银付款机器人",
            "网银对公付款机器人（开发模板）_(2)",
            "网银收款查询机器人",
        ]

        for robot_dir in robot_dirs:
            target_path = os.path.join(ROOT_PATH, robot_dir)
            if os.path.exists(target_path):
                print(f"\n--- 扫描: {robot_dir} ---")
                findings, modified = scan_directory(target_path, dry_run)
                all_findings.extend(findings)
                all_modified.extend(modified)
            else:
                print(f"\n[跳过] {robot_dir} 不存在")

        # 生成综合报告
        print(f"\n{'=' * 60}")
        print(f"扫描完成!")
        print(f"  扫描机器人: {len(robot_dirs)} 个")
        print(f"  发现ID字段: {len(all_findings)} 处")
        print(f"  清洗文件: {len(all_modified)} 个")
        print(f"{'=' * 60}")

        if all_findings:
            generate_report(ROOT_PATH, all_findings, all_modified, dry_run)

        return

    target_dir = args.target_dir
    if not target_dir:
        print("[ERROR] 请指定目标目录 (--target-dir) 或使用 --auto 自动扫描")
        sys.exit(1)

    if not os.path.exists(target_dir):
        print(f"[ERROR] 目标目录不存在: {target_dir}")
        sys.exit(1)

    # 执行扫描
    findings, modified_files = scan_directory(target_dir, dry_run)

    # 输出结果
    print(f"\n{'=' * 60}")
    if dry_run:
        print(f"试运行完成!")
    else:
        print(f"清洗完成!")
    print(f"  扫描目录: {target_dir}")
    print(f"  发现ID字段: {len(findings)} 处")
    print(f"  清洗文件: {len(modified_files)} 个")
    print(f"{'=' * 60}")

    # 生成报告
    if findings:
        generate_report(target_dir, findings, modified_files, dry_run)


if __name__ == "__main__":
    main()
