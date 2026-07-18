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
import Select_file


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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kwbwkd5y')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在打开数据文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbwkd5y', error, False)
    finally: 
        if node_success_flag == True:
            sleep(2)
            Debug_Block_Success('canvas-node-_kwbwkd5y')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kwbwkd5y', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开数据文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_3dlxumbg')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_cb54n1ob')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fp_excel = rpa.app.microsoft.excel.open(fp_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_cb54n1ob', error, False)
            finally: 
                rgv.set_values({"fp_excel": fp_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_cb54n1ob')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_cb54n1ob', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fp_excel''', 'success':node_success_flag, 'variables':{"fp_excel": str(fp_excel),"fp_excel_path": str(fp_excel_path),"": str()}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_a850w57v')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"未找到数据文件，请手动选择！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_a850w57v', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_a850w57v')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_a850w57v', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "未找到数据文件，请手动选择！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 调用自定义脚本
            try:
                Debug_Block_Start('canvas-node-_8zl5wbpm')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 弹出文件选择窗口
                fp_excel_path=Select_file.start()
                
                if fp_excel_path == '':
                     sys.exit()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_8zl5wbpm', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_8zl5wbpm')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_8zl5wbpm', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_ngq3030s')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fp_excel = rpa.app.microsoft.excel.open(fp_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_ngq3030s', error, False)
            finally: 
                rgv.set_values({"fp_excel": fp_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_ngq3030s')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_ngq3030s', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fp_excel''', 'success':node_success_flag, 'variables':{"fp_excel": str(fp_excel),"": str(),"fp_excel_path": str(fp_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_6q80m0me')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"机器人开始进行发票查验……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_6q80m0me', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_6q80m0me')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_6q80m0me', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始进行发票查验……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_3dlxumbg', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_3dlxumbg')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_3dlxumbg', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_uzrm2u31')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fp_excel is not None:
            sheet = fp_excel.get_sheet(r"发票查验")
            if sheet is not None:
                sheet.activate()
                fpcy_sheet= fp_excel.get_sheet()
        else:
            fpcy_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_uzrm2u31', error, False)
    finally: 
        rgv.set_values({"fpcy_sheet": fpcy_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_uzrm2u31')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_uzrm2u31', 'time':block_start_time, 'error': error, 'description':r'''在 fp_excel Excel对象中激活Sheet页 "发票查验"，将对应的Sheet页对象赋值给 fpcy_sheet''', 'success':node_success_flag, 'variables':{"fpcy_sheet": str(fpcy_sheet),"fp_excel": str(fp_excel)}})
        if (error is not None):
            sys.exit(1)
    # 获取Excel的行数
    try:
        Debug_Block_Start('canvas-node-_wli3flgn')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if(fpcy_sheet is not None):
            fpcy_lines = fpcy_sheet.row_count()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_wli3flgn', error, False)
    finally: 
        rgv.set_values({"fpcy_lines": fpcy_lines})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_wli3flgn')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel的行数', 'id':'canvas-node-_wli3flgn', 'time':block_start_time, 'error': error, 'description':r'''获取 fpcy_sheet Sheet页的行数''', 'success':node_success_flag, 'variables':{"fpcy_lines": str(fpcy_lines),"fpcy_sheet": str(fpcy_sheet)}})
        if (error is not None):
            sys.exit(1)