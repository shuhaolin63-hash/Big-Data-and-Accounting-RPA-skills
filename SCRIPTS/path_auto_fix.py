"""
路径自动修复脚本
智能检测本机路径，自动替换 .py / .json 中的硬编码路径。
支持检测 f:\\RPA(1) 是否存在、遍历其他盘符搜索 RPA 目录、
检测 C:\\RPADATA，一键检测+修复。
"""

import os
import re
import sys


def detect_local_asset_base():
    """
    检测本机资产库路径。
    优先检测 f:\\RPA(1)，不存在则遍历其他盘符搜索包含 "RPA" 的目录。
    返回: 检测到的路径字符串，未找到返回 None
    """
    # 优先检测 f:\\RPA(1)
    primary = r"f:\RPA(1)"
    if os.path.exists(primary):
        print(f"检测到资产库路径: {primary}")
        return primary

    print(f"默认路径 {primary} 不存在，正在搜索其他盘符...")

    # 遍历所有可用盘符
    detected = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            try:
                for item in os.listdir(drive):
                    item_path = os.path.join(drive, item)
                    if os.path.isdir(item_path) and "RPA" in item.upper():
                        detected.append(item_path)
            except PermissionError:
                continue
            except Exception:
                continue

    if detected:
        print(f"搜索到可能的资产库路径: {detected}")
        # 返回最匹配的（包含 RPA(1) 的优先，否则取第一个）
        for p in detected:
            if "RPA(1)" in p or "RPA1" in p:
                return p
        return detected[0]

    print("未搜索到资产库目录")
    return None


def detect_rpa_data_path():
    """
    检测 C:\\RPADATA 路径是否存在。
    返回: 路径字符串（存在则返回 C:\\RPADATA，否则返回 None）
    """
    path = r"C:\RPADATA"
    if os.path.exists(path):
        print(f"检测到 RPADATA 路径: {path}")
        return path
    else:
        print(f"RPADATA 路径不存在: {path}")
        return None


def replace_paths_in_files(project_dir, old_prefix, new_prefix):
    """
    替换 .py / .json 文件中的路径前缀。
    
    参数:
        project_dir: 项目目录
        old_prefix: 旧路径前缀
        new_prefix: 新路径前缀
    
    返回: 替换记录列表 [(文件路径, 替换次数)]
    """
    records = []
    target_exts = (".py", ".json")
    old_escaped = re.escape(old_prefix)
    pattern = re.compile(old_escaped, re.IGNORECASE)

    for root, dirs, files in os.walk(project_dir):
        # 跳过无关目录
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules", ".venv", "venv", ".idea")]
        for f in files:
            file_path = os.path.join(root, f)
            ext = os.path.splitext(f)[1]
            if ext not in target_exts:
                continue

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
            except Exception:
                continue

            new_content, count = pattern.subn(new_prefix, content)
            if count > 0:
                try:
                    with open(file_path, "w", encoding="utf-8") as fh:
                        fh.write(new_content)
                    records.append((file_path, count))
                    print(f"  [已替换] {file_path}  ({count} 处)")
                except Exception as e:
                    print(f"  [写入失败] {file_path} - {e}")

    return records


def auto_fix_all(project_dir, dry_run=False):
    """
    一键检测+修复项目中的所有路径。
    
    流程:
        1. 检测本地 f:\\RPA(1) 资产库路径
        2. 检测 C:\\RPADATA
        3. 扫描项目中的路径并替换
    
    参数:
        project_dir: 项目目录
        dry_run: 仅预览不修改
    
    返回: 汇总信息字典
    """
    print("=" * 60)
    print("      路径自动修复工具 - 一键检测 + 修复")
    print("=" * 60)

    if not os.path.exists(project_dir):
        print(f"错误: 项目目录不存在 - {project_dir}")
        return {"success": False, "error": "目录不存在"}

    result = {
        "project_dir": project_dir,
        "asset_base": None,
        "rpa_data": None,
        "replacements": [],
        "dry_run": dry_run,
    }

    # 第1步: 检测资产库路径
    print("\n[第1步] 检测资产库路径...")
    asset_base = detect_local_asset_base()
    result["asset_base"] = asset_base

    # 第2步: 检测 RPADATA
    print("\n[第2步] 检测 RPADATA 路径...")
    rpa_data = detect_rpa_data_path()
    result["rpa_data"] = rpa_data

    # 第3步: 扫描并替换路径
    print("\n[第3步] 扫描项目中的路径...")

    # 需要替换的映射
    replace_map = {}
    if asset_base:
        # 常见的可能旧路径前缀模式
        common_prefixes = [
            r"d:\RPA(1)", r"d:\RPA1", r"d:\RPA_1",
            r"e:\RPA(1)", r"e:\RPA1",
            r"c:\RPA(1)", r"c:\RPA1",
            r"f:\RPA(1)",  # 同名不同盘符的情况
        ]
        for prefix in common_prefixes:
            if prefix.lower() != asset_base.lower():
                replace_map[prefix] = asset_base

    if rpa_data:
        # 常见 RPADATA 旧路径
        old_rpa_data_prefixes = [
            r"d:\RPADATA", r"e:\RPADATA", r"f:\RPADATA",
        ]
        for prefix in old_rpa_data_prefixes:
            if prefix.lower() != rpa_data.lower():
                replace_map[prefix] = rpa_data

    if not replace_map:
        print("未检测到需要替换的路径映射")
    else:
        print(f"路径替换映射:")
        for old_p, new_p in replace_map.items():
            print(f"  {old_p} -> {new_p}")

        if dry_run:
            print("\n[预览模式] 仅扫描，不实际修改")
            # 预览模式：扫描受影响文件但不修改
            for old_p, new_p in replace_map.items():
                old_escaped = re.escape(old_p)
                pattern_re = re.compile(old_escaped, re.IGNORECASE)
                for root, dirs, files in os.walk(project_dir):
                    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
                    for f in files:
                        fp = os.path.join(root, f)
                        ext = os.path.splitext(f)[1]
                        if ext not in (".py", ".json"):
                            continue
                        try:
                            with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                                content = fh.read()
                            m = pattern_re.search(content)
                            if m:
                                cnt = len(pattern_re.findall(content))
                                print(f"  [检测] {fp}  ({cnt} 处, 旧路径: {old_p})")
                        except Exception:
                            continue
        else:
            print("\n执行路径替换...")
            for old_p, new_p in replace_map.items():
                records = replace_paths_in_files(project_dir, old_p, new_p)
                result["replacements"].extend(records)

    # 输出汇总
    print("\n" + "=" * 60)
    print("修复完成汇总")
    print(f"  项目目录: {project_dir}")
    print(f"  资产库路径: {asset_base or '未检测到'}")
    print(f"  RPADATA路径: {rpa_data or '未检测到'}")
    if result["replacements"]:
        total = sum(r[1] for r in result["replacements"])
        print(f"  已替换文件: {len(result['replacements'])} 个")
        print(f"  总替换次数: {total}")
    else:
        print(f"  替换情况: {'预览模式' if dry_run else '无需替换'}")

    result["success"] = True
    return result


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="路径自动修复工具")
    parser.add_argument("project_dir", nargs="?", default=os.getcwd(), help="项目目录路径（默认当前目录）")
    parser.add_argument("--dry-run", action="store_true", help="仅扫描预览，不执行修改")
    args = parser.parse_args()

    auto_fix_all(args.project_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
