"""
资产存在性检查脚本
扫描 f:\\RPA(1) 下所有资产，检查 .xls 表格、.png 图片、
各机器人目录的 dependencies/Assess 和 Select_file 组件完整性。
输出汇总报告。
"""

import os
import sys
from pathlib import Path
from PIL import Image


def check_xls_files(base_dir):
    """检查 .xls 表格文件"""
    xls_files = list(Path(base_dir).rglob("*.xls"))
    results = []
    for f in xls_files:
        exists = os.path.exists(f)
        size = os.path.getsize(f) if exists else 0
        results.append({
            "type": "xls",
            "path": str(f),
            "exists": exists,
            "size_kb": round(size / 1024, 2)
        })
    return results


def check_png_files(base_dir):
    """检查 .png 图片文件，用 PIL 读取尺寸"""
    png_files = list(Path(base_dir).rglob("*.png"))
    results = []
    for f in png_files:
        exists = os.path.exists(f)
        width = height = 0
        if exists:
            try:
                img = Image.open(f)
                width, height = img.size
                img.close()
            except Exception:
                pass
        results.append({
            "type": "png",
            "path": str(f),
            "exists": exists,
            "width": width,
            "height": height
        })
    return results


def check_robot_components(base_dir):
    """检查各机器人目录下的 dependencies/Assess 和 Select_file 组件"""
    results = []
    for robot_dir in Path(base_dir).iterdir():
        if not robot_dir.is_dir():
            continue
        # 检查 dependencies/Assess
        assess_path = robot_dir / "dependencies" / "Assess"
        assess_exists = os.path.isdir(assess_path)
        assess_files = []
        if assess_exists:
            assess_files = [str(f.name) for f in sorted(assess_path.iterdir())]
        results.append({
            "type": "component_assess",
            "robot": robot_dir.name,
            "path": str(assess_path),
            "exists": assess_exists,
            "files": assess_files
        })
        # 检查 Select_file
        select_path = robot_dir / "Select_file"
        select_exists = os.path.isdir(select_path)
        select_files = []
        if select_exists:
            select_files = [str(f.name) for f in sorted(select_path.iterdir())]
        results.append({
            "type": "component_select_file",
            "robot": robot_dir.name,
            "path": str(select_path),
            "exists": select_exists,
            "files": select_files
        })
    return results


def generate_report(xls_results, png_results, component_results):
    """生成汇总报告"""
    lines = []
    lines.append("=" * 70)
    lines.append("              资产完整性检查汇总报告")
    lines.append("=" * 70)
    lines.append(f"检查时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # XLS 统计
    xls_total = len(xls_results)
    xls_missing = sum(1 for r in xls_results if not r["exists"])
    lines.append(f"[.xls 表格文件]  总数: {xls_total},  缺失: {xls_missing}")
    if xls_missing > 0:
        for r in xls_results:
            if not r["exists"]:
                lines.append(f"  - 缺失: {r['path']}")
    lines.append("")

    # PNG 统计
    png_total = len(png_results)
    png_missing = sum(1 for r in png_results if not r["exists"])
    lines.append(f"[.png 图片文件]  总数: {png_total},  缺失: {png_missing}")
    if png_missing > 0:
        for r in png_results:
            if not r["exists"]:
                lines.append(f"  - 缺失: {r['path']}")
    lines.append("")

    # 组件统计
    assess_total = sum(1 for r in component_results if r["type"] == "component_assess")
    assess_missing = sum(1 for r in component_results if r["type"] == "component_assess" and not r["exists"])
    select_total = sum(1 for r in component_results if r["type"] == "component_select_file")
    select_missing = sum(1 for r in component_results if r["type"] == "component_select_file" and not r["exists"])
    lines.append(f"[dependencies/Assess 组件]  检查: {assess_total},  缺失: {assess_missing}")
    if assess_missing > 0:
        for r in component_results:
            if r["type"] == "component_assess" and not r["exists"]:
                lines.append(f"  - 缺失: {r['robot']} -> {r['path']}")
    lines.append(f"[Select_file 组件]        检查: {select_total},  缺失: {select_missing}")
    if select_missing > 0:
        for r in component_results:
            if r["type"] == "component_select_file" and not r["exists"]:
                lines.append(f"  - 缺失: {r['robot']} -> {r['path']}")
    lines.append("")

    # 详细列表
    lines.append("-" * 70)
    lines.append("详细 .xls 文件列表:")
    for r in xls_results:
        flag = "OK" if r["exists"] else "MISS"
        lines.append(f"  [{flag}] {r['path']}  ({r['size_kb']} KB)")

    lines.append("")
    lines.append("详细 .png 文件列表:")
    for r in png_results:
        flag = "OK" if r["exists"] else "MISS"
        dim = f"{r['width']}x{r['height']}" if r["exists"] else "N/A"
        lines.append(f"  [{flag}] {r['path']}  ({dim})")

    lines.append("")
    lines.append("详细组件检查:")
    for r in component_results:
        flag = "OK" if r["exists"] else "MISS"
        if r["type"] == "component_assess":
            lines.append(f"  [{flag}] {r['path']}  files={r['files']}")
        else:
            lines.append(f"  [{flag}] {r['path']}  files={r['files']}")

    lines.append("")
    lines.append("=" * 70)
    lines.append("检查完成")
    return "\n".join(lines)


def main():
    """主函数"""
    base_dir = r"f:\RPA(1)"
    if not os.path.exists(base_dir):
        print(f"错误: 资产目录不存在 - {base_dir}")
        sys.exit(1)

    print(f"正在扫描资产目录: {base_dir}")
    xls_results = check_xls_files(base_dir)
    png_results = check_png_files(base_dir)
    component_results = check_robot_components(base_dir)

    report = generate_report(xls_results, png_results, component_results)
    print(report)

    # 保存报告
    report_path = os.path.join(base_dir, "asset_check_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n报告已保存至: {report_path}")


if __name__ == "__main__":
    main()
