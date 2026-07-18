# -*- coding: utf-8 -*-
"""
ID 风控校验脚本

功能：
  1. check_id_legality - ID格式检查
  2. check_id_duplicate - 串号检测
  3. check_code_tamper - 篡改检测（TODO标记/eval/subprocess等）
  4. generate_risk_report - 生成完整风控报告

用法：
  python risk_check.py --check-id <user_id> <task_id>         # 检查ID合法性
  python risk_check.py --check-duplicate <task_id>             # 检查串号
  python risk_check.py --check-tamper --target-dir <dir>       # 检查篡改
  python risk_check.py --full-report --target-dir <dir>        # 完整风控报告
"""

import os
import sys
import re
import json
import hashlib
import argparse
from datetime import datetime


# =============================================================================
# 配置区
# =============================================================================
ROOT_PATH = "f:\\RPA(1)"
SYSTEM_PATH = os.path.join(ROOT_PATH, "rpa-student-multi-agent-system")

# 已知的ID记录文件
ID_RECORD_FILE = os.path.join(SYSTEM_PATH, "USER_WORKSPACE", "user_id_config.yaml")

# 需要扫描的扩展名
SCAN_EXTENSIONS = [".py", ".json", ".flow.json", ".variable.json", ".ctrl.json"]

# 篡改检测模式
TAMPER_PATTERNS = {
    "TODO标记": r"#\s*TODO|#\s*FIXME|#\s*HACK|#\s*XXX",
    "eval执行": r"\beval\s*\(|\bexec\s*\(|\bcompile\s*\(",
    "subprocess调用": r"\bsubprocess\.\w+\s*\(|\bos\.system\s*\(",
    "动态导入": r"\b__import__\s*\(|\bimportlib\.import_module\s*\(",
    "反射调用": r"\bgetattr\s*\(.*,\s*[\"']\w+[\"']\s*\)",
    "base64解码": r"base64\.b64decode\s*\(",
    "文件写入": r"open\s*\([^)]+['\"]w['\"]",
    "os操作": r"os\.remove\s*\(|os\.unlink\s*\(|shutil\.rmtree\s*\(",
    "网络请求": r"requests?\.(get|post|put|delete)\s*\(",
    "动态属性": r"setattr\s*\(|delattr\s*\(",
}

# ID格式模式
UUID_PATTERN = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
HEX32_PATTERN = re.compile(r'^[0-9a-fA-F]{32}$')


# =============================================================================
# 1. ID格式检查
# =============================================================================
def check_id_legality(user_id=None, task_id=None):
    """
    检查ID格式合法性

    规则：
      - UserID: UUID格式 8-4-4-4-12，共36字符
      - TaskID: 32位十六进制字符串

    返回: (is_valid, results)
      results: 每个ID的检查结果列表
    """
    print("\n" + "=" * 60)
    print("ID 格式合法性检查")
    print("=" * 60)

    results = []

    if user_id:
        is_valid = UUID_PATTERN.match(user_id) is not None
        user_result = {
            "field": "UserID",
            "value": user_id[:8] + "***" + user_id[-4:] if len(user_id) > 12 else user_id,
            "valid": is_valid,
            "errors": [],
        }

        if not user_id:
            user_result["errors"].append("不能为空")
        elif len(user_id) != 36:
            user_result["errors"].append(f"长度应为36位，当前{len(user_id)}位")
        elif not is_valid:
            user_result["errors"].append("格式不正确，应为8-4-4-4-12的UUID格式")

        results.append(user_result)
        status = "通过" if is_valid else "不通过"
        print(f"  UserID: {user_result['value']} -> [{status}]")
        if user_result["errors"]:
            for err in user_result["errors"]:
                print(f"    错误: {err}")

    if task_id:
        is_valid = HEX32_PATTERN.match(task_id) is not None
        task_result = {
            "field": "TaskID",
            "value": task_id[:8] + "***" if len(task_id) > 8 else task_id,
            "valid": is_valid,
            "errors": [],
        }

        if not task_id:
            task_result["errors"].append("不能为空")
        elif len(task_id) != 32:
            task_result["errors"].append(f"长度应为32位，当前{len(task_id)}位")
        elif not is_valid:
            task_result["errors"].append("包含非十六进制字符")

        results.append(task_result)
        status = "通过" if is_valid else "不通过"
        print(f"  TaskID: {task_result['value']} -> [{status}]")
        if task_result["errors"]:
            for err in task_result["errors"]:
                print(f"    错误: {err}")

    all_valid = all(r["valid"] for r in results)
    return all_valid, results


