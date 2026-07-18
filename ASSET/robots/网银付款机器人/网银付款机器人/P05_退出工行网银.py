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
from rpa.sdk import logger


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明全局变量
    # data
    rgv.init_value("data", None)
    data = rgv.get_value("data")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # bankkey
    rgv.init_value("bankkey", r"123456")
    bankkey = rgv.get_value("bankkey")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # wy_excel
    rgv.init_value("wy_excel", None)
    wy_excel = rgv.get_value("wy_excel")
    # wy_excel_path
    rgv.init_value("wy_excel_path", r"C:\\RPADATA\网银付款业务数据表.xls")
    wy_excel_path = rgv.get_value("wy_excel_path")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # username
    rgv.init_value("username", r" ")
    username = rgv.get_value("username")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # wyfk_sheet
    rgv.init_value("wyfk_sheet", None)
    wyfk_sheet = rgv.get_value("wyfk_sheet")
    # wyfk_lines
    rgv.init_value("wyfk_lines", None)
    wyfk_lines = rgv.get_value("wyfk_lines")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # Running_state
    rgv.init_value("Running_state", r"")
    Running_state = rgv.get_value("Running_state")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_vg03b12m')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人已完成网银付款，自动退出工行网银仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_vg03b12m', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_vg03b12m')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_vg03b12m', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人已完成网银付款，自动退出工行网银仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 获取已打开网页
    try:
        Debug_Block_Start('canvas-node-_wdwjf67j')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        bank_web = visual.browser.catch("chrome", r"中国工商银行", mode="title", pattern="contain", timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wdwjf67j', error, False)
    finally: 
        rgv.set_values({"bank_web": bank_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wdwjf67j')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取已打开网页', 'id':'canvas-node-_wdwjf67j', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中，根据 标题 查找打开的网页 ，将查找到的浏览器对象赋值给 bank_web''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_5la6tenu')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="退出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=20)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_5la6tenu', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_5la6tenu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_5la6tenu', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 退出''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_pedmf49g')
        node_success_flag = True
        sleep(2)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"^{w}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_pedmf49g', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_pedmf49g')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_pedmf49g', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "^{w}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_l347ge9q')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_7qup0zht')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_bqlfk34i')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(os.path.basename(wy_excel_path).split('.')[0], mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_bqlfk34i', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_bqlfk34i')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_bqlfk34i', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(wy_excel_path).split('.')[0] 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_i5x9yzct')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_i5x9yzct', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_i5x9yzct')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_i5x9yzct', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_7qup0zht', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_7qup0zht')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_7qup0zht', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_2tga1z2w')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fp_win is not None: fp_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_2tga1z2w', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_2tga1z2w')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_2tga1z2w', 'time':block_start_time, 'error': error, 'description':r'''激活 fp_win 窗口''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_4qxjzn3x')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_4qxjzn3x', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_4qxjzn3x')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_4qxjzn3x', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 记录日志
            try:
                Debug_Block_Start('canvas-node-_l347ge9u')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger.info(r''' ''')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_l347ge9u', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_l347ge9u')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_l347ge9u', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l347ge9q', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l347ge9q')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_l347ge9q', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})