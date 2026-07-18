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
    # fprz_lines
    rgv.init_value("fprz_lines", None)
    fprz_lines = rgv.get_value("fprz_lines")
    # certification_key
    rgv.init_value("certification_key", r"8888888888888888")
    certification_key = rgv.get_value("certification_key")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # fp_excel
    rgv.init_value("fp_excel", None)
    fp_excel = rgv.get_value("fp_excel")
    # fp_excel_path
    rgv.init_value("fp_excel_path", r"C:\\RPADATA\\发票认证业务数据表.xls")
    fp_excel_path = rgv.get_value("fp_excel_path")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # certification_web
    rgv.init_value("certification_web", None)
    certification_web = rgv.get_value("certification_web")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # fprz_sheet
    rgv.init_value("fprz_sheet", None)
    fprz_sheet = rgv.get_value("fprz_sheet")
    # result_path
    rgv.init_value("result_path", r"")
    result_path = rgv.get_value("result_path")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_qc0q52xe')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_qc0q52xe', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_qc0q52xe')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_qc0q52xe', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始运行，请输入实践平台账号及密码！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_uofx33w1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_uofx33w1', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_uofx33w1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_uofx33w1', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_wrng2q6e')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("username", username)
        username = username
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wrng2q6e', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wrng2q6e')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_wrng2q6e', 'time':block_start_time, 'error': error, 'description':r'''设置变量 username 的值为 username''', 'success':node_success_flag, 'variables':{"username": str(username)}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_kxju05u4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("password", password)
        password = password
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxju05u4', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxju05u4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_kxju05u4', 'time':block_start_time, 'error': error, 'description':r'''设置变量 password 的值为 password''', 'success':node_success_flag, 'variables':{"password": str(password)}})
        if (error is not None):
            sys.exit(1)
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kxjsnzcs')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjsnzcs', error, False)
    finally: 
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_kxjsnzcs')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kxjsnzcs', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在自动识别测评任务！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_kxjsnzct')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        path = Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjsnzct', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjsnzct')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kxjsnzct', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_l2ygxh2z')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("fp_excel_path", path or fp_excel_path)
        fp_excel_path = path or fp_excel_path
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l2ygxh2z', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l2ygxh2z')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_l2ygxh2z', 'time':block_start_time, 'error': error, 'description':r'''设置变量 fp_excel_path 的值为 path or fp_excel_path''', 'success':node_success_flag, 'variables':{"fp_excel_path": str(fp_excel_path)}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_kxjsnzcu')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjsnzcu', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjsnzcu')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_kxjsnzcu', 'time':block_start_time, 'error': error, 'description':r'''''', 'success':node_success_flag, 'variables':{}})