# =============================================================================
# 2. 串号检测
# =============================================================================
def check_id_duplicate(task_id, scan_dir=None):
    """
    检测TaskID是否与系统中已有工程重复

    返回: (has_duplicate, details)
      has_duplicate: True表示发现重复
      details: 重复详情或None
    """
    print("\n" + "=" * 60)
    print("ID 串号检测")
    print("=" * 60)

    if not scan_dir:
        scan_dir = ROOT_PATH

    if not os.path.exists(scan_dir):
        print(f"  [INFO] 扫描目录不存在: {scan_dir}")
        return False, None

    # 计算当前ID的哈希
    id_hash = hashlib.md5(task_id.encode()).hexdigest()

    matches = []
    for root, dirs, files in os.walk(scan_dir):
        if "dependencies" in root.split(os.sep):
            continue
        if "rpa-student-multi-agent-system" in root.split(os.sep):
            continue

        for filename in files:
            if not filename.endswith(".py") and not filename.endswith(".json"):
                continue

            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, Exception):
                try:
                    with open(filepath, "r", encoding="gbk") as f:
                        content = f.read()
                except Exception:
                    continue

            # 在文件中搜索TaskID
            if task_id in content:
                rel_path = os.path.relpath(filepath, scan_dir)
                matches.append(rel_path)
                print(f"  [发现重复] {rel_path}")

            # 也搜索Base64编码的ID
            for match in re.finditer(r'[A-Za-z0-9+/]{20,}={0,2}', content):
                try:
                    import base64
                    decoded = base64.b64decode(match.group()).decode("utf-8", errors="ignore")
                    if task_id in decoded:
                        rel_path = os.path.relpath(filepath, scan_dir)
                        if rel_path not in matches:
                            matches.append(rel_path)
                            print(f"  [发现重复(Base64)] {rel_path}")
                except Exception:
                    continue

    if matches:
        print(f"\n  发现 {len(matches)} 个文件包含该TaskID")
        return True, {"task_id": task_id, "matched_files": matches}

    print("  未发现重复ID")
    return False, None


