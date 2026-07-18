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
from rpa.sdk import logger


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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_logsxyx4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人已完成发票开具业务，正在退出电子税务局仿真平台……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyx4', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyx4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_logsxyx4', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人已完成发票开具业务，正在退出电子税务局仿真平台……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_loghnt6c')
        node_success_flag = True
        sleep(3)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="退出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_loghnt6c', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_loghnt6c')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_loghnt6c', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，鼠标 左键单击 退出''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 关闭网页
    try:
        Debug_Block_Start('canvas-node-_loghnt6d')
        node_success_flag = True
        sleep(2)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if swj_web is not None:
            swj_web.close()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_loghnt6d', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_loghnt6d')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭网页', 'id':'canvas-node-_loghnt6d', 'time':block_start_time, 'error': error, 'description':r'''关闭 swj_web 网页''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_logk759x')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_logk75a1')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_logk75a5')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fpkj_win = visual.window.catch(os.path.basename(fpkj_excel_path).split('.')[0], mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_logk75a5', error, False)
                    finally: 
                        rgv.set_values({"fpkj_win": fpkj_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_logk75a5')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_logk75a5', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(fpkj_excel_path).split('.')[0] 查找打开的窗口标题，将查找到的窗口对象赋值给 fpkj_win''', 'success':node_success_flag, 'variables':{"fpkj_win": str(fpkj_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_logloagm')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fpkj_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_logloagm', error, False)
                    finally: 
                        rgv.set_values({"fpkj_win": fpkj_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_logloagm')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_logloagm', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 fpkj_win''', 'success':node_success_flag, 'variables':{"fpkj_win": str(fpkj_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logk75a1', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logk75a1')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_logk75a1', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_logloago')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fpkj_win is not None: fpkj_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logloago', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logloago')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_logloago', 'time':block_start_time, 'error': error, 'description':r'''激活 fpkj_win 窗口''', 'success':node_success_flag, 'variables':{"fpkj_win": str(fpkj_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_logloagp')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logloagp', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logloagp')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_logloagp', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 记录日志
            try:
                Debug_Block_Start('canvas-node-_logloagn')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger.info(r''' ''')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logloagn', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logloagn')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_logloagn', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logk759x', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logk759x')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_logk759x', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("fpkj_excel", fpkj_excel)
    rgv.set_value("fpkj_sheet", fpkj_sheet)
    rgv.set_value("swj_web", swj_web)
    rgv.set_value("lines", lines)
    rgv.set_value("i", i)
    rgv.set_value("data", data)
    rgv.set_value("kp_web", kp_web)
    rgv.set_value("lzfp_web", lzfp_web)
    rgv.set_value("fpkj_win", fpkj_win)
    rgv.set_value("username", username)
    rgv.set_value("password", password)
    rgv.set_value("fpkj_excel_path", fpkj_excel_path)