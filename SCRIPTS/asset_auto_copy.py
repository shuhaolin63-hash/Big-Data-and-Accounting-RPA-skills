"""
资产自动复制脚本
根据作业场景从 f:\\RPA(1) 资产库复制模板到用户工作区。
支持场景映射字典，用 shutil.copytree 复制整个机器人目录。
"""

import os
import shutil
import sys

# 场景映射字典: 场景标识 -> 资产库中的机器人目录名 (相对 f:\\RPA(1) 的相对路径)
SCENE_MAP = {
    "invoice_check":        r"发票查验机器人\发票查验机器人",
    "invoice_open":         r"发票开具机器人\发票开具机器人",
    "invoice_certify":      r"发票认证机器人\发票认证机器人",
    "tax_login":            r"电子税务局平台登录机器人",
    "bank_pay":             r"网银付款机器人\网银付款机器人",
    "bank_corp_pay":        r"网银对公付款机器人（开发模板）_(2)",
    "bank_receive_query":   r"网银收款查询机器人\网银收款查询机器人",
}


def get_available_scenes():
    """获取所有可用场景列表"""
    return list(SCENE_MAP.keys())


def get_source_path(scene_key, asset_base=None):
    """根据场景键获取源路径"""
    if asset_base is None:
        asset_base = r"f:\RPA(1)"
    if scene_key not in SCENE_MAP:
        raise ValueError(f"未知场景: {scene_key}，可用场景: {list(SCENE_MAP.keys())}")
    return os.path.join(asset_base, SCENE_MAP[scene_key])


def copy_template(scene_key, target_dir, asset_base=None):
    """
    复制指定场景的机器人模板到目标目录。
    
    参数:
        scene_key: 场景标识，如 'invoice_check'
        target_dir: 目标工作区目录
        asset_base: 资产库根目录，默认 f:\\RPA(1)
    
    返回:
        成功返回目标路径，失败返回 None
    """
    source = get_source_path(scene_key, asset_base)

    # 检查源是否存在
    if not os.path.exists(source):
        print(f"错误: 源路径不存在 - {source}")
        return None

    # 检查源是否是目录
    if not os.path.isdir(source):
        print(f"错误: 源路径不是目录 - {source}")
        return None

    # 构建目标路径
    scene_name = SCENE_MAP[scene_key].split("\\")[-1]  # 取最后一级目录名
    dest = os.path.join(target_dir, scene_name)

    # 如果目标已存在，先询问是否覆盖
    if os.path.exists(dest):
        print(f"警告: 目标路径已存在 - {dest}")
        overwrite = input("是否覆盖? (y/n): ").strip().lower()
        if overwrite == "y":
            shutil.rmtree(dest)
            print(f"已删除旧目录: {dest}")
        else:
            print("跳过复制")
            return dest

    # 执行复制
    try:
        shutil.copytree(source, dest)
        print(f"复制成功: {source}")
        print(f"       -> {dest}")
        return dest
    except Exception as e:
        print(f"复制失败: {e}")
        return None


def batch_copy(scene_keys, target_dir, asset_base=None):
    """批量复制多个场景"""
    results = {}
    for key in scene_keys:
        print(f"\n--- 正在处理场景: {key} ---")
        result = copy_template(key, target_dir, asset_base)
        results[key] = result
    return results


def main():
    """主函数"""
    asset_base = r"f:\RPA(1)"
    if not os.path.exists(asset_base):
        print(f"错误: 资产库路径不存在 - {asset_base}")
        sys.exit(1)

    print("=" * 60)
    print("资产自动复制工具")
    print("=" * 60)
    print(f"资产库路径: {asset_base}")
    print(f"可用场景: {', '.join(get_available_scenes())}")
    print("-" * 60)

    # 交互式选择
    scene_input = input("请输入场景标识（多个用逗号分隔）或 all 选择全部: ").strip()
    target_dir = input("请输入目标工作区路径: ").strip()

    if not target_dir:
        print("错误: 目标路径不能为空")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True)

    if scene_input == "all":
        scenes = get_available_scenes()
    else:
        scenes = [s.strip() for s in scene_input.split(",") if s.strip()]

    print(f"\n准备复制以下场景: {scenes}")
    print(f"目标路径: {target_dir}")
    confirm = input("确认执行? (y/n): ").strip().lower()
    if confirm != "y":
        print("已取消")
        return

    batch_copy(scenes, target_dir, asset_base)
    print("\n全部完成")


if __name__ == "__main__":
    main()
