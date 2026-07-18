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
import START
import P00_打开数据表格
import P01_发票查验
import END


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
    # 申明自动创建变量
    Running_state = r""
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kvm6yo2c')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        START.start()
        tsk_value = rgv.get_value("tsk_value")
        v_time = rgv.get_value("v_time")
        fp_excel_path = rgv.get_value("fp_excel_path")
        fp_excel = rgv.get_value("fp_excel")
        Vcode = rgv.get_value("Vcode")
        web_result = rgv.get_value("web_result")
        username = rgv.get_value("username")
        fp_win = rgv.get_value("fp_win")
        v_date = rgv.get_value("v_date")
        fpcy_excel_path = rgv.get_value("fpcy_excel_path")
        fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
        lines_number = rgv.get_value("lines_number")
        fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
        check_html = rgv.get_value("check_html")
        fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
        fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
        size_changer = rgv.get_value("size_changer")
        invoice_web = rgv.get_value("invoice_web")
        fpcy_sheet = rgv.get_value("fpcy_sheet")
        data = rgv.get_value("data")
        fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
        fpcy_lines = rgv.get_value("fpcy_lines")
        verification_code = rgv.get_value("verification_code")
        result_path = rgv.get_value("result_path")
        i = rgv.get_value("i")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvm6yo2c', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kvm6yo2c')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvm6yo2c', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_kwbwkd66')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kvm6yo2d')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P00_打开数据表格 子流程
                P00_打开数据表格.start()
                tsk_value = rgv.get_value("tsk_value")
                v_time = rgv.get_value("v_time")
                fp_excel_path = rgv.get_value("fp_excel_path")
                fp_excel = rgv.get_value("fp_excel")
                Vcode = rgv.get_value("Vcode")
                web_result = rgv.get_value("web_result")
                username = rgv.get_value("username")
                fp_win = rgv.get_value("fp_win")
                v_date = rgv.get_value("v_date")
                fpcy_excel_path = rgv.get_value("fpcy_excel_path")
                fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
                lines_number = rgv.get_value("lines_number")
                fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
                check_html = rgv.get_value("check_html")
                fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
                fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
                size_changer = rgv.get_value("size_changer")
                invoice_web = rgv.get_value("invoice_web")
                fpcy_sheet = rgv.get_value("fpcy_sheet")
                data = rgv.get_value("data")
                fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
                fpcy_lines = rgv.get_value("fpcy_lines")
                verification_code = rgv.get_value("verification_code")
                result_path = rgv.get_value("result_path")
                i = rgv.get_value("i")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvm6yo2d', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvm6yo2d')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvm6yo2d', 'time':block_start_time, 'error': error, 'description':r'''调用 P00_打开数据表格 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kwbwkd64')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P01_发票查验 子流程
                P01_发票查验.start()
                tsk_value = rgv.get_value("tsk_value")
                v_time = rgv.get_value("v_time")
                fp_excel_path = rgv.get_value("fp_excel_path")
                fp_excel = rgv.get_value("fp_excel")
                Vcode = rgv.get_value("Vcode")
                web_result = rgv.get_value("web_result")
                username = rgv.get_value("username")
                fp_win = rgv.get_value("fp_win")
                v_date = rgv.get_value("v_date")
                fpcy_excel_path = rgv.get_value("fpcy_excel_path")
                fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
                lines_number = rgv.get_value("lines_number")
                fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
                check_html = rgv.get_value("check_html")
                fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
                fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
                size_changer = rgv.get_value("size_changer")
                invoice_web = rgv.get_value("invoice_web")
                fpcy_sheet = rgv.get_value("fpcy_sheet")
                data = rgv.get_value("data")
                fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
                fpcy_lines = rgv.get_value("fpcy_lines")
                verification_code = rgv.get_value("verification_code")
                result_path = rgv.get_value("result_path")
                i = rgv.get_value("i")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbwkd64', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbwkd64')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbwkd64', 'time':block_start_time, 'error': error, 'description':r'''调用 P01_发票查验 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_tbzo1x28')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"发票查验机器人运行成功，感谢使用！", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_tbzo1x28', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_tbzo1x28')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_tbzo1x28', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "发票查验机器人运行成功，感谢使用！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 弹出提示框
            try:
                Debug_Block_Start('canvas-node-_kwbwkd6a')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                Running_state = rpa.system.dialog.msgbox('信息', r"机器人运行异常，请查看运行日志，排除故障后再运行！", disappear_time=5)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbwkd6a', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbwkd6a')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出提示框', 'id':'canvas-node-_kwbwkd6a', 'time':block_start_time, 'error': error, 'description':r'''弹出提示框''', 'success':node_success_flag, 'variables':{"Running_state": str(Running_state)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbwkd66', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbwkd66')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_kwbwkd66', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kwbwkd65')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        END.start()
        tsk_value = rgv.get_value("tsk_value")
        v_time = rgv.get_value("v_time")
        fp_excel_path = rgv.get_value("fp_excel_path")
        fp_excel = rgv.get_value("fp_excel")
        Vcode = rgv.get_value("Vcode")
        web_result = rgv.get_value("web_result")
        username = rgv.get_value("username")
        fp_win = rgv.get_value("fp_win")
        v_date = rgv.get_value("v_date")
        fpcy_excel_path = rgv.get_value("fpcy_excel_path")
        fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
        lines_number = rgv.get_value("lines_number")
        fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
        check_html = rgv.get_value("check_html")
        fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
        fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
        size_changer = rgv.get_value("size_changer")
        invoice_web = rgv.get_value("invoice_web")
        fpcy_sheet = rgv.get_value("fpcy_sheet")
        data = rgv.get_value("data")
        fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
        fpcy_lines = rgv.get_value("fpcy_lines")
        verification_code = rgv.get_value("verification_code")
        result_path = rgv.get_value("result_path")
        i = rgv.get_value("i")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbwkd65', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbwkd65')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbwkd65', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)