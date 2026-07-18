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
    # tsk_value
    rgv.init_value("tsk_value", r"")
    tsk_value = rgv.get_value("tsk_value")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # fp_excel_path
    rgv.init_value("fp_excel_path", r"C:/RPADATA/发票查验业务数据表.xls")
    fp_excel_path = rgv.get_value("fp_excel_path")
    # fp_excel
    rgv.init_value("fp_excel", None)
    fp_excel = rgv.get_value("fp_excel")
    # Vcode
    rgv.init_value("Vcode", r"flase")
    Vcode = rgv.get_value("Vcode")
    # web_result
    rgv.init_value("web_result", r"")
    web_result = rgv.get_value("web_result")
    # username
    rgv.init_value("username", r" ")
    username = rgv.get_value("username")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # v_date
    rgv.init_value("v_date", r"")
    v_date = rgv.get_value("v_date")
    # fpcy_excel_path
    rgv.init_value("fpcy_excel_path", r"")
    fpcy_excel_path = rgv.get_value("fpcy_excel_path")
    # fpcy_cyjg_excel
    rgv.init_value("fpcy_cyjg_excel", None)
    fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
    # lines_number
    rgv.init_value("lines_number", 1)
    lines_number = rgv.get_value("lines_number")
    # fpcyxx_sheet_name
    rgv.init_value("fpcyxx_sheet_name", r"发票查验信息")
    fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
    # check_html
    rgv.init_value("check_html", r"")
    check_html = rgv.get_value("check_html")
    # fpcyjg_sheet_name
    rgv.init_value("fpcyjg_sheet_name", r"发票查验结果")
    fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
    # fpcy_cyjg_sheet
    rgv.init_value("fpcy_cyjg_sheet", None)
    fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # invoice_web
    rgv.init_value("invoice_web", None)
    invoice_web = rgv.get_value("invoice_web")
    # fpcy_sheet
    rgv.init_value("fpcy_sheet", None)
    fpcy_sheet = rgv.get_value("fpcy_sheet")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # fpcy_cyxx_sheet
    rgv.init_value("fpcy_cyxx_sheet", None)
    fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
    # fpcy_lines
    rgv.init_value("fpcy_lines", None)
    fpcy_lines = rgv.get_value("fpcy_lines")
    # verification_code
    rgv.init_value("verification_code", r"")
    verification_code = rgv.get_value("verification_code")
    # result_path
    rgv.init_value("result_path", r"")
    result_path = rgv.get_value("result_path")
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
        Debug_Block_Start('canvas-node-_hhh732vb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_hhh732vb', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_hhh732vb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_hhh732vb', 'time':block_start_time, 'error': error, 'description':r'''关闭已出现的字幕''', 'success':node_success_flag, 'variables':{}})
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_kxivoqqb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Assess.start('auto_end')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kxivoqqb', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kxivoqqb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kxivoqqb', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)