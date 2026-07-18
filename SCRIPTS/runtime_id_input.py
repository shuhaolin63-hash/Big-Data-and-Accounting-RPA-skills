"""
运行时动态ID注入脚本
负责接收、校验并注入用户 UserID / TaskID 到环境变量。
支持 UUID 格式校验、32位十六进制校验、交互式输入。"""

import os
import re
import sys

# 内存缓存
_injected_ids = {}


def validate_user_id(user_id):
    """
    校验 UserID 是否为标准 UUID 格式。
    格式: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    返回: (是否合法, 错误信息)
    """
    if not user_id or not user_id.strip():
        return False, "UserID 不能为空"

    user_id = user_id.strip()
    pattern = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    if re.match(pattern, user_id):
        return True, ""
    else:
        return False, "UserID 格式错误，应为 UUID 格式: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"


def validate_task_id(task_id):
    """
    校验 TaskID 是否为32位十六进制格式。
    格式: 32位十六进制字符（可含连字符）
    返回: (是否合法, 错误信息)
    """
    if not task_id or not task_id.strip():
        return False, "TaskID 不能为空"

    task_id = task_id.strip()
    # 允许带连字符的32位十六进制
    raw = task_id.replace("-", "")
    if len(raw) != 32:
        return False, f"TaskID 长度应为32位十六进制，当前长度为 {len(raw)}"
    if not re.match(r'^[0-9a-fA-F]{32}$', raw):
        return False, "TaskID 包含非法字符，仅允许 0-9 a-f A-F"
    return True, ""


def inject_id_to_env(user_id, task_id):
    """
    将 UserID 和 TaskID 注入到环境变量和内存缓存。
    参数:
        user_id: 用户ID (UUID格式)
        task_id: 任务ID (32位十六进制)
    返回: (是否成功, 错误信息)
    """
    # 校验 UserID
    user_valid, user_err = validate_user_id(user_id)
    if not user_valid:
        return False, f"UserID 校验失败: {user_err}"

    # 校验 TaskID
    task_valid, task_err = validate_task_id(task_id)
    if not task_valid:
        return False, f"TaskID 校验失败: {task_err}"

    user_id = user_id.strip()
    task_id = task_id.strip()

    # 注入环境变量
    os.environ["RPA_USER_ID"] = user_id
    os.environ["RPA_TASK_ID"] = task_id

    # 写入内存缓存
    _injected_ids["user_id"] = user_id
    _injected_ids["task_id"] = task_id

    return True, ""


def get_injected_id():
    """
    获取当前注入的ID字典。
    返回: {"user_id": str, "task_id": str}，未注入时值为 None
    """
    return {
        "user_id": os.environ.get("RPA_USER_ID") or _injected_ids.get("user_id"),
        "task_id": os.environ.get("RPA_TASK_ID") or _injected_ids.get("task_id"),
    }


def clear_id():
    """清除内存和环境变量中的ID"""
    # 清除环境变量
    for key in ["RPA_USER_ID", "RPA_TASK_ID"]:
        if key in os.environ:
            del os.environ[key]
    # 清除内存缓存
    _injected_ids.clear()
    print("已清除所有ID信息")


def interactive_input():
    """
    交互式引导用户输入 UserID 和 TaskID。
    循环校验直到输入合法，用户可输入 q 退出。
    返回: (user_id, task_id) 或 (None, None) 表示退出
    """
    print("=" * 60)
    print("运行时 ID 输入工具")
    print("输入 q 可随时退出")
    print("=" * 60)

    # 输入 UserID
    user_id = None
    while user_id is None:
        raw = input("\n请输入 UserID（UUID格式 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx）: ").strip()
        if raw.lower() == "q":
            print("已退出")
            return None, None
        valid, err = validate_user_id(raw)
        if valid:
            user_id = raw
        else:
            print(f"  [错误] {err}")
            print(f"  示例: 550e8400-e29b-41d4-a716-446655440000")

    # 输入 TaskID
    task_id = None
    while task_id is None:
        raw = input("\n请输入 TaskID（32位十六进制，可带连字符）: ").strip()
        if raw.lower() == "q":
            print("已退出")
            return None, None
        valid, err = validate_task_id(raw)
        if valid:
            task_id = raw
        else:
            print(f"  [错误] {err}")
            print(f"  示例: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6")

    # 注入
    success, err_msg = inject_id_to_env(user_id, task_id)
    if success:
        print(f"\nID 注入成功！")
        print(f"  RPA_USER_ID = {user_id}")
        print(f"  RPA_TASK_ID = {task_id}")
    else:
        print(f"\nID 注入失败: {err_msg}")
        return None, None

    return user_id, task_id


def main():
    """主函数"""
    result = interactive_input()
    if result[0] is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
