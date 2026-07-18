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
    # wycx_lines
    rgv.init_value("wycx_lines", None)
    wycx_lines = rgv.get_value("wycx_lines")
    # wy_win
    rgv.init_value("wy_win", None)
    wy_win = rgv.get_value("wy_win")
    # bankkey
    rgv.init_value("bankkey", r"123456")
    bankkey = rgv.get_value("bankkey")
    # tsk_value
    rgv.init_value("tsk_value", r"")
    tsk_value = rgv.get_value("tsk_value")
    # wy_excel
    rgv.init_value("wy_excel", None)
    wy_excel = rgv.get_value("wy_excel")
    # wy_excel_path
    rgv.init_value("wy_excel_path", r"C:\\RPADATA\\收款查询业务数据表.xls")
    wy_excel_path = rgv.get_value("wy_excel_path")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # u
    rgv.init_value("u", None)
    u = rgv.get_value("u")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # account_web
    rgv.init_value("account_web", None)
    account_web = rgv.get_value("account_web")
    # wycx_sheet
    rgv.init_value("wycx_sheet", None)
    wycx_sheet = rgv.get_value("wycx_sheet")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_rxjin5pt')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人已完成收款查询，自动退出工行网银仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_rxjin5pt', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_rxjin5pt')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_rxjin5pt', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人已完成收款查询，自动退出工行网银仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 获取已打开网页
    try:
        Debug_Block_Start('canvas-node-_wm6j04vo')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        account_web = visual.browser.catch("chrome", r"https://fz.chinaive.com/wsyh/account_manage/", mode="url", pattern="contain", timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wm6j04vo', error, False)
    finally: 
        rgv.set_values({"account_web": account_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wm6j04vo')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取已打开网页', 'id':'canvas-node-_wm6j04vo', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中，根据 URL 查找打开的网页 ，将查找到的浏览器对象赋值给 account_web''', 'success':node_success_flag, 'variables':{"account_web": str(account_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_i44yjgcl')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="退出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=account_web, timeout=20)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_i44yjgcl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_i44yjgcl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_i44yjgcl', 'time':block_start_time, 'error': error, 'description':r'''在 account_web 网页中，鼠标 左键单击 退出''', 'success':node_success_flag, 'variables':{"account_web": str(account_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_rw64y01p')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"^{w}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_rw64y01p', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_rw64y01p')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_rw64y01p', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "^{w}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_l346w2ta')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_3hmis2g3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_ncmch1lc')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        wy_win = visual.window.catch(os.path.basename(wy_excel_path).split('.')[0], mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_ncmch1lc', error, False)
                    finally: 
                        rgv.set_values({"wy_win": wy_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_ncmch1lc')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_ncmch1lc', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(wy_excel_path).split('.')[0] 查找打开的窗口标题，将查找到的窗口对象赋值给 wy_win''', 'success':node_success_flag, 'variables':{"wy_win": str(wy_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_eqqj186d')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        wy_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_eqqj186d', error, False)
                    finally: 
                        rgv.set_values({"wy_win": wy_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_eqqj186d')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_eqqj186d', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 wy_win''', 'success':node_success_flag, 'variables':{"wy_win": str(wy_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_3hmis2g3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_3hmis2g3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_3hmis2g3', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_uca59fp3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if wy_win is not None: wy_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_uca59fp3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_uca59fp3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_uca59fp3', 'time':block_start_time, 'error': error, 'description':r'''激活 wy_win 窗口''', 'success':node_success_flag, 'variables':{"wy_win": str(wy_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_j6wfksp8')
                node_success_flag = True
                sleep(0.5)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_j6wfksp8', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_j6wfksp8')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_j6wfksp8', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 记录日志
            try:
                Debug_Block_Start('canvas-node-_l346w2te')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger.info(r''' ''')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_l346w2te', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_l346w2te')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_l346w2te', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l346w2ta', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l346w2ta')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_l346w2ta', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("data", data)
    rgv.set_value("wycx_lines", wycx_lines)
    rgv.set_value("wy_win", wy_win)
    rgv.set_value("bankkey", bankkey)
    rgv.set_value("tsk_value", tsk_value)
    rgv.set_value("wy_excel", wy_excel)
    rgv.set_value("wy_excel_path", wy_excel_path)
    rgv.set_value("username", username)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("u", u)
    rgv.set_value("v_time", v_time)
    rgv.set_value("save_as_dialog", save_as_dialog)
    rgv.set_value("account_web", account_web)
    rgv.set_value("wycx_sheet", wycx_sheet)
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("password", password)
    rgv.set_value("cookies", cookies)