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
import Assess


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
        Debug_Block_Start('canvas-node-_cuq14ibm')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_cuq14ibm', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_cuq14ibm')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_cuq14ibm', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始运行，请输入实践平台账号及密码！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_x7cvqgzc')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_x7cvqgzc', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_x7cvqgzc')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_x7cvqgzc', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_snv33p6l')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("username", username)
        username = username
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_snv33p6l', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_snv33p6l')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_snv33p6l', 'time':block_start_time, 'error': error, 'description':r'''设置变量 username 的值为 username''', 'success':node_success_flag, 'variables':{"username": str(username)}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_kxjv4rxl')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("password", password)
        password = password
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjv4rxl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjv4rxl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_kxjv4rxl', 'time':block_start_time, 'error': error, 'description':r'''设置变量 password 的值为 password''', 'success':node_success_flag, 'variables':{"password": str(password)}})
        if (error is not None):
            sys.exit(1)
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kxjv6eaj')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjv6eaj', error, False)
    finally: 
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_kxjv6eaj')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kxjv6eaj', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在自动识别测评任务！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_kxjv6eak')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        path = Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjv6eak', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjv6eak')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kxjv6eak', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_l2yjjixu')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("wy_excel_path", path or wy_excel_path)
        wy_excel_path = path or wy_excel_path
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l2yjjixu', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l2yjjixu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_l2yjjixu', 'time':block_start_time, 'error': error, 'description':r'''设置变量 wy_excel_path 的值为 path or wy_excel_path''', 'success':node_success_flag, 'variables':{"wy_excel_path": str(wy_excel_path)}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_kxjv6eal')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjv6eal', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjv6eal')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_kxjv6eal', 'time':block_start_time, 'error': error, 'description':r'''''', 'success':node_success_flag, 'variables':{}})