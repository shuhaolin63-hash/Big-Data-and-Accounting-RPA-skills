# -*- coding: utf-8 -*-
import os
import sys
import shutil
import visual
import fnmatch
import datetime
import pyperclip
import subprocess
import rpa4 as rpa
import rpa as rpa_v33
from rpa.core import *
from rpa.utils import *
import visual_global_variable as rgv
import time
import START
import END


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明自动创建变量
    invoice_web = None
    fpcy_excel = None
    v_file_path_1 = r""
    fpcy_sheet = None
    data = None
    fpcy_win = None
    verification_value = r""
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mpdfjg52')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        START.start()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpdfjg52', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpdfjg52')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpdfjg52', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mpdfjg54')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 打开新网页
            try:
                Debug_Block_Start('canvas-node-_mp3i1cgy')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                invoice_web = visual.browser.create("chrome", r"https://fz.chinaive.com/fpcy/?username=zhanhunliren",  wait=True, visible=True, timeout=100)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1cgy', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1cgy')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_mp3i1cgy', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问"https://fz.chinaive.com/fpcy/?username=zhanhunliren"，将浏览器对象赋值给 invoice_web''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mp3i1cgz')
                node_success_flag = True
                sleep(2)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{space}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1cgz', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_mp3i1cgz')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mp3i1cgz', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{space}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch0')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fpcy_excel = rpa.app.microsoft.excel.open(r"C:\Users\Administrator\Desktop\发票单笔查验业务数据表.xls", visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch0', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch0')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_mp3i1ch0', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fpcy_excel''', 'success':node_success_flag, 'variables':{"fpcy_excel": str(fpcy_excel),"v_file_path_1": str(v_file_path_1)}})
                if (error is not None):
                    sys.exit(1)
            # 激活Sheet页
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch1')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fpcy_excel is not None:
                    sheet = fpcy_excel.get_sheet(r"发票单笔查验")
                    if sheet is not None:
                        sheet.activate()
                        fpcy_sheet= fpcy_excel.get_sheet()
                else:
                    fpcy_sheet = None
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch1', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch1')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_mp3i1ch1', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_excel Excel对象中激活Sheet页 "发票单笔查验"，将对应的Sheet页对象赋值给 fpcy_sheet''', 'success':node_success_flag, 'variables':{"fpcy_sheet": str(fpcy_sheet),"fpcy_excel": str(fpcy_excel)}})
                if (error is not None):
                    sys.exit(1)
            # 获取Excel行的值
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch2')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fpcy_sheet is not None:
                    data = fpcy_sheet.read(str(2),only_visible = True,max = 1000)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel行的值', 'id':'canvas-node-_mp3i1ch2', 'time':block_start_time, 'error': error, 'description':r'''获取 fpcy_sheet Sheet页的 2 行的值，并将结果赋值给 data''', 'success':node_success_flag, 'variables':{"data": str(data),"fpcy_sheet": str(fpcy_sheet)}})
                if (error is not None):
                    sys.exit(1)
            # 获取窗口
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fpcy_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_mp3i1ch3', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 fpcy_win''', 'success':node_success_flag, 'variables':{"fpcy_win": str(fpcy_win)}})
                if (error is not None):
                    sys.exit(1)
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fpcy_win is not None: fpcy_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch4', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_mp3i1ch4', 'time':block_start_time, 'error': error, 'description':r'''激活 fpcy_win 窗口''', 'success':node_success_flag, 'variables':{"fpcy_win": str(fpcy_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch5')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch5', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(2)
                    Debug_Block_Success('canvas-node-_mp3i1ch5')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mp3i1ch5', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch7')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="发票代码输入框1", value=data[2], elem_type="Chrome", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch7', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch7')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mp3i1ch7', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 发票代码输入框1 内填写 data[2]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch6')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="发票号码输入框", value=data[3], elem_type="Chrome", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch6', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch6')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mp3i1ch6', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 发票号码输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch8')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="开票日期输入框", value=data[4], elem_type="Chrome", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch8', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch8')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mp3i1ch8', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 开票日期输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1ch9')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="校验码输入框", value=data[5][-6:], elem_type="Chrome", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1ch9', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1ch9')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mp3i1ch9', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 校验码输入框 内填写 data[5][-6:]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 弹出输入框
            try:
                Debug_Block_Start('canvas-node-_mp3i1cha')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                verification_value = rpa.system.dialog.inputbox(r"验证码", r"手动输入验证码") 
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1cha', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1cha')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出输入框', 'id':'canvas-node-_mp3i1cha', 'time':block_start_time, 'error': error, 'description':r'''弹出输入框，将用户输入内容赋值给 verification_value''', 'success':node_success_flag, 'variables':{"verification_value": str(verification_value)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1chb')
                node_success_flag = True
                sleep(0.5)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    pyperclip.copy(verification_value)                                                                         
                    visual.element.input_hotkey("验证码输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=invoice_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1chb', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(1)
                    Debug_Block_Success('canvas-node-_mp3i1chb')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_mp3i1chb', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，通过剪贴方式在 验证码输入框 内填写 verification_value''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web),"verification_value": str(verification_value)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mp3i1chc')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="查验", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=invoice_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mp3i1chc', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mp3i1chc')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mp3i1chc', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，鼠标 左键单击 查验''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpdfjg54', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpdfjg54')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_mpdfjg54', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mpdfjg53')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        END.start()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpdfjg53', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpdfjg53')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpdfjg53', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)