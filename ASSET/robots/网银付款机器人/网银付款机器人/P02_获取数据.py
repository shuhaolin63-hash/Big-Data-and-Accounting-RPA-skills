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
    # 获取Excel行的值
    try:
        Debug_Block_Start('canvas-node-_0qg3b9s1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if wyfk_sheet is not None:
            data = wyfk_sheet.read(str(i),only_visible = True,max = 1000)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_0qg3b9s1', error, False)
    finally: 
        rgv.set_values({"data": data})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_0qg3b9s1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel行的值', 'id':'canvas-node-_0qg3b9s1', 'time':block_start_time, 'error': error, 'description':r'''获取 wyfk_sheet Sheet页的 i 行的值，并将结果赋值给 data''', 'success':node_success_flag, 'variables':{"i": str(i),"data": str(data),"wyfk_sheet": str(wyfk_sheet)}})
        if (error is not None):
            sys.exit(1)