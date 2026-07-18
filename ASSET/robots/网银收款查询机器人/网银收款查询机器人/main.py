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
import P03_查询收款信息
import P04_退出工行网银
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
    # wycx_lines
    rgv.init_value("wycx_lines", None)
    wycx_lines = rgv.get_value("wycx_lines")
    # wy_win
    rgv.init_value("wy_win", None)
    wy_win = rgv.get_value("wy_win")
    # bankkey
    rgv.init_value("bankkey", r"bankkey_placeholder")
    bankkey = rgv.get_value("bankkey")
    # tsk_value
    rgv.init_value("tsk_value", r"")
    tsk_value = rgv.get_value("tsk_value")
    # wy_excel
    rgv.init_value("wy_excel", None)
    wy_excel = rgv.get_value("wy_excel")
    # wy_excel_path
    rgv.init_value("wy_excel_path", r"C:\\RPADATA\\收款查询业务数据表.xls")
    wy_excel_path = rgv.get_value("wy_excel_path")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # u
    rgv.init_value("u", None)
    u = rgv.get_value("u")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # account_web
    rgv.init_value("account_web", None)
    account_web = rgv.get_value("account_web")
    # wycx_sheet
    rgv.init_value("wycx_sheet", None)
    wycx_sheet = rgv.get_value("wycx_sheet")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
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
        Debug_Block_Start('canvas-node-_kvkq5lx0')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        rgv.set_value("data", data)
        rgv.set_value("wycx_lines", wycx_lines)
        rgv.set_value("wy_win", wy_win)
        rgv.set_value("bankkey", bankkey)
        rgv.set_value("tsk_value", tsk_value)
        rgv.set_value("wy_excel", wy_excel)
        rgv.set_value("wy_excel_path", wy_excel_path)
        rgv.set_value("username", username)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("u", u)
        rgv.set_value("v_time", v_time)
        rgv.set_value("save_as_dialog", save_as_dialog)
        rgv.set_value("account_web", account_web)
        rgv.set_value("wycx_sheet", wycx_sheet)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("password", password)
        rgv.set_value("cookies", cookies)
        START.start()
        data = rgv.get_value("data")
        wycx_lines = rgv.get_value("wycx_lines")
        wy_win = rgv.get_value("wy_win")
        bankkey = rgv.get_value("bankkey")
        tsk_value = rgv.get_value("tsk_value")
        wy_excel = rgv.get_value("wy_excel")
        wy_excel_path = rgv.get_value("wy_excel_path")
        username = rgv.get_value("username")
        bank_web = rgv.get_value("bank_web")
        u = rgv.get_value("u")
        v_time = rgv.get_value("v_time")
        save_as_dialog = rgv.get_value("save_as_dialog")
        account_web = rgv.get_value("account_web")
        wycx_sheet = rgv.get_value("wycx_sheet")
        size_changer = rgv.get_value("size_changer")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvkq5lx0', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kvkq5lx0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkq5lx0', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_kwbzhbpm')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kwbzhbpk')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P00_打开数据表格 子流程
                rgv.set_value("data", data)
                rgv.set_value("wycx_lines", wycx_lines)
                rgv.set_value("wy_win", wy_win)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("tsk_value", tsk_value)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("u", u)
                rgv.set_value("v_time", v_time)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("account_web", account_web)
                rgv.set_value("wycx_sheet", wycx_sheet)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("password", password)
                rgv.set_value("cookies", cookies)
                P00_打开数据表格.start()
                data = rgv.get_value("data")
                wycx_lines = rgv.get_value("wycx_lines")
                wy_win = rgv.get_value("wy_win")
                bankkey = rgv.get_value("bankkey")
                tsk_value = rgv.get_value("tsk_value")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                u = rgv.get_value("u")
                v_time = rgv.get_value("v_time")
                save_as_dialog = rgv.get_value("save_as_dialog")
                account_web = rgv.get_value("account_web")
                wycx_sheet = rgv.get_value("wycx_sheet")
                size_changer = rgv.get_value("size_changer")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbzhbpk', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbzhbpk')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbzhbpk', 'time':block_start_time, 'error': error, 'description':r'''调用 P00_打开数据表格 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kvkq5lx1')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P01_登录工行网银 子流程
                rgv.set_value("data", data)
                rgv.set_value("wycx_lines", wycx_lines)
                rgv.set_value("wy_win", wy_win)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("tsk_value", tsk_value)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("u", u)
                rgv.set_value("v_time", v_time)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("account_web", account_web)
                rgv.set_value("wycx_sheet", wycx_sheet)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("password", password)
                rgv.set_value("cookies", cookies)
                P01_登录工行网银.start()
                data = rgv.get_value("data")
                wycx_lines = rgv.get_value("wycx_lines")
                wy_win = rgv.get_value("wy_win")
                bankkey = rgv.get_value("bankkey")
                tsk_value = rgv.get_value("tsk_value")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                u = rgv.get_value("u")
                v_time = rgv.get_value("v_time")
                save_as_dialog = rgv.get_value("save_as_dialog")
                account_web = rgv.get_value("account_web")
                wycx_sheet = rgv.get_value("wycx_sheet")
                size_changer = rgv.get_value("size_changer")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkq5lx1', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvkq5lx1')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkq5lx1', 'time':block_start_time, 'error': error, 'description':r'''调用 P01_登录工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 按照次数循环
            try:
                Debug_Block_Start('flow_kqfz9u8t')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                for u in range(int(2), int(wycx_lines) + 1, int(1)):
                    pass
                    # 设置变量值
                    try:
                        Debug_Block_Start('canvas-node-_kvkq5lx5')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rgv.set_value("u", u)
                        u = u
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkq5lx5', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkq5lx5')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_kvkq5lx5', 'time':block_start_time, 'error': error, 'description':r'''设置变量 u 的值为 u''', 'success':node_success_flag, 'variables':{"u": str(u)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_kvkq5lx2')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # 调用 P02_获取数据 子流程
                        rgv.set_value("data", data)
                        rgv.set_value("wycx_lines", wycx_lines)
                        rgv.set_value("wy_win", wy_win)
                        rgv.set_value("bankkey", bankkey)
                        rgv.set_value("tsk_value", tsk_value)
                        rgv.set_value("wy_excel", wy_excel)
                        rgv.set_value("wy_excel_path", wy_excel_path)
                        rgv.set_value("username", username)
                        rgv.set_value("bank_web", bank_web)
                        rgv.set_value("u", u)
                        rgv.set_value("v_time", v_time)
                        rgv.set_value("save_as_dialog", save_as_dialog)
                        rgv.set_value("account_web", account_web)
                        rgv.set_value("wycx_sheet", wycx_sheet)
                        rgv.set_value("size_changer", size_changer)
                        rgv.set_value("password", password)
                        rgv.set_value("cookies", cookies)
                        P02_获取数据.start()
                        data = rgv.get_value("data")
                        wycx_lines = rgv.get_value("wycx_lines")
                        wy_win = rgv.get_value("wy_win")
                        bankkey = rgv.get_value("bankkey")
                        tsk_value = rgv.get_value("tsk_value")
                        wy_excel = rgv.get_value("wy_excel")
                        wy_excel_path = rgv.get_value("wy_excel_path")
                        username = rgv.get_value("username")
                        bank_web = rgv.get_value("bank_web")
                        u = rgv.get_value("u")
                        v_time = rgv.get_value("v_time")
                        save_as_dialog = rgv.get_value("save_as_dialog")
                        account_web = rgv.get_value("account_web")
                        wycx_sheet = rgv.get_value("wycx_sheet")
                        size_changer = rgv.get_value("size_changer")
                        password = rgv.get_value("password")
                        cookies = rgv.get_value("cookies")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkq5lx2', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkq5lx2')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkq5lx2', 'time':block_start_time, 'error': error, 'description':r'''调用 P02_获取数据 子流程''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_kvkq5lx3')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # 调用 P03_查询收款信息 子流程
                        rgv.set_value("data", data)
                        rgv.set_value("wycx_lines", wycx_lines)
                        rgv.set_value("wy_win", wy_win)
                        rgv.set_value("bankkey", bankkey)
                        rgv.set_value("tsk_value", tsk_value)
                        rgv.set_value("wy_excel", wy_excel)
                        rgv.set_value("wy_excel_path", wy_excel_path)
                        rgv.set_value("username", username)
                        rgv.set_value("bank_web", bank_web)
                        rgv.set_value("u", u)
                        rgv.set_value("v_time", v_time)
                        rgv.set_value("save_as_dialog", save_as_dialog)
                        rgv.set_value("account_web", account_web)
                        rgv.set_value("wycx_sheet", wycx_sheet)
                        rgv.set_value("size_changer", size_changer)
                        rgv.set_value("password", password)
                        rgv.set_value("cookies", cookies)
                        P03_查询收款信息.start()
                        data = rgv.get_value("data")
                        wycx_lines = rgv.get_value("wycx_lines")
                        wy_win = rgv.get_value("wy_win")
                        bankkey = rgv.get_value("bankkey")
                        tsk_value = rgv.get_value("tsk_value")
                        wy_excel = rgv.get_value("wy_excel")
                        wy_excel_path = rgv.get_value("wy_excel_path")
                        username = rgv.get_value("username")
                        bank_web = rgv.get_value("bank_web")
                        u = rgv.get_value("u")
                        v_time = rgv.get_value("v_time")
                        save_as_dialog = rgv.get_value("save_as_dialog")
                        account_web = rgv.get_value("account_web")
                        wycx_sheet = rgv.get_value("wycx_sheet")
                        size_changer = rgv.get_value("size_changer")
                        password = rgv.get_value("password")
                        cookies = rgv.get_value("cookies")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvkq5lx3', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvkq5lx3')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkq5lx3', 'time':block_start_time, 'error': error, 'description':r'''调用 P03_查询收款信息 子流程''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('flow_kqfz9u8t', error, False)
            finally: 
                rgv.set_values({"u": u})
                if node_success_flag == True:
                    Debug_Block_Success('flow_kqfz9u8t')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'按照次数循环', 'id':'flow_kqfz9u8t', 'time':block_start_time, 'error': error, 'description':r'''从 2 开始到 wycx_lines 结束，步长 1 ，每次循环的值赋值给 u''', 'success':node_success_flag, 'variables':{"wycx_lines": str(wycx_lines),"u": str(u)}})
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_kvkq5lx4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P04_退出工行网银 子流程
                rgv.set_value("data", data)
                rgv.set_value("wycx_lines", wycx_lines)
                rgv.set_value("wy_win", wy_win)
                rgv.set_value("bankkey", bankkey)
                rgv.set_value("tsk_value", tsk_value)
                rgv.set_value("wy_excel", wy_excel)
                rgv.set_value("wy_excel_path", wy_excel_path)
                rgv.set_value("username", username)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("u", u)
                rgv.set_value("v_time", v_time)
                rgv.set_value("save_as_dialog", save_as_dialog)
                rgv.set_value("account_web", account_web)
                rgv.set_value("wycx_sheet", wycx_sheet)
                rgv.set_value("size_changer", size_changer)
                rgv.set_value("password", password)
                rgv.set_value("cookies", cookies)
                P04_退出工行网银.start()
                data = rgv.get_value("data")
                wycx_lines = rgv.get_value("wycx_lines")
                wy_win = rgv.get_value("wy_win")
                bankkey = rgv.get_value("bankkey")
                tsk_value = rgv.get_value("tsk_value")
                wy_excel = rgv.get_value("wy_excel")
                wy_excel_path = rgv.get_value("wy_excel_path")
                username = rgv.get_value("username")
                bank_web = rgv.get_value("bank_web")
                u = rgv.get_value("u")
                v_time = rgv.get_value("v_time")
                save_as_dialog = rgv.get_value("save_as_dialog")
                account_web = rgv.get_value("account_web")
                wycx_sheet = rgv.get_value("wycx_sheet")
                size_changer = rgv.get_value("size_changer")
                password = rgv.get_value("password")
                cookies = rgv.get_value("cookies")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkq5lx4', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvkq5lx4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kvkq5lx4', 'time':block_start_time, 'error': error, 'description':r'''调用 P04_退出工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kvkq5lwy')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"网银收款查询机器人运行成功，感谢使用！", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkq5lwy', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_kvkq5lwy')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvkq5lwy', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "网银收款查询机器人运行成功，感谢使用！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 弹出提示框
            try:
                Debug_Block_Start('canvas-node-_kwbzhbpq')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                Running_state = rpa.system.dialog.msgbox('信息', r"机器人运行异常，请查看运行日志，排除故障后再运行！", disappear_time=5)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwbzhbpq', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwbzhbpq')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出提示框', 'id':'canvas-node-_kwbzhbpq', 'time':block_start_time, 'error': error, 'description':r'''弹出提示框''', 'success':node_success_flag, 'variables':{"Running_state": str(Running_state)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbzhbpm', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbzhbpm')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_kwbzhbpm', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_kwbzhbpl')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        rgv.set_value("data", data)
        rgv.set_value("wycx_lines", wycx_lines)
        rgv.set_value("wy_win", wy_win)
        rgv.set_value("bankkey", bankkey)
        rgv.set_value("tsk_value", tsk_value)
        rgv.set_value("wy_excel", wy_excel)
        rgv.set_value("wy_excel_path", wy_excel_path)
        rgv.set_value("username", username)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("u", u)
        rgv.set_value("v_time", v_time)
        rgv.set_value("save_as_dialog", save_as_dialog)
        rgv.set_value("account_web", account_web)
        rgv.set_value("wycx_sheet", wycx_sheet)
        rgv.set_value("size_changer", size_changer)
        rgv.set_value("password", password)
        rgv.set_value("cookies", cookies)
        END.start()
        data = rgv.get_value("data")
        wycx_lines = rgv.get_value("wycx_lines")
        wy_win = rgv.get_value("wy_win")
        bankkey = rgv.get_value("bankkey")
        tsk_value = rgv.get_value("tsk_value")
        wy_excel = rgv.get_value("wy_excel")
        wy_excel_path = rgv.get_value("wy_excel_path")
        username = rgv.get_value("username")
        bank_web = rgv.get_value("bank_web")
        u = rgv.get_value("u")
        v_time = rgv.get_value("v_time")
        save_as_dialog = rgv.get_value("save_as_dialog")
        account_web = rgv.get_value("account_web")
        wycx_sheet = rgv.get_value("wycx_sheet")
        size_changer = rgv.get_value("size_changer")
        password = rgv.get_value("password")
        cookies = rgv.get_value("cookies")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbzhbpl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbzhbpl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_kwbzhbpl', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 回写全局变量值
    rgv.set_value("data", data)
    rgv.set_value("wycx_lines", wycx_lines)
    rgv.set_value("wy_win", wy_win)
    rgv.set_value("bankkey", bankkey)
    rgv.set_value("tsk_value", tsk_value)
    rgv.set_value("wy_excel", wy_excel)
    rgv.set_value("wy_excel_path", wy_excel_path)
    rgv.set_value("username", username)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("u", u)
    rgv.set_value("v_time", v_time)
    rgv.set_value("save_as_dialog", save_as_dialog)
    rgv.set_value("account_web", account_web)
    rgv.set_value("wycx_sheet", wycx_sheet)
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("password", password)
    rgv.set_value("cookies", cookies)