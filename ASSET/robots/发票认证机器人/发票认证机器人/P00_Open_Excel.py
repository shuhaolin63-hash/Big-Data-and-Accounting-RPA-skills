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
    # fprz_lines
    rgv.init_value("fprz_lines", None)
    fprz_lines = rgv.get_value("fprz_lines")
    # certification_key
    rgv.init_value("certification_key", r"8888888888888888")
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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_q858rclc')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在打开数据文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_q858rclc', error, False)
    finally: 
        if node_success_flag == True:
            sleep(2)
            Debug_Block_Success('canvas-node-_q858rclc')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_q858rclc', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在打开数据文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_ir3c9zfi')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_w2rmk27j')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fp_excel = rpa.app.microsoft.excel.open(fp_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_w2rmk27j', error, False)
            finally: 
                rgv.set_values({"fp_excel": fp_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_w2rmk27j')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_w2rmk27j', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fp_excel''', 'success':node_success_flag, 'variables':{"fp_excel": str(fp_excel),"fp_excel_path": str(fp_excel_path),"": str()}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_c48uiak6')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"未找到数据文件，请手动选择！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_c48uiak6', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_c48uiak6')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_c48uiak6', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "未找到数据文件，请手动选择！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 调用自定义脚本
            try:
                Debug_Block_Start('canvas-node-_u3s66ftk')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 弹出文件选择窗口
                fp_excel_path=Select_file.start()
                
                if fp_excel_path == '':
                     sys.exit()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_u3s66ftk', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_u3s66ftk')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_u3s66ftk', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 启动Excel
            try:
                Debug_Block_Start('canvas-node-_qhhwzd8v')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fp_excel = rpa.app.microsoft.excel.open(fp_excel_path, visible=True, readonly=False, password=r"", write_password=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_qhhwzd8v', error, False)
            finally: 
                rgv.set_values({"fp_excel": fp_excel})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_qhhwzd8v')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_qhhwzd8v', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fp_excel''', 'success':node_success_flag, 'variables':{"fp_excel": str(fp_excel),"": str(),"fp_excel_path": str(fp_excel_path)}})
                if (error is not None):
                    sys.exit(1)
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_7bdhbpe7')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"机器人开始进行发票认证……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_7bdhbpe7', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_7bdhbpe7')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_7bdhbpe7', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始进行发票认证……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ir3c9zfi', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ir3c9zfi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_ir3c9zfi', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_y7iqs9iw')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fp_excel is not None:
            sheet = fp_excel.get_sheet(r"发票认证")
            if sheet is not None:
                sheet.activate()
                fprz_sheet= fp_excel.get_sheet()
        else:
            fprz_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_y7iqs9iw', error, False)
    finally: 
        rgv.set_values({"fprz_sheet": fprz_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_y7iqs9iw')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_y7iqs9iw', 'time':block_start_time, 'error': error, 'description':r'''在 fp_excel Excel对象中激活Sheet页 "发票认证"，将对应的Sheet页对象赋值给 fprz_sheet''', 'success':node_success_flag, 'variables':{"fprz_sheet": str(fprz_sheet),"fp_excel": str(fp_excel)}})
        if (error is not None):
            sys.exit(1)
    # 获取Excel的行数
    try:
        Debug_Block_Start('canvas-node-_1aiynse1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if(fprz_sheet is not None):
            fprz_lines = fprz_sheet.row_count()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_1aiynse1', error, False)
    finally: 
        rgv.set_values({"fprz_lines": fprz_lines})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_1aiynse1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel的行数', 'id':'canvas-node-_1aiynse1', 'time':block_start_time, 'error': error, 'description':r'''获取 fprz_sheet Sheet页的行数''', 'success':node_success_flag, 'variables':{"fprz_lines": str(fprz_lines),"fprz_sheet": str(fprz_sheet)}})
        if (error is not None):
            sys.exit(1)