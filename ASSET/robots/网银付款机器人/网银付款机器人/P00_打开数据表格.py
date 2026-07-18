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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kvknkdqp')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在打开数据文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvknkdqp', error, False)
    finally: 
        if node_success_flag == True:
            sleep(2)
            Debug_Block_Success('canvas-node-_kvknkdqp')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvknkdqp', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开数据文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_os9n5g4u')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_g6lwab0z')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wy_excel = rpa.app.microsoft.excel.open(wy_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_g6lwab0z', error, False)
            finally: 
                rgv.set_values({"wy_excel": wy_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_g6lwab0z')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_g6lwab0z', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 wy_excel''', 'success':node_success_flag, 'variables':{"wy_excel": str(wy_excel),"": str(),"wy_excel_path": str(wy_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kvknkdqq')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"未找到数据文件，请手动选择！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvknkdqq', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvknkdqq')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvknkdqq', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "未找到数据文件，请手动选择！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 调用自定义脚本
            try:
                Debug_Block_Start('canvas-node-_niaf4cpx')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 弹出文件选择窗口
                wy_excel_path=Select_file.start()
                
                if wy_excel_path == '':
                     sys.exit()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_niaf4cpx', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_niaf4cpx')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_niaf4cpx', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_tw12zcet')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wy_excel = rpa.app.microsoft.excel.open(wy_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_tw12zcet', error, False)
            finally: 
                rgv.set_values({"wy_excel": wy_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_tw12zcet')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_tw12zcet', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 wy_excel''', 'success':node_success_flag, 'variables':{"wy_excel": str(wy_excel),"": str(),"wy_excel_path": str(wy_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_4y2hodtl')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"机器人正在登录工行网银仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_4y2hodtl', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_4y2hodtl')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_4y2hodtl', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在登录工行网银仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_os9n5g4u', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_os9n5g4u')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_os9n5g4u', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_18blk9tb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if wy_excel is not None:
            sheet = wy_excel.get_sheet(r"网银付款")
            if sheet is not None:
                sheet.activate()
                wyfk_sheet= wy_excel.get_sheet()
        else:
            wyfk_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_18blk9tb', error, False)
    finally: 
        rgv.set_values({"wyfk_sheet": wyfk_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_18blk9tb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_18blk9tb', 'time':block_start_time, 'error': error, 'description':r'''在 wy_excel Excel对象中激活Sheet页 "网银付款"，将对应的Sheet页对象赋值给 wyfk_sheet''', 'success':node_success_flag, 'variables':{"wy_excel": str(wy_excel),"wyfk_sheet": str(wyfk_sheet)}})
        if (error is not None):
            sys.exit(1)
    # 获取Excel的行数
    try:
        Debug_Block_Start('canvas-node-_bc30z6dn')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if(wyfk_sheet is not None):
            wyfk_lines = wyfk_sheet.row_count()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_bc30z6dn', error, False)
    finally: 
        rgv.set_values({"wyfk_lines": wyfk_lines})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_bc30z6dn')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel的行数', 'id':'canvas-node-_bc30z6dn', 'time':block_start_time, 'error': error, 'description':r'''获取 wyfk_sheet Sheet页的行数''', 'success':node_success_flag, 'variables':{"wyfk_lines": str(wyfk_lines),"wyfk_sheet": str(wyfk_sheet)}})
        if (error is not None):
            sys.exit(1)