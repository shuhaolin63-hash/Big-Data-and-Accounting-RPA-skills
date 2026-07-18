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
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # fpkj_excel
    rgv.init_value("fpkj_excel", None)
    fpkj_excel = rgv.get_value("fpkj_excel")
    # fpkj_sheet
    rgv.init_value("fpkj_sheet", None)
    fpkj_sheet = rgv.get_value("fpkj_sheet")
    # swj_web
    rgv.init_value("swj_web", None)
    swj_web = rgv.get_value("swj_web")
    # lines
    rgv.init_value("lines", None)
    lines = rgv.get_value("lines")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # kp_web
    rgv.init_value("kp_web", None)
    kp_web = rgv.get_value("kp_web")
    # lzfp_web
    rgv.init_value("lzfp_web", None)
    lzfp_web = rgv.get_value("lzfp_web")
    # fpkj_win
    rgv.init_value("fpkj_win", None)
    fpkj_win = rgv.get_value("fpkj_win")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # fpkj_excel_path
    rgv.init_value("fpkj_excel_path", r"C:\RPADATA\发票开具业务(数电票)数据表.xls")
    fpkj_excel_path = rgv.get_value("fpkj_excel_path")
    # 申明自动创建变量
    dltx_web_element = None
    key = r"123456"
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_logloagz')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在登录电子税务局仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloagz', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloagz')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_logloagz', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在登录电子税务局仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 打开新网页
    try:
        Debug_Block_Start('canvas-node-_lofgjgaq')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        swj_web = visual.browser.create("chrome", "https://fz.chinaive.com/dzswj/?username="+username,  wait=True, visible=True, timeout=100)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgaq', error, False)
    finally: 
        rgv.set_values({"swj_web": swj_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgaq')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_lofgjgaq', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问"https://fz.chinaive.com/dzswj/?username="+username，将浏览器对象赋值给 swj_web''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 等待网页元素出现（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgar')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dltx_web_element = visual.element.wait_appear(element="登录头像", elem_type="Chrome", index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgar', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgar')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'等待网页元素出现（网页）', 'id':'canvas-node-_lofgjgar', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，等待 登录头像 出现，等待 10 秒，将结果赋值给 dltx_web_element''', 'success':node_success_flag, 'variables':{"dltx_web_element": str(dltx_web_element),"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_lofgjgas')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"!{space}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgas', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgas')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lofgjgas', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{space}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_lofgjgat')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"x")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgat', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgat')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lofgjgat', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "x"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgau')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="登录头像", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgau', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgau')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgau', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，鼠标 左键单击 登录头像''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgav')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if swj_web is not None: 
            pyperclip.copy(r"rcjc")                                                                         
            visual.element.input_hotkey("账号输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgav', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lofgjgav')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lofgjgav', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，通过剪贴方式在 账号输入框 内填写 "rcjc"''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgaw')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if swj_web is not None: 
            visual.element.input(element="密码输入框", value=key, elem_type="Chrome", index=1, window=swj_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgaw', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgaw')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_lofgjgaw', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页 中，在 密码输入框 内填写 key''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web),"key": str(key)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgax')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="登录按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgax', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgax')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgax', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，鼠标 左键单击 登录按钮''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_logloah0')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloah0', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloah0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_logloah0', 'time':block_start_time, 'error': error, 'description':r'''关闭已出现的字幕''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("fpkj_excel", fpkj_excel)
    rgv.set_value("fpkj_sheet", fpkj_sheet)
    rgv.set_value("swj_web", swj_web)
    rgv.set_value("lines", lines)
    rgv.set_value("i", i)
    rgv.set_value("data", data)
    rgv.set_value("kp_web", kp_web)
    rgv.set_value("lzfp_web", lzfp_web)
    rgv.set_value("fpkj_win", fpkj_win)
    rgv.set_value("username", username)
    rgv.set_value("password", password)
    rgv.set_value("fpkj_excel_path", fpkj_excel_path)