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
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # fpzbkj_excel
    rgv.init_value("fpzbkj_excel", None)
    fpzbkj_excel = rgv.get_value("fpzbkj_excel")
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
    # fpzbkj_win
    rgv.init_value("fpzbkj_win", None)
    fpzbkj_win = rgv.get_value("fpzbkj_win")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # fpzbkj_excel_path
    rgv.init_value("fpzbkj_excel_path", r"C:\RPADATA\发票逐笔开具业务数据表.xls")
    fpzbkj_excel_path = rgv.get_value("fpzbkj_excel_path")
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_logsxyxm')
        node_success_flag = True
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxm', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxm')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_logsxyxn')
        node_success_flag = True
        Assess.start('auto_end')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxn', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxn')