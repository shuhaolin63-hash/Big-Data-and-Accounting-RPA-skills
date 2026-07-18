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
    rgv.init_value("bankkey", r"123456")
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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kvkpkvqx')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在打开数据文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvkpkvqx', error, False)
    finally: 
        if node_success_flag == True:
            sleep(2)
            Debug_Block_Success('canvas-node-_kvkpkvqx')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvkpkvqx', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开数据文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_jx0wc1ic')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_9lqgr8dy')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wy_excel = rpa.app.microsoft.excel.open(wy_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_9lqgr8dy', error, False)
            finally: 
                rgv.set_values({"wy_excel": wy_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_9lqgr8dy')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_9lqgr8dy', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 wy_excel''', 'success':node_success_flag, 'variables':{"wy_excel": str(wy_excel),"wy_excel_path": str(wy_excel_path),"": str()}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kvkpxvqs')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"未找到数据文件，请手动选择！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkpxvqs', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvkpxvqs')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvkpxvqs', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "未找到数据文件，请手动选择！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 调用自定义脚本
            try:
                Debug_Block_Start('canvas-node-_qnj2f60h')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 弹出文件选择窗口
                wy_excel_path=Select_file.start()
                
                if wy_excel_path == '':
                     sys.exit()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_qnj2f60h', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_qnj2f60h')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_qnj2f60h', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_fv0089r5')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wy_excel = rpa.app.microsoft.excel.open(wy_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_fv0089r5', error, False)
            finally: 
                rgv.set_values({"wy_excel": wy_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_fv0089r5')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_fv0089r5', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 wy_excel''', 'success':node_success_flag, 'variables':{"wy_excel": str(wy_excel),"": str(),"wy_excel_path": str(wy_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_1x0yk4qz')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"机器人正在登录工行网银仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_1x0yk4qz', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_1x0yk4qz')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_1x0yk4qz', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在登录工行网银仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_jx0wc1ic', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_jx0wc1ic')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_jx0wc1ic', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_68d3la6v')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if wy_excel is not None:
            sheet = wy_excel.get_sheet(r"网银查询")
            if sheet is not None:
                sheet.activate()
                wycx_sheet= wy_excel.get_sheet()
        else:
            wycx_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_68d3la6v', error, False)
    finally: 
        rgv.set_values({"wycx_sheet": wycx_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_68d3la6v')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_68d3la6v', 'time':block_start_time, 'error': error, 'description':r'''在 wy_excel Excel对象中激活Sheet页 "网银查询"，将对应的Sheet页对象赋值给 wycx_sheet''', 'success':node_success_flag, 'variables':{"wycx_sheet": str(wycx_sheet),"wy_excel": str(wy_excel)}})
        if (error is not None):
            sys.exit(1)
    # 获取Excel的行数
    try:
        Debug_Block_Start('canvas-node-_bhkb7e5z')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if(wycx_sheet is not None):
            wycx_lines = wycx_sheet.row_count()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_bhkb7e5z', error, False)
    finally: 
        rgv.set_values({"wycx_lines": wycx_lines})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_bhkb7e5z')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel的行数', 'id':'canvas-node-_bhkb7e5z', 'time':block_start_time, 'error': error, 'description':r'''获取 wycx_sheet Sheet页的行数''', 'success':node_success_flag, 'variables':{"wycx_lines": str(wycx_lines),"wycx_sheet": str(wycx_sheet)}})
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