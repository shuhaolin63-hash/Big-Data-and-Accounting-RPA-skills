#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键环境初始化脚本
检查并准备 Big-Data-and-Accounting-RPA-skills 所需的运行环境
"""

import os
import sys
import subprocess
import shutil

REQUIRED_PYTHON = (3, 9)
ASSET_BASE = r"f:\RPA(1)"
PROJECT_DIR = r"f:\RPA(1)\Big-Data-and-Accounting-RPA-skills"


def print_step(step, msg, status=""):
    status_icon = {"ok": "  ✅", "fail": "  ❌", "warn": "  ⚠️", "info": "  ℹ️"}
    icon = status_icon.get(status, "  ▶️")
    print(f"{icon} [{step}] {msg}")


def check_python():
    """检查 Python 版本"""
    v = sys.version_info
    if v.major >= REQUIRED_PYTHON[0] and v.minor >= REQUIRED_PYTHON[1]:
        print_step("Python", f"版本 {v.major}.{v.minor}.{v.micro} ✅", "ok")
        return True
    else:
        print_step("Python", f"需要 >= {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}，当前 {v.major}.{v.minor}", "fail")
        return False


def check_pillow():
    """检查 Pillow 库"""
    try:
        import PIL
        print_step("Pillow", f"已安装（版本 {PIL.__version__}）", "ok")
        return True
    except ImportError:
        print_step("Pillow", "未安装，执行: pip install Pillow", "warn")
        return False


def check_asset_base():
    """检查资产根目录"""
    if os.path.exists(ASSET_BASE):
        items = os.listdir(ASSET_BASE)
        png_count = len([f for f in items if f.endswith('.png')])
        xls_count = len([f for f in items if f.endswith('.xls')])
        robot_dirs = [f for f in items if os.path.isdir(os.path.join(ASSET_BASE, f)) and '机器' in f]
        print_step("资产根目录", f"{ASSET_BASE} 存在（{png_count} 张图片, {xls_count} 个表格, {len(robot_dirs)} 个机器人目录）", "ok")
        return True
    else:
        print_step("资产根目录", f"{ASSET_BASE} 不存在", "fail")
        return False


def check_project_structure():
    """检查项目目录结构完整性"""
    required_dirs = [
        "ASSET/img_asset",
        "ASSET/excel_template",
        "ASSET/homework_history",
        "ASSET/py_base_template",
        "ASSET/robots",
        "REFERENCE/ui_guide",
        "SCRIPTS",
        "AGENTS/agent_teacher",
        "AGENTS/agent_fix_crack",
        "AGENTS/agent_module_asset",
        "USER_WORKSPACE",
    ]
    all_ok = True
    for d in required_dirs:
        full = os.path.join(PROJECT_DIR, d)
        if os.path.exists(full):
            print_step("目录结构", f"{d}/", "ok")
        else:
            print_step("目录结构", f"{d}/ 缺失", "fail")
            all_ok = False
    return all_ok


def check_skills():
    """检查 SKILL 文件"""
    skill_files = [
        "SKILL.md",
        ".trae/skills/Big-Data-and-Accounting-RPA-skills/SKILL.md",
        ".trae/skills/rpa-teacher-agent/SKILL.md",
        ".trae/skills/rpa-crack-agent/SKILL.md",
        ".trae/skills/rpa-module-asset-agent/SKILL.md",
    ]
    all_ok = True
    for sf in skill_files:
        full = os.path.join(PROJECT_DIR, sf)
        if os.path.exists(full):
            print_step("SKILL文件", sf, "ok")
        else:
            print_step("SKILL文件", f"{sf} 缺失", "fail")
            all_ok = False
    return all_ok


def install_dependencies():
    """安装 Python 依赖"""
    print("\n  ▶️  正在安装依赖...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"],
                       capture_output=True, check=True)
        print_step("依赖安装", "Pillow 安装成功", "ok")
        return True
    except subprocess.CalledProcessError:
        print_step("依赖安装", "Pillow 安装失败，请手动执行: pip install Pillow", "fail")
        return False


def init_user_workspace():
    """初始化用户工作区"""
    workspace = os.path.join(PROJECT_DIR, "USER_WORKSPACE")
    os.makedirs(os.path.join(workspace, "current_homework"), exist_ok=True)
    print_step("用户工作区", "current_homework/ 就绪", "ok")

    # 检查 user_id_config.yaml
    config_file = os.path.join(workspace, "user_id_config.yaml")
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if '{{USER_ID}}' in content:
            print_step("ID配置", "user_id_config.yaml 待填写（含占位符）", "warn")
        else:
            print_step("ID配置", "user_id_config.yaml 已配置", "ok")
    else:
        print_step("ID配置", "user_id_config.yaml 缺失", "fail")


def show_summary(results):
    """显示汇总"""
    total = len(results)
    passed = sum(1 for r in results.values() if r)
    print(f"\n{'='*50}")
    print(f"  环境检查完成：{passed}/{total} 项通过")
    if passed == total:
        print(f"  ✅ 环境就绪！可以开始使用 Big-Data-and-Accounting-RPA-skills")
    else:
        print(f"  ⚠️  请修复上述未通过项后再使用")
    print(f"{'='*50}")


def main():
    print(f"{'='*50}")
    print(f"  Big-Data-and-Accounting-RPA-skills 环境初始化")
    print(f"{'='*50}\n")

    results = {}

    # 1. 检查 Python
    results["Python"] = check_python()

    # 2. 检查项目目录结构
    results["目录结构"] = check_project_structure()

    # 3. 检查 SKILL 文件
    results["SKILL文件"] = check_skills()

    # 4. 检查资产根目录
    results["资产根目录"] = check_asset_base()

    # 5. 检查 Pillow
    pillow_ok = check_pillow()
    results["Pillow"] = pillow_ok

    # 6. 初始化用户工作区
    init_user_workspace()

    # 7. 如果 Pillow 缺失，自动安装
    if not pillow_ok:
        print()
        ans = input("  是否自动安装 Pillow? (y/n): ").strip().lower()
        if ans == 'y':
            results["Pillow"] = install_dependencies()
        else:
            print_step("Pillow", "跳过安装，资产检查脚本会跳过图片尺寸检测", "warn")

    # 8. 汇总
    show_summary(results)

    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
