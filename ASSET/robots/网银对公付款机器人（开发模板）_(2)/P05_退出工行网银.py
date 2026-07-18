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


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明全局变量
    # wyfk_sheet
    rgv.init_value("wyfk_sheet", None)
    wyfk_sheet = rgv.get_value("wyfk_sheet")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # 申明自动创建变量
    v_win_obj_1 = None
    wyfk_win = None
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mpy3pbas')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbby')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="退出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbby', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbby')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbby', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 退出''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbz')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"^{w}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbz', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbz')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mpy3pbbz', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "^{w}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 获取窗口
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc0')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                wyfk_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc0', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc0')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_mpy3pbc0', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 wyfk_win''', 'success':node_success_flag, 'variables':{"wyfk_win": str(wyfk_win)}})
                if (error is not None):
                    sys.exit(1)
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc1')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if wyfk_win is not None: wyfk_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc1', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc1')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_mpy3pbc1', 'time':block_start_time, 'error': error, 'description':r'''激活 wyfk_win 窗口''', 'success':node_success_flag, 'variables':{"wyfk_win": str(wyfk_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc2')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_mpy3pbc2', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbas', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbas')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_mpy3pbas', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)