# =============================================================================
# 3. 篡改检测
# =============================================================================
def check_code_tamper(target_dir):
    """
    检测代码中的篡改痕迹

    检测项：
      - TODO/FIXME/HACK 未处理标记
      - eval/exec/subprocess 等危险函数调用
      - 非标准修改痕迹
      - Base64解码操作
      - 文件写入操作

    返回: (has_risks, risk_details)
    """
    print("\n" + "=" * 60)
    print("代码篡改检测")
    print("=" * 60)

    if not os.path.exists(target_dir):
        print(f"  [ERROR] 目标目录不存在: {target_dir}")
        return False, []

    all_risks = []

    for root, dirs, files in os.walk(target_dir):
        if "dependencies" in root.split(os.sep):
            continue

        for filename in files:
            if not any(filename.endswith(ext) for ext in SCAN_EXTENSIONS):
                continue

            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, target_dir)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, Exception):
                try:
                    with open(filepath, "r", encoding="gbk") as f:
                        content = f.read()
                except Exception:
                    continue

            file_risks = []

            # 逐行检查
            lines = content.split("\n")
            for line_num, line in enumerate(lines, 1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue

                for risk_name, pattern in TAMPER_PATTERNS.items():
                    if re.search(pattern, stripped):
                        file_risks.append({
                            "line": line_num,
                            "type": risk_name,
                            "content": stripped[:100],
                        })

            if file_risks:
                all_risks.append({
                    "file": rel_path,
                    "risks": file_risks,
                })

                risk_types = list(set(r["type"] for r in file_risks))
                print(f"  [风险] {rel_path}: {len(file_risks)} 处风险 ({', '.join(risk_types)})")

                for r in file_risks[:3]:  # 显示前3条
                    print(f"    行{r['line']}: [{r['type']}] {r['content'][:80]}")

                if len(file_risks) > 3:
                    print(f"    ... 还有 {len(file_risks) - 3} 处")

    has_risks = len(all_risks) > 0
    if not has_risks:
        print("  未检测到篡改风险")

    return has_risks, all_risks


# =============================================================================
# 4. 生成完整风控报告
# =============================================================================
def generate_risk_report(target_dir, user_id=None, task_id=None):
    """
    生成完整风控报告

    包含：
      1. ID格式检查结果
      2. 串号检测结果
      3. 篡改检测结果
      4. 综合风险评估

    返回: 报告文件路径
    """
    print("\n" + "=" * 60)
    print("生成完整风控报告")
    print("=" * 60)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. ID格式检查
    id_valid, id_results = check_id_legality(user_id, task_id)

    # 2. 串号检测
    has_duplicate, duplicate_details = check_id_duplicate(task_id, target_dir)

    # 3. 篡改检测
    has_tamper, tamper_details = check_code_tamper(target_dir)

    # 4. 综合评估
    risk_level = "低"
    risk_count = 0
    risk_items = []

    if not id_valid:
        risk_count += 1
        risk_items.append("ID格式不合法")

    if has_duplicate:
        risk_count += 1
        risk_items.append("存在串号风险")

    if has_tamper:
        risk_count += 1
        risk_items.append("检测到代码篡改风险")

    if risk_count == 0:
        risk_level = "低"
    elif risk_count == 1:
        risk_level = "中"
    else:
        risk_level = "高"

    # 生成报告
    report_path = os.path.join(SYSTEM_PATH, f"risk_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("RPA 风控校验报告\n")
        f.write(f"时间: {timestamp}\n")
        f.write(f"目标: {target_dir}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"一、ID格式检查\n")
        f.write(f"    结果: {'通过' if id_valid else '不通过'}\n")
        if id_results:
            for r in id_results:
                f.write(f"    {r['field']}: {'合法' if r['valid'] else '不合法'}\n")
                for err in r["errors"]:
                    f.write(f"      - {err}\n")

        f.write(f"\n二、串号检测\n")
        f.write(f"    结果: {'发现重复' if has_duplicate else '无重复'}\n")
        if has_duplicate and duplicate_details:
            f.write(f"    重复文件:\n")
            for fp in duplicate_details["matched_files"]:
                f.write(f"      - {fp}\n")

        f.write(f"\n三、篡改检测\n")
        f.write(f"    结果: {'发现风险' if has_tamper else '无风险'}\n")
        if has_tamper and tamper_details:
            for detail in tamper_details[:5]:
                f.write(f"    {detail['file']}:\n")
                for risk in detail["risks"][:3]:
                    f.write(f"      行{risk['line']}: [{risk['type']}] {risk['content'][:80]}\n")

        f.write(f"\n四、综合评估\n")
        f.write(f"    风险等级: {risk_level}\n")
        f.write(f"    风险项数: {risk_count}\n")
        if risk_items:
            for item in risk_items:
                f.write(f"    - {item}\n")

        f.write(f"\n五、建议\n")
        if risk_level == "低":
            f.write("    一切正常，可以提交作业。\n")
        elif risk_level == "中":
            f.write("    存在轻度风险，建议处理后再提交。\n")
        else:
            f.write("    存在严重风险，请修复后再提交！\n")

        f.write("\n" + "=" * 60 + "\n")

    print(f"\n[报告已保存] {report_path}")

    # 控制台输出综合评估
    print(f"\n{'=' * 60}")
    print("综合风控评估")
    print(f"  ID格式: {'通过' if id_valid else '不通过'}")
    print(f"  串号检测: {'有风险' if has_duplicate else '无风险'}")
    print(f"  篡改检测: {'有风险' if has_tamper else '无风险'}")
    print(f"  综合风险等级: {risk_level}")
    print("=" * 60)

    return report_path


# =============================================================================
# 主函数
# =============================================================================
def main():
    """主入口"""
    parser = argparse.ArgumentParser(description="RPA ID 风控校验工具")
    parser.add_argument("--check-id", nargs=2, metavar=("USER_ID", "TASK_ID"), help="检查ID格式")
    parser.add_argument("--check-duplicate", metavar="TASK_ID", help="检查串号")
    parser.add_argument("--check-tamper", action="store_true", help="检查代码篡改")
    parser.add_argument("--target-dir", type=str, default=None, help="目标目录")
    parser.add_argument("--full-report", action="store_true", help="生成完整风控报告")
    parser.add_argument("--user-id", type=str, help="用户ID（用于完整报告）")
    parser.add_argument("--task-id", type=str, help="任务ID（用于完整报告）")
    args = parser.parse_args()

    target_dir = args.target_dir or ROOT_PATH

    # 检查ID格式
    if args.check_id:
        user_id, task_id = args.check_id
        check_id_legality(user_id, task_id)
        return

    # 检查串号
    if args.check_duplicate:
        check_id_duplicate(args.check_duplicate, target_dir)
        return

    # 检查篡改
    if args.check_tamper:
        check_code_tamper(target_dir)
        return

    # 生成完整风控报告
    if args.full_report:
        generate_risk_report(target_dir, args.user_id, args.task_id)
        return

    # 默认：显示帮助
    parser.print_help()


if __name__ == "__main__":
    main()
