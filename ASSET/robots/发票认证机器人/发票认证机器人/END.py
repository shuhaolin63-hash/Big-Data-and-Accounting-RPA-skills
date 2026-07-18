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
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_svfska62')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_svfska62', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_svfska62')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_svfska62', 'time':block_start_time, 'error': error, 'description':r'''关闭已出现的字幕''', 'success':node_success_flag, 'variables':{}})
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_kxjsnzcv')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Assess.start('auto_end')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxjsnzcv', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxjsnzcv')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kxjsnzcv', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)