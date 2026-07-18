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
import P00_Open_Excel
import P01_Invoice_Certification
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
    # fprz_lines
    rgv.init_value("fprz_lines", None)
    fprz_lines = rgv.get_value("fprz_lines")
    # certification_key
    rgv.init_value("certification_key", r"cert_key_placeholder")
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
    # 申明自动创建变量
    Running_state = r""
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kw0gqp64')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        rgv.set_value("fprz_lines", fprz_lines)
        rgv.set_value("certification_key", certification_key)
        rgv.set_value("v_time", v_time)
        rgv.set_value("fp_win", fp_win)
        rgv.set_value("fp_excel", fp_excel)
        rgv.set_value("fp_excel_path", fp_excel_path)
        rgv.set_value("username", username)
        rgv.set_value("certification_web", certification_web)
        rgv.set_value("data", data)
        rgv.set_value("fprz_sheet", fprz_sheet)
        rgv.set_value("result_path", result_path)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("i", i)
        rgv.set_value("password", password)
        rgv.set_value("cookies", cookies)
        START.start()
        fprz_lines = rgv.get_value("fprz_lines")
        certification_key = rgv.get_value("certification_key")
        v_time = rgv.get_value("v_time")
        fp_win = rgv.get_value("fp_win")
        fp_excel = rgv.get_value("fp_excel")
        fp_excel_path = rgv.get_value("fp_excel_path")
        username = rgv.get_value("username")
        certification_web = rgv.get_value("certification_web")
        data = rgv.get_value("data")
        fprz_sheet = rgv.get_value("fprz_sheet")
        result_path = rgv.get_value("result_path")
        size_changer = rgv.get_value("size_changer")
        i = rgv.get_value("i")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kw0gqp64', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kw0gqp64')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kw0gqp64', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_kwbydxbb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kwbydxb9')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P00_Open_Excel 子流程
                rgv.set_value("fprz_lines", fprz_lines)
                rgv.set_value("certification_key", certification_key)
                rgv.set_value("v_time", v_time)
                rgv.set_value("fp_win", fp_win)
                rgv.set_value("fp_excel", fp_excel)
                rgv.set_value("fp_excel_path", fp_excel_path)
                rgv.set_value("username", username)
                rgv.set_value("certification_web", certification_web)
                rgv.set_value("data", data)
                rgv.set_value("fprz_sheet", fprz_sheet)
                rgv.set_value("result_path", result_path)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("i", i)
                rgv.set_value("password", password)
                rgv.set_value("cookies", cookies)
                P00_Open_Excel.start()
                fprz_lines = rgv.get_value("fprz_lines")
                certification_key = rgv.get_value("certification_key")
                v_time = rgv.get_value("v_time")
                fp_win = rgv.get_value("fp_win")
                fp_excel = rgv.get_value("fp_excel")
                fp_excel_path = rgv.get_value("fp_excel_path")
                username = rgv.get_value("username")
                certification_web = rgv.get_value("certification_web")
                data = rgv.get_value("data")
                fprz_sheet = rgv.get_value("fprz_sheet")
                result_path = rgv.get_value("result_path")
                size_changer = rgv.get_value("size_changer")
                i = rgv.get_value("i")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbydxb9', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbydxb9')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbydxb9', 'time':block_start_time, 'error': error, 'description':r'''调用 P00_Open_Excel 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kw0gqp65')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P01_Invoice_Certification 子流程
                rgv.set_value("fprz_lines", fprz_lines)
                rgv.set_value("certification_key", certification_key)
                rgv.set_value("v_time", v_time)
                rgv.set_value("fp_win", fp_win)
                rgv.set_value("fp_excel", fp_excel)
                rgv.set_value("fp_excel_path", fp_excel_path)
                rgv.set_value("username", username)
                rgv.set_value("certification_web", certification_web)
                rgv.set_value("data", data)
                rgv.set_value("fprz_sheet", fprz_sheet)
                rgv.set_value("result_path", result_path)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("i", i)
                rgv.set_value("password", password)
                rgv.set_value("cookies", cookies)
                P01_Invoice_Certification.start()
                fprz_lines = rgv.get_value("fprz_lines")
                certification_key = rgv.get_value("certification_key")
                v_time = rgv.get_value("v_time")
                fp_win = rgv.get_value("fp_win")
                fp_excel = rgv.get_value("fp_excel")
                fp_excel_path = rgv.get_value("fp_excel_path")
                username = rgv.get_value("username")
                certification_web = rgv.get_value("certification_web")
                data = rgv.get_value("data")
                fprz_sheet = rgv.get_value("fprz_sheet")
                result_path = rgv.get_value("result_path")
                size_changer = rgv.get_value("size_changer")
                i = rgv.get_value("i")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kw0gqp65', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kw0gqp65')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kw0gqp65', 'time':block_start_time, 'error': error, 'description':r'''调用 P01_Invoice_Certification 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kw09ag3u')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"发票认证机器人运行成功，感谢使用！", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kw09ag3u', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_kw09ag3u')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kw09ag3u', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "发票认证机器人运行成功，感谢使用！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 弹出提示框
            try:
                Debug_Block_Start('canvas-node-_kwbydxbf')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                Running_state = rpa.system.dialog.msgbox('信息', r"机器人运行异常，请查看运行日志，排除故障后再运行！", disappear_time=5)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbydxbf', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbydxbf')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出提示框', 'id':'canvas-node-_kwbydxbf', 'time':block_start_time, 'error': error, 'description':r'''弹出提示框''', 'success':node_success_flag, 'variables':{"Running_state": str(Running_state)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbydxbb', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbydxbb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_kwbydxbb', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kwbydxba')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        rgv.set_value("fprz_lines", fprz_lines)
        rgv.set_value("certification_key", certification_key)
        rgv.set_value("v_time", v_time)
        rgv.set_value("fp_win", fp_win)
        rgv.set_value("fp_excel", fp_excel)
        rgv.set_value("fp_excel_path", fp_excel_path)
        rgv.set_value("username", username)
        rgv.set_value("certification_web", certification_web)
        rgv.set_value("data", data)
        rgv.set_value("fprz_sheet", fprz_sheet)
        rgv.set_value("result_path", result_path)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("i", i)
        rgv.set_value("password", password)
        rgv.set_value("cookies", cookies)
        END.start()
        fprz_lines = rgv.get_value("fprz_lines")
        certification_key = rgv.get_value("certification_key")
        v_time = rgv.get_value("v_time")
        fp_win = rgv.get_value("fp_win")
        fp_excel = rgv.get_value("fp_excel")
        fp_excel_path = rgv.get_value("fp_excel_path")
        username = rgv.get_value("username")
        certification_web = rgv.get_value("certification_web")
        data = rgv.get_value("data")
        fprz_sheet = rgv.get_value("fprz_sheet")
        result_path = rgv.get_value("result_path")
        size_changer = rgv.get_value("size_changer")
        i = rgv.get_value("i")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbydxba', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbydxba')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbydxba', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 回写全局变量值
    rgv.set_value("fprz_lines", fprz_lines)
    rgv.set_value("certification_key", certification_key)
    rgv.set_value("v_time", v_time)
    rgv.set_value("fp_win", fp_win)
    rgv.set_value("fp_excel", fp_excel)
    rgv.set_value("fp_excel_path", fp_excel_path)
    rgv.set_value("username", username)
    rgv.set_value("certification_web", certification_web)
    rgv.set_value("data", data)
    rgv.set_value("fprz_sheet", fprz_sheet)
    rgv.set_value("result_path", result_path)
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("i", i)
    rgv.set_value("password", password)
    rgv.set_value("cookies", cookies)