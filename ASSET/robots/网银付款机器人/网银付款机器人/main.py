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
import P01_登录工行网银
import P02_获取数据
import P03_逐笔付款
import P04_查询付款信息
import P05_退出工行网银
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
    # data
    rgv.init_value("data", None)
    data = rgv.get_value("data")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # bankkey
    rgv.init_value("bankkey", r"bankkey_placeholder")
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
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kvkonlrq')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        rgv.set_value("data", data)
        rgv.set_value("save_as_dialog", save_as_dialog)
        rgv.set_value("bankkey", bankkey)
        rgv.set_value("v_time", v_time)
        rgv.set_value("wy_excel", wy_excel)
        rgv.set_value("wy_excel_path", wy_excel_path)
        rgv.set_value("fp_win", fp_win)
        rgv.set_value("username", username)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("wyfk_lines", wyfk_lines)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("Running_state", Running_state)
        rgv.set_value("cookies", cookies)
        rgv.set_value("password", password)
        START.start()
        data = rgv.get_value("data")
        save_as_dialog = rgv.get_value("save_as_dialog")
        bankkey = rgv.get_value("bankkey")
        v_time = rgv.get_value("v_time")
        wy_excel = rgv.get_value("wy_excel")
        wy_excel_path = rgv.get_value("wy_excel_path")
        fp_win = rgv.get_value("fp_win")
        username = rgv.get_value("username")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        wyfk_lines = rgv.get_value("wyfk_lines")
        size_changer = rgv.get_value("size_changer")
        Running_state = rgv.get_value("Running_state")
        cookies = rgv.get_value("cookies")
        password = rgv.get_value("password")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvkonlrq', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kvkonlrq')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlrq', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_kwbyr2f5')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kvkonlrr')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P00_打开数据表格 子流程
                rgv.set_value("data", data)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("v_time", v_time)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("fp_win", fp_win)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("wyfk_lines", wyfk_lines)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("Running_state", Running_state)
                rgv.set_value("cookies", cookies)
                rgv.set_value("password", password)
                P00_打开数据表格.start()
                data = rgv.get_value("data")
                save_as_dialog = rgv.get_value("save_as_dialog")
                bankkey = rgv.get_value("bankkey")
                v_time = rgv.get_value("v_time")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                fp_win = rgv.get_value("fp_win")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                wyfk_lines = rgv.get_value("wyfk_lines")
                size_changer = rgv.get_value("size_changer")
                Running_state = rgv.get_value("Running_state")
                cookies = rgv.get_value("cookies")
                password = rgv.get_value("password")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkonlrr', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvkonlrr')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlrr', 'time':block_start_time, 'error': error, 'description':r'''调用 P00_打开数据表格 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kwbyr2f3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P01_登录工行网银 子流程
                rgv.set_value("data", data)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("v_time", v_time)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("fp_win", fp_win)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("wyfk_lines", wyfk_lines)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("Running_state", Running_state)
                rgv.set_value("cookies", cookies)
                rgv.set_value("password", password)
                P01_登录工行网银.start()
                data = rgv.get_value("data")
                save_as_dialog = rgv.get_value("save_as_dialog")
                bankkey = rgv.get_value("bankkey")
                v_time = rgv.get_value("v_time")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                fp_win = rgv.get_value("fp_win")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                wyfk_lines = rgv.get_value("wyfk_lines")
                size_changer = rgv.get_value("size_changer")
                Running_state = rgv.get_value("Running_state")
                cookies = rgv.get_value("cookies")
                password = rgv.get_value("password")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbyr2f3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbyr2f3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbyr2f3', 'time':block_start_time, 'error': error, 'description':r'''调用 P01_登录工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 按照次数循环
            try:
                Debug_Block_Start('flow_kq8wa02y')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                for i in range(int(2), int(wyfk_lines) + 1, int(1)):
                    pass
                    # 设置变量值
                    try:
                        Debug_Block_Start('canvas-node-_kvkonlrw')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rgv.set_value("i", i)
                        i = i
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkonlrw', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkonlrw')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_kvkonlrw', 'time':block_start_time, 'error': error, 'description':r'''设置变量 i 的值为 i''', 'success':node_success_flag, 'variables':{"i": str(i)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_kvkonlrs')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # 调用 P02_获取数据 子流程
                        rgv.set_value("data", data)
                        rgv.set_value("save_as_dialog", save_as_dialog)
                        rgv.set_value("bankkey", bankkey)
                        rgv.set_value("v_time", v_time)
                        rgv.set_value("wy_excel", wy_excel)
                        rgv.set_value("wy_excel_path", wy_excel_path)
                        rgv.set_value("fp_win", fp_win)
                        rgv.set_value("username", username)
                        rgv.set_value("bank_web", bank_web)
                        rgv.set_value("i", i)
                        rgv.set_value("wyfk_sheet", wyfk_sheet)
                        rgv.set_value("wyfk_lines", wyfk_lines)
                        rgv.set_value("size_changer", size_changer)
                        rgv.set_value("Running_state", Running_state)
                        rgv.set_value("cookies", cookies)
                        rgv.set_value("password", password)
                        P02_获取数据.start()
                        data = rgv.get_value("data")
                        save_as_dialog = rgv.get_value("save_as_dialog")
                        bankkey = rgv.get_value("bankkey")
                        v_time = rgv.get_value("v_time")
                        wy_excel = rgv.get_value("wy_excel")
                        wy_excel_path = rgv.get_value("wy_excel_path")
                        fp_win = rgv.get_value("fp_win")
                        username = rgv.get_value("username")
                        bank_web = rgv.get_value("bank_web")
                        i = rgv.get_value("i")
                        wyfk_sheet = rgv.get_value("wyfk_sheet")
                        wyfk_lines = rgv.get_value("wyfk_lines")
                        size_changer = rgv.get_value("size_changer")
                        Running_state = rgv.get_value("Running_state")
                        cookies = rgv.get_value("cookies")
                        password = rgv.get_value("password")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkonlrs', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkonlrs')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlrs', 'time':block_start_time, 'error': error, 'description':r'''调用 P02_获取数据 子流程''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_kvkonlrt')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # 调用 P03_逐笔付款 子流程
                        rgv.set_value("data", data)
                        rgv.set_value("save_as_dialog", save_as_dialog)
                        rgv.set_value("bankkey", bankkey)
                        rgv.set_value("v_time", v_time)
                        rgv.set_value("wy_excel", wy_excel)
                        rgv.set_value("wy_excel_path", wy_excel_path)
                        rgv.set_value("fp_win", fp_win)
                        rgv.set_value("username", username)
                        rgv.set_value("bank_web", bank_web)
                        rgv.set_value("i", i)
                        rgv.set_value("wyfk_sheet", wyfk_sheet)
                        rgv.set_value("wyfk_lines", wyfk_lines)
                        rgv.set_value("size_changer", size_changer)
                        rgv.set_value("Running_state", Running_state)
                        rgv.set_value("cookies", cookies)
                        rgv.set_value("password", password)
                        P03_逐笔付款.start()
                        data = rgv.get_value("data")
                        save_as_dialog = rgv.get_value("save_as_dialog")
                        bankkey = rgv.get_value("bankkey")
                        v_time = rgv.get_value("v_time")
                        wy_excel = rgv.get_value("wy_excel")
                        wy_excel_path = rgv.get_value("wy_excel_path")
                        fp_win = rgv.get_value("fp_win")
                        username = rgv.get_value("username")
                        bank_web = rgv.get_value("bank_web")
                        i = rgv.get_value("i")
                        wyfk_sheet = rgv.get_value("wyfk_sheet")
                        wyfk_lines = rgv.get_value("wyfk_lines")
                        size_changer = rgv.get_value("size_changer")
                        Running_state = rgv.get_value("Running_state")
                        cookies = rgv.get_value("cookies")
                        password = rgv.get_value("password")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkonlrt', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkonlrt')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlrt', 'time':block_start_time, 'error': error, 'description':r'''调用 P03_逐笔付款 子流程''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_kvkonlru')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # 调用 P04_查询付款信息 子流程
                        rgv.set_value("data", data)
                        rgv.set_value("save_as_dialog", save_as_dialog)
                        rgv.set_value("bankkey", bankkey)
                        rgv.set_value("v_time", v_time)
                        rgv.set_value("wy_excel", wy_excel)
                        rgv.set_value("wy_excel_path", wy_excel_path)
                        rgv.set_value("fp_win", fp_win)
                        rgv.set_value("username", username)
                        rgv.set_value("bank_web", bank_web)
                        rgv.set_value("i", i)
                        rgv.set_value("wyfk_sheet", wyfk_sheet)
                        rgv.set_value("wyfk_lines", wyfk_lines)
                        rgv.set_value("size_changer", size_changer)
                        rgv.set_value("Running_state", Running_state)
                        rgv.set_value("cookies", cookies)
                        rgv.set_value("password", password)
                        P04_查询付款信息.start()
                        data = rgv.get_value("data")
                        save_as_dialog = rgv.get_value("save_as_dialog")
                        bankkey = rgv.get_value("bankkey")
                        v_time = rgv.get_value("v_time")
                        wy_excel = rgv.get_value("wy_excel")
                        wy_excel_path = rgv.get_value("wy_excel_path")
                        fp_win = rgv.get_value("fp_win")
                        username = rgv.get_value("username")
                        bank_web = rgv.get_value("bank_web")
                        i = rgv.get_value("i")
                        wyfk_sheet = rgv.get_value("wyfk_sheet")
                        wyfk_lines = rgv.get_value("wyfk_lines")
                        size_changer = rgv.get_value("size_changer")
                        Running_state = rgv.get_value("Running_state")
                        cookies = rgv.get_value("cookies")
                        password = rgv.get_value("password")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkonlru', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkonlru')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlru', 'time':block_start_time, 'error': error, 'description':r'''调用 P04_查询付款信息 子流程''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('flow_kq8wa02y', error, False)
            finally: 
                rgv.set_values({"i": i})
                if node_success_flag == True:
                    Debug_Block_Success('flow_kq8wa02y')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'按照次数循环', 'id':'flow_kq8wa02y', 'time':block_start_time, 'error': error, 'description':r'''从 2 开始到 wyfk_lines 结束，步长 1 ，每次循环的值赋值给 i''', 'success':node_success_flag, 'variables':{"wyfk_lines": str(wyfk_lines),"i": str(i)}})
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kvkonlrv')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P05_退出工行网银 子流程
                rgv.set_value("data", data)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("v_time", v_time)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("fp_win", fp_win)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("wyfk_lines", wyfk_lines)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("Running_state", Running_state)
                rgv.set_value("cookies", cookies)
                rgv.set_value("password", password)
                P05_退出工行网银.start()
                data = rgv.get_value("data")
                save_as_dialog = rgv.get_value("save_as_dialog")
                bankkey = rgv.get_value("bankkey")
                v_time = rgv.get_value("v_time")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                fp_win = rgv.get_value("fp_win")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                wyfk_lines = rgv.get_value("wyfk_lines")
                size_changer = rgv.get_value("size_changer")
                Running_state = rgv.get_value("Running_state")
                cookies = rgv.get_value("cookies")
                password = rgv.get_value("password")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkonlrv', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvkonlrv')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkonlrv', 'time':block_start_time, 'error': error, 'description':r'''调用 P05_退出工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_1l9014sw')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"网银付款机器人运行成功，感谢使用！", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_1l9014sw', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_1l9014sw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_1l9014sw', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "网银付款机器人运行成功，感谢使用！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 弹出提示框
            try:
                Debug_Block_Start('canvas-node-_kwbyr2fa')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                Running_state = rpa.system.dialog.msgbox('信息', r"机器人运行异常，请查看运行日志，排除故障后再运行！", disappear_time=5)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbyr2fa', error, False)
            finally: 
                rgv.set_values({"Running_state": Running_state})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbyr2fa')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出提示框', 'id':'canvas-node-_kwbyr2fa', 'time':block_start_time, 'error': error, 'description':r'''弹出提示框''', 'success':node_success_flag, 'variables':{"Running_state": str(Running_state)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbyr2f5', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbyr2f5')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_kwbyr2f5', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kwbyr2f4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        rgv.set_value("data", data)
        rgv.set_value("save_as_dialog", save_as_dialog)
        rgv.set_value("bankkey", bankkey)
        rgv.set_value("v_time", v_time)
        rgv.set_value("wy_excel", wy_excel)
        rgv.set_value("wy_excel_path", wy_excel_path)
        rgv.set_value("fp_win", fp_win)
        rgv.set_value("username", username)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("wyfk_lines", wyfk_lines)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("Running_state", Running_state)
        rgv.set_value("cookies", cookies)
        rgv.set_value("password", password)
        END.start()
        data = rgv.get_value("data")
        save_as_dialog = rgv.get_value("save_as_dialog")
        bankkey = rgv.get_value("bankkey")
        v_time = rgv.get_value("v_time")
        wy_excel = rgv.get_value("wy_excel")
        wy_excel_path = rgv.get_value("wy_excel_path")
        fp_win = rgv.get_value("fp_win")
        username = rgv.get_value("username")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        wyfk_lines = rgv.get_value("wyfk_lines")
        size_changer = rgv.get_value("size_changer")
        Running_state = rgv.get_value("Running_state")
        cookies = rgv.get_value("cookies")
        password = rgv.get_value("password")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbyr2f4', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbyr2f4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbyr2f4', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 回写全局变量值
    rgv.set_value("data", data)
    rgv.set_value("save_as_dialog", save_as_dialog)
    rgv.set_value("bankkey", bankkey)
    rgv.set_value("v_time", v_time)
    rgv.set_value("wy_excel", wy_excel)
    rgv.set_value("wy_excel_path", wy_excel_path)
    rgv.set_value("fp_win", fp_win)
    rgv.set_value("username", username)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("wyfk_lines", wyfk_lines)
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("Running_state", Running_state)
    rgv.set_value("cookies", cookies)
    rgv.set_value("password", password)