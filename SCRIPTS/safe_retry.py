"""
安全重试机制脚本
为 RPA 操作提供通用重试、网页操作安全封装、文件操作安全封装。
支持自定义重试次数和延迟、异常捕获与日志。
"""

import os
import time
import traceback
from functools import wraps


def safe_execute(func, max_retries=3, retry_delay=2):
    """
    通用重试执行器。
    以指定重试次数和延迟执行函数，捕获所有异常并重试。
    
    参数:
        func: 可调用对象
        max_retries: 最大重试次数（默认3次）
        retry_delay: 重试间隔秒数（默认2秒）
    
    返回:
        (是否成功, 结果或异常信息)
    """
    last_exception = None
    for attempt in range(1, max_retries + 1):
        try:
            result = func()
            return True, result
        except Exception as e:
            last_exception = e
            print(f"  执行失败 (第{attempt}/{max_retries}次): {e}")
            if attempt < max_retries:
                print(f"  等待 {retry_delay} 秒后重试...")
                time.sleep(retry_delay)
            else:
                print(f"  已达到最大重试次数 {max_retries}")
                traceback.print_exc()

    return False, last_exception


def safe_web_operation(browser_obj, operation, element, max_retries=3):
    """
    网页操作安全封装。
    
    参数:
        browser_obj: 浏览器对象（应支持 element 操作方法）
        operation: 操作类型字符串，如 "click", "input", "get_text", "is_visible"
        element: 元素选择器或元素对象
        max_retries: 最大重试次数
    
    返回:
        (是否成功, 结果或异常信息)
    """
    operation_map = {
        "click":     lambda: browser_obj.click(element),
        "input":     lambda: browser_obj.input_text(element),
        "get_text":  lambda: browser_obj.get_text(element),
        "is_visible": lambda: browser_obj.is_visible(element),
        "wait":      lambda: browser_obj.wait(element),
    }

    if operation not in operation_map:
        return False, f"不支持的操作: {operation}，支持: {list(operation_map.keys())}"

    return safe_execute(operation_map[operation], max_retries=max_retries, retry_delay=2)


def safe_web_click(browser_obj, element, max_retries=3):
    """
    安全点击操作封装。
    
    参数:
        browser_obj: 浏览器对象
        element: 要点击的元素
        max_retries: 最大重试次数
    
    返回:
        (是否成功, 异常信息或None)
    """
    return safe_web_operation(browser_obj, "click", element, max_retries=max_retries)


def safe_web_input(browser_obj, element, text, max_retries=3):
    """
    安全输入操作封装。
    
    参数:
        browser_obj: 浏览器对象
        element: 输入框元素
        text: 要输入的文本
        max_retries: 最大重试次数
    
    返回:
        (是否成功, 异常信息或None)
    """
    def do_input():
        browser_obj.click(element)
        browser_obj.clear(element)
        browser_obj.input_text(element, text)
        return True

    return safe_execute(do_input, max_retries=max_retries, retry_delay=2)


def safe_file_operation(file_path, operation_func, max_retries=2):
    """
    文件操作安全封装。
    处理文件锁定、权限错误等常见文件操作异常。
    
    参数:
        file_path: 文件路径
        operation_func: 文件操作函数（接收 file_path 作为参数）
        max_retries: 最大重试次数（默认2次）
    
    返回:
        (是否成功, 结果或异常信息)
    """
    def wrapper():
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        return operation_func(file_path)

    return safe_execute(wrapper, max_retries=max_retries, retry_delay=1)


def safe_screenshot(browser_obj, save_path, max_retries=3):
    """
    安全截图操作封装。
    
    参数:
        browser_obj: 浏览器对象（应支持 screenshot 方法）
        save_path: 截图保存路径
        max_retries: 最大重试次数
    
    返回:
        (是否成功, 异常信息或None)
    """
    def do_screenshot():
        # 确保目标目录存在
        save_dir = os.path.dirname(save_path)
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        # 执行截图
        browser_obj.screenshot(save_path)

        # 验证截图文件是否生成
        if not os.path.exists(save_path):
            raise RuntimeError(f"截图文件未生成: {save_path}")
        if os.path.getsize(save_path) == 0:
            raise RuntimeError(f"截图文件为空: {save_path}")

        return save_path

    return safe_execute(do_screenshot, max_retries=max_retries, retry_delay=2)


# ==================== 装饰器风格 ====================


def retry(max_retries=3, retry_delay=2):
    """
    重试装饰器。
    
    用法:
        @retry(max_retries=3, retry_delay=2)
        def my_function():
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"  [{func.__name__}] 失败 (第{attempt}/{max_retries}次): {e}")
                    if attempt < max_retries:
                        print(f"  等待 {retry_delay} 秒后重试...")
                        time.sleep(retry_delay)
                    else:
                        print(f"  [{func.__name__}] 已达到最大重试次数 {max_retries}")
                        raise
            return None  # 不会执行到这里
        return wrapper
    return decorator


# ==================== 使用示例 ====================

if __name__ == "__main__":
    import random

    print("=" * 50)
    print("安全重试机制 - 测试")

    # 测试通用重试
    def unstable_function():
        if random.random() < 0.7:
            raise ConnectionError("模拟网络异常")
        return "成功"

    print("\n1. 测试 safe_execute（模拟70%概率失败）:")
    success, result = safe_execute(unstable_function, max_retries=5, retry_delay=1)
    print(f"   结果: {'成功' if success else '失败'}, 返回值: {result}")

    # 测试装饰器风格
    print("\n2. 测试 @retry 装饰器:")
    @retry(max_retries=3, retry_delay=1)
    def fetch_data():
        if random.random() < 0.5:
            raise TimeoutError("模拟超时")
        return "数据获取成功"

    try:
        result = fetch_data()
        print(f"   结果: {result}")
    except Exception as e:
        print(f"   最终失败: {e}")

    print("\n测试完成")
