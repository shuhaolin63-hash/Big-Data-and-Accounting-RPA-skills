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
        Debug_Block_Start('canvas-node-_7sg1d1ow')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在登录工行网银仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_7sg1d1ow', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_7sg1d1ow')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_7sg1d1ow', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在登录工行网银仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 打开新网页
    try:
        Debug_Block_Start('canvas-node-_0vlc0usu')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        bank_web = visual.browser.create("chrome", 'https://fz.chinaive.com/wsyh/?username='+username,  wait=True, visible=True, timeout=100)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_0vlc0usu', error, False)
    finally: 
        rgv.set_values({"bank_web": bank_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_0vlc0usu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_0vlc0usu', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问'https://fz.chinaive.com/wsyh/?username='+username，将浏览器对象赋值给 bank_web''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 激活网页
    try:
        Debug_Block_Start('canvas-node-_wn5298iu')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None:
            visual.browser.activate(bank_web)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wn5298iu', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wn5298iu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_wn5298iu', 'time':block_start_time, 'error': error, 'description':r'''将 bank_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_h4v4o9mp')
        node_success_flag = True
        sleep(2)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"!{SPACE}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_h4v4o9mp', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_h4v4o9mp')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_h4v4o9mp', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{SPACE}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_l7i9598p')
        node_success_flag = True
        sleep(0.5)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"x")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l7i9598p', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l7i9598p')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_l7i9598p', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "x"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_t1hlurpq')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="企业网上银行登录", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_t1hlurpq', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_t1hlurpq')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_t1hlurpq', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 企业网上银行登录''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_g2xpkq0c')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="U盾登录", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_g2xpkq0c', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_g2xpkq0c')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_g2xpkq0c', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 U盾登录''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_00tbzfev')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="U盾密码输入框", value=bankkey, elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_00tbzfev', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_00tbzfev')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_00tbzfev', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 U盾密码输入框 内填写 bankkey''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web),"bankkey": str(bankkey)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_t4srzens')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="确定", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_t4srzens', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_t4srzens')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_t4srzens', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 确定''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_kwbzhbpj')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbzhbpj', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbzhbpj')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_kwbzhbpj', 'time':block_start_time, 'error': error, 'description':r'''''', 'success':node_success_flag, 'variables':{}})
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