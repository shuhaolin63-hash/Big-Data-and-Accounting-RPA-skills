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
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # fpkj_excel
    rgv.init_value("fpkj_excel", None)
    fpkj_excel = rgv.get_value("fpkj_excel")
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
    # fpkj_win
    rgv.init_value("fpkj_win", None)
    fpkj_win = rgv.get_value("fpkj_win")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # fpkj_excel_path
    rgv.init_value("fpkj_excel_path", r"C:\RPADATA\发票开具业务(数电票)数据表.xls")
    fpkj_excel_path = rgv.get_value("fpkj_excel_path")
    # 申明自动创建变量
    v_file_path_1 = r""
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_lofgjgac')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在打开业务数据表……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgac', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgac')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_lofgjgac', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开业务数据表……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_lofgjgad')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_lofgjgah')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fpkj_excel = rpa.app.microsoft.excel.open(fpkj_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgah', error, False)
            finally: 
                rgv.set_values({"fpkj_excel": fpkj_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgah')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_lofgjgah', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fpkj_excel''', 'success':node_success_flag, 'variables':{"fpkj_excel": str(fpkj_excel),"v_file_path_1": str(v_file_path_1),"fpkj_excel_path": str(fpkj_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_lofgjgai')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r" 未找到数据文件，请手动选择！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgai', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgai')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_lofgjgai', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 " 未找到数据文件，请手动选择！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 调用自定义脚本
            try:
                Debug_Block_Start('canvas-node-_lofgjgak')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 弹出文件选择窗口
                fpzbkj_excel_path=Select_file.start()
                
                if fpzbkj_excel_path == '':
                     sys.exit()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgak', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgak')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_lofgjgak', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_lofgjgaj')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fpkj_excel = rpa.app.microsoft.excel.open(fpkj_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgaj', error, False)
            finally: 
                rgv.set_values({"fpkj_excel": fpkj_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgaj')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_lofgjgaj', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fpkj_excel''', 'success':node_success_flag, 'variables':{"fpkj_excel": str(fpkj_excel),"v_file_path_1": str(v_file_path_1),"fpkj_excel_path": str(fpkj_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_logloagy')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"机器人正在打开业务数据表……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logloagy', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logloagy')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_logloagy', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开业务数据表……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgad', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgad')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_lofgjgad', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_lofgjgal')
        node_success_flag = True
        sleep(10)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpkj_excel is not None:
            sheet = fpkj_excel.get_sheet(r"发票开具")
            if sheet is not None:
                sheet.activate()
                fpkj_sheet= fpkj_excel.get_sheet()
        else:
            fpkj_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgal', error, False)
    finally: 
        rgv.set_values({"fpkj_sheet": fpkj_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgal')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_lofgjgal', 'time':block_start_time, 'error': error, 'description':r'''在 fpkj_excel Excel对象中激活Sheet页 "发票开具"，将对应的Sheet页对象赋值给 fpkj_sheet''', 'success':node_success_flag, 'variables':{"fpkj_sheet": str(fpkj_sheet),"fpkj_excel": str(fpkj_excel)}})
        if (error is not None):
            sys.exit(1)
    # 获取Excel的行数
    try:
        Debug_Block_Start('canvas-node-_lofgjgb4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if(fpkj_sheet is not None):
            lines = fpkj_sheet.row_count()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgb4', error, False)
    finally: 
        rgv.set_values({"lines": lines})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgb4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel的行数', 'id':'canvas-node-_lofgjgb4', 'time':block_start_time, 'error': error, 'description':r'''获取 fpkj_sheet Sheet页的行数''', 'success':node_success_flag, 'variables':{"lines": str(lines),"fpkj_sheet": str(fpkj_sheet)}})
        if (error is not None):
            sys.exit(1)