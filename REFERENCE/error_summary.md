# 常见运行错误汇总表

本文档汇总了 RPA 课程作业中常见的运行错误类型、错误信息、可能原因及解决方案。

---

## 错误汇总表

| # | 错误类型 | 错误信息 | 可能原因 | 解决方案 |
|---|----------|----------|----------|----------|
| 1 | **导入错误** | `ModuleNotFoundError: No module named 'rpa'` | RPA 环境未正确安装或激活 | 确认已安装 RPA Studio 并配置了 Python 环境；检查是否在虚拟环境中运行 |
| 2 | **导入错误** | `ModuleNotFoundError: No module named 'xlrd'` | 缺少 Excel 文件读取库 | 执行 `pip install xlrd` 安装 xlrd 库 |
| 3 | **导入错误** | `ImportError: cannot import name 'xxx' from 'rpa'` | RPA 模块版本不匹配 | 检查 rpa 模块版本，部分函数名在不同版本中有变更；查看官方文档确认正确 API |
| 4 | **文件未找到** | `FileNotFoundError: [Errno 2] No such file or directory: 'xxx.xls'` | Excel 数据表路径不存在或文件名错误 | 检查路径是否正确；确认文件存在于指定目录；运行 `path_batch_replace.py` 自动修复路径 |
| 5 | **文件未找到** | `FileNotFoundError: 'f:\\RPA(1)\\xxx\\main.py'` | 工程文件路径不正确 | 确认工程目录结构完整；检查文件夹名是否包含特殊字符或空格 |
| 6 | **文件未找到** | 截图/图片文件路径错误 | 图片素材缺失或路径配置错误 | 运行 `asset_exists_check.py` 检查图片资产完整性；手动确认图片文件是否存在 |
| 7 | **权限错误** | `PermissionError: [Errno 13] Permission denied` | 文件被其他程序占用或只读属性 | 关闭已打开的 Excel/文件；去掉文件的只读属性；以管理员身份运行 |
| 8 | **编码错误** | `UnicodeDecodeError: 'gbk' codec can't decode byte xxx` | 文件编码格式与 Python 默认编码不匹配 | 使用 `encoding='utf-8'` 或 `encoding='gbk'` 指定正确编码；推荐统一使用 UTF-8 |
| 9 | **Excel 错误** | `xlrd.biffh.XLRDError: Excel xlsx file; not supported` | xlrd 新版本不支持 .xlsx 格式 | 降级 xlrd 到 1.2.0：`pip install xlrd==1.2.0`；或改用 openpyxl 读取 .xlsx |
| 10 | **Excel 错误** | `IndexError: list index out of range` 读取 Excel 行/列 | 数据表格结构变更，表头行或数据行索引错误 | 检查 Excel 表格结构；确认行/列索引与代码中一致；打印 sheet.nrows 和 sheet.ncols 调试 |
| 11 | **Excel 错误** | `TypeError: 'NoneType' object is not subscriptable` | Excel 单元格值为空 | 检查数据是否完整；使用 `if cell_value` 判空处理 |
| 12 | **类型错误** | `TypeError: expected string or bytes-like object` | 函数参数类型不匹配 | 检查传入参数类型；使用 `str()` 转换或 `isinstance()` 类型检查 |
| 13 | **属性错误** | `AttributeError: 'NoneType' object has no attribute 'click'` | 未找到页面元素，click() 返回 None | 增加等待时间确保元素加载完成；检查选择器是否正确；使用 try/except 捕获 |
| 14 | **超时错误** | `TimeoutException: Message: timeout` | 页面加载或元素等待超时 | 增加 timeout 值（建议 10-30 秒）；检查网络连接；确认页面是否有异常弹窗 |
| 15 | **超时错误** | 等待时间不足导致元素未加载 | sleep 时间设置过短 | 将固定 sleep 改为智能等待（WebDriverWait）；至少保证 3-5 秒等待时间 |
| 16 | **选择器错误** | `NoSuchElementException: Unable to locate element` | CSS/XPath 选择器路径错误或元素不存在 | 检查选择器路径是否准确；确认页面已加载目标元素；使用浏览器开发者工具验证选择器 |
| 17 | **选择器错误** | `StaleElementReferenceException: element is not attached to the page document` | 页面刷新或 DOM 更新导致元素引用失效 | 重新定位元素；在每次操作前重新查找元素而非缓存引用 |
| 18 | **JavaScript 错误** | `JavascriptException: TypeError: xxx is not a function` | 页面脚本执行异常 | 确认页面是否正常加载 JS 资源；尝试增加延迟等待 JS 执行完成 |
| 19 | **窗口错误** | `NoSuchWindowException: target window already closed` | 窗口已关闭但代码仍尝试操作 | 检查窗口句柄管理逻辑；操作前确认窗口是否仍处于打开状态 |
| 20 | **窗口错误** | 弹窗/新窗口无法定位 | 浏览器弹窗被拦截或新窗口未完全打开 | 关闭弹窗拦截功能；使用 `switch_to.window()` 切换到新窗口 |
| 21 | **变量错误** | `KeyError: 'xxx'` 字典键不存在 | 变量配置文件中缺少某个键 | 检查 variable.json / ctrl.json 中的键定义；确认键名拼写正确 |
| 22 | **变量错误** | `json.JSONDecodeError: Expecting value: line 1 column 1` | JSON 文件格式错误或为空 | 检查 .json 文件格式是否合法；使用 JSON 验证工具检查文件；避免手动编辑 JSON 引入格式错误 |
| 23 | **流程错误** | `FlowExecutionError: xxx step failed` | .flow.json 流程步骤执行失败 | 检查 flow.json 中的步骤定义；确认每一步的输入输出参数正确 |
| 24 | **流程错误** | 循环处理中途中断 | 某条数据处理时出现未捕获异常 | 在循环中使用 try/except 捕获异常；添加 continue 跳过失败数据并记录日志 |
| 25 | **路径错误** | `OSError: [WinError 123] 文件名、目录名或卷标语法不正确` | 路径中包含非法字符 | 检查路径中是否包含 `:`、`*`、`?` 等非法字符；使用 `os.path.join()` 拼接路径 |
| 26 | **路径错误** | 路径中的反斜杠未转义 | Windows 路径中的 `\` 未使用 `\\` 或原始字符串 | 使用双反斜杠 `\\` 或 `r"f:\RPA(1)"` 原始字符串；推荐使用 `os.path.join()` |
| 27 | **编码错误（Base64）** | `binascii.Error: Incorrect padding` | Base64 字符串格式不正确 | 检查 Base64 编码是否完整；添加 `=` 填充；确认要解码的字符串确实是 Base64 编码 |
| 28 | **网络错误** | `urllib.error.URLError: <urlopen error [WinError 10060]>` | 目标系统网站无法访问 | 检查网络连接；确认目标系统 URL 是否正确；确认是否在校园网/VPN 环境下 |
| 29 | **识别错误** | OCR/验证码识别失败 | 验证码图片质量差或识别模型不匹配 | 提高截图质量；更换验证码识别服务；考虑手动输入验证码方案 |
| 30 | **运行时错误** | RPA 引擎崩溃或闪退 | 内存不足或系统资源耗尽 | 关闭不必要的程序释放内存；减少 RPA 操作并发数；重启 RPA Studio |

---

## 错误排查通用流程

当遇到未知错误时，按以下步骤排查：

```
Step 1: 查看错误信息
  │  确认错误类型和具体的错误信息文本
  ▼
Step 2: 定位错误位置
  │  确认报错发生在哪个文件、哪个函数、哪一行
  ▼
Step 3: 分析可能原因
  │  参考上表，找到对应的错误类型和原因
  ▼
Step 4: 尝试解决方案
  │  按推荐的解决方案操作
  ▼
Step 5: 验证修复效果
      重新运行，确认错误是否消除
```

## 预防性建议

1. **运行 `asset_exists_check.py`**：在开始任何操作前检查资产完整性
2. **运行 `path_auto_fix.py`**：自动修复路径配置问题
3. **使用 `safe_retry.py`**：对关键操作使用安全重试封装，提高运行稳定性
4. **日志记录**：记录详细运行日志，方便定位问题
5. **分段测试**：不要一次性执行全部流程，逐个子流程测试
