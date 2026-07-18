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


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明全局变量
    # wyfk_sheet
    rgv.init_value("wyfk_sheet", None)
    wyfk_sheet = rgv.get_value("wyfk_sheet")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # 申明自动创建变量
    v_excel_obj_1 = None
    v_file_path_1 = r""
    wyfk_excel = None
    v_sheet_obj_1 = None
    bankkey = r"123456"
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mpy3pb9o')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_mpy3pbax')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wyfk_excel = rpa.app.microsoft.excel.open(r"C:\RPADATA\网银对公付款业务数据表.xls", visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbax', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbax')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_mpy3pbax', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 wyfk_excel''', 'success':node_success_flag, 'variables':{"wyfk_excel": str(wyfk_excel),"v_file_path_1": str(v_file_path_1)}})
                if (error is not None):
                    sys.exit(1)
            # 激活Sheet页
            try:
                Debug_Block_Start('canvas-node-_mpy3pbay')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if wyfk_excel is not None:
                    sheet = wyfk_excel.get_sheet(r"网银对公付款")
                    if sheet is not None:
                        sheet.activate()
                        wyfk_sheet= wyfk_excel.get_sheet()
                else:
                    wyfk_sheet = None
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbay', error, False)
            finally: 
                rgv.set_values({"wyfk_sheet": wyfk_sheet})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbay')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_mpy3pbay', 'time':block_start_time, 'error': error, 'description':r'''在 wyfk_excel Excel对象中激活Sheet页 "网银对公付款"，将对应的Sheet页对象赋值给 wyfk_sheet''', 'success':node_success_flag, 'variables':{"wyfk_sheet": str(wyfk_sheet),"wyfk_excel": str(wyfk_excel)}})
                if (error is not None):
                    sys.exit(1)
            # 打开新网页
            try:
                Debug_Block_Start('canvas-node-_mpy3pbaz')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                bank_web = visual.browser.create("chrome", r"https://fz.chinaive.com/wsyh/?username=zhanhunliren",  wait=True, visible=True, timeout=100)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbaz', error, False)
            finally: 
                rgv.set_values({"bank_web": bank_web})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbaz')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_mpy3pbaz', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问"https://fz.chinaive.com/wsyh/?username=zhanhunliren"，将浏览器对象赋值给 bank_web''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb0')
                node_success_flag = True
                sleep(2)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{space}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb0', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb0')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mpy3pbb0', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{space}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mpyrkxgl')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"x")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpyrkxgl', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpyrkxgl')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mpyrkxgl', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "x"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb2')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="企业网上银行登录", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbb2', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 企业网上银行登录''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="U盾登录", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbb3', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 U盾登录''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="U盾密码输入框", value=bankkey, elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb4', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mpy3pbb4', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 U盾密码输入框 内填写 bankkey''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web),"bankkey": str(bankkey)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb5')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="确定", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb5', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb5')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbb5', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 确定''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
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
        Debug_Block_Error('canvas-node-_mpy3pb9o', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pb9o')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_mpy3pb9o', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)