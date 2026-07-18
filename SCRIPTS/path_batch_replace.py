"""
批量路径替换脚本
正则匹配 Windows 路径格式 [A-Za-z]:\\xxx，
遍历工程中 .py / .json / .flow.json / .variable.json 文件。
auto_detect_and_fix(project_dir) 自动检测并修复，输出替换报告。
"""

import os
import re
import sys

# 匹配 Windows 绝对路径的正则: 盘符:\开头
WINDOWS_PATH_PATTERN = re.compile(r'[A-Za-z]:\\(?:[^\\:"*?<>|\n]*\\)*[^\\:"*?<>|\n]*')

# 需要处理的文件扩展名
TARGET_EXTENSIONS = (".py", ".json")
# 需要处理的文件名完整匹配（含扩展名）
TARGET_FILENAMES = (".flow.json", ".variable.json")

# 替换排除模式（包含这些路径的不替换）
EXCLUDE_PATTERNS = [
    r'C:\\Windows',
    r'C:\\Program Files',
    r'C:\\Program Files \(x86\)',
    r'C:\\Users\\.*\\AppData',
]


def should_exclude(path_str):
    """判断路径是否应排除替换"""
    for pattern in EXCLUDE_PATTERNS:
        if re.match(pattern, path_str, re.IGNORECASE):
            return True
    return False


def collect_target_files(project_dir):
    """收集项目中需要处理的文件"""
    target_files = []
    for root, dirs, files in os.walk(project_dir):
        # 跳过 .git、__pycache__、node_modules、.venv 等目录
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules", ".venv", "venv", ".idea")]
        for f in files:
            file_path = os.path.join(root, f)
            ext = os.path.splitext(f)[1]
            # .flow.json 和 .variable.json 的扩展名是 .json，用完整文件名匹配
            if f.endswith(".flow.json") or f.endswith(".variable.json"):
                target_files.append(file_path)
            elif ext in TARGET_EXTENSIONS and not f.endswith(".flow.json") and not f.endswith(".variable.json"):
                target_files.append(file_path)
    return target_files


def detect_paths_in_file(file_path):
    """检测文件中的 Windows 绝对路径"""
    paths_found = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"  读取失败: {file_path} - {e}")
        return paths_found

    matches = WINDOWS_PATH_PATTERN.findall(content)
    unique_paths = set(m.strip() for m in matches if m.strip())
    for p in sorted(unique_paths):
        if not should_exclude(p):
            paths_found.append(p)
    return paths_found


def replace_paths_in_file(file_path, old_prefix, new_prefix, dry_run=False):
    """
    在单个文件中替换路径前缀。
    返回 (替换次数, 是否修改)
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"  读取失败: {file_path} - {e}")
        return 0, False

    # 转义路径中的反斜杠用于正则
    old_escaped = re.escape(old_prefix)
    # 替换路径前缀（不区分大小写匹配盘符）
    pattern = re.compile(old_escaped, re.IGNORECASE)
    new_content, count = pattern.subn(new_prefix, content)

    if count > 0 and not dry_run:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
        except Exception as e:
            print(f"  写入失败: {file_path} - {e}")
            return 0, False

    return count, count > 0


def auto_detect_and_fix(project_dir, new_prefix=None, dry_run=False):
    """
    自动检测项目中的 Windows 绝对路径并修复。
    
    参数:
        project_dir: 项目目录
        new_prefix: 替换为目标前缀，如 r"f:\\RPA(1)"。为 None 时仅检测不替换
        dry_run: 如果为 True，仅预览不实际修改
    
    返回: 汇总报告字符串
    """
    if not os.path.exists(project_dir):
        return f"错误: 目录不存在 - {project_dir}"

    print(f"正在扫描目录: {project_dir}")
    files = collect_target_files(project_dir)
    print(f"找到 {len(files)} 个目标文件")

    # 自动检测最常见的路径前缀
    path_prefixes = {}
    for fp in files:
        paths = detect_paths_in_file(fp)
        for p in paths:
            # 提取前缀: 前两级路径，如 d:\some_dir
            parts = p.split("\\")
            if len(parts) >= 3:
                prefix = "\\".join(parts[:3])
                path_prefixes.setdefault(prefix, [])
                path_prefixes[prefix].append(fp)

    # 生成报告
    lines = []
    lines.append("=" * 70)
    lines.append("            批量路径替换分析报告")
    lines.append("=" * 70)
    lines.append(f"项目目录: {project_dir}")
    lines.append(f"扫描文件数: {len(files)}")
    lines.append("")

    if not path_prefixes:
        lines.append("未检测到需要替换的路径。")
        lines.append("=" * 70)
        report = "\n".join(lines)
        print(report)
        return report

    lines.append("检测到的路径前缀:")
    for prefix, file_list in sorted(path_prefixes.items()):
        lines.append(f"  前缀: {prefix}  (出现在 {len(file_list)} 个文件中)")
        for fp in sorted(set(file_list)):
            lines.append(f"    - {fp}")
    lines.append("")

    # 如果提供了 new_prefix 则执行替换
    if new_prefix and path_prefixes:
        total_replacements = 0
        for old_prefix in sorted(path_prefixes.keys()):
            affected_files = set(path_prefixes[old_prefix])
            print(f"\n替换前缀: {old_prefix} -> {new_prefix}")
            for fp in sorted(affected_files):
                count, modified = replace_paths_in_file(fp, old_prefix, new_prefix, dry_run=dry_run)
                if count > 0:
                    status = "[预览]" if dry_run else "[已替换]"
                    print(f"  {status} {fp}  (替换 {count} 处)")
                    total_replacements += count

        lines.append(f"替换目标前缀: {new_prefix}")
        mode = "预览模式（未实际修改）" if dry_run else "已执行替换"
        lines.append(f"模式: {mode}")
        lines.append(f"总替换次数: {total_replacements}")

    lines.append("")
    lines.append("=" * 70)
    lines.append("分析完成")
    report = "\n".join(lines)
    print(report)
    return report


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="批量路径替换工具")
    parser.add_argument("project_dir", nargs="?", default=os.getcwd(), help="项目目录路径（默认当前目录）")
    parser.add_argument("--new-prefix", help="新路径前缀，如 f:\\\\RPA(1)")
    parser.add_argument("--dry-run", action="store_true", help="仅预览不修改")
    args = parser.parse_args()

    auto_detect_and_fix(args.project_dir, args.new_prefix, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
