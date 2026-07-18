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
        Debug_Block_Start('canvas-node-_w4po2odi')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_w4po2odi', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_w4po2odi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_w4po2odi', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始运行，请输入实践平台账号及密码！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_pbfhp6f6')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_pbfhp6f6', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_pbfhp6f6')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_pbfhp6f6', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_wmmtky2w')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("username", username)
        username = username
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wmmtky2w', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wmmtky2w')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_wmmtky2w', 'time':block_start_time, 'error': error, 'description':r'''设置变量 username 的值为 username''', 'success':node_success_flag, 'variables':{"username": str(username)}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_kxju1gd8')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("password", password)
        password = password
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxju1gd8', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxju1gd8')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_kxju1gd8', 'time':block_start_time, 'error': error, 'description':r'''设置变量 password 的值为 password''', 'success':node_success_flag, 'variables':{"password": str(password)}})
        if (error is not None):
            sys.exit(1)
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kxju1gd9')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxju1gd9', error, False)
    finally: 
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_kxju1gd9')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kxju1gd9', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在自动识别测评任务！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_kxju1gda')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        path = Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxju1gda', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxju1gda')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kxju1gda', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_l2yjahlu')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("wy_excel_path", path or wy_excel_path)
        wy_excel_path = path or wy_excel_path
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l2yjahlu', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l2yjahlu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_l2yjahlu', 'time':block_start_time, 'error': error, 'description':r'''设置变量 wy_excel_path 的值为 path or wy_excel_path''', 'success':node_success_flag, 'variables':{"wy_excel_path": str(wy_excel_path)}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_kxju1gdb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxju1gdb', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxju1gdb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_kxju1gdb', 'time':block_start_time, 'error': error, 'description':r'''''', 'success':node_success_flag, 'variables':{}})