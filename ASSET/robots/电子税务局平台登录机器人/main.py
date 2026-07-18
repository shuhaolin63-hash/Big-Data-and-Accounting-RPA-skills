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
import END


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明自动创建变量
    v_web_obj_1 = None
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mnfgdi54')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        START.start()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mnfgdi54', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mnfgdi54')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mnfgdi54', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mnfgdi55')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 打开新网页
            try:
                Debug_Block_Start('canvas-node-_mnfgdi50')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                v_web_obj_1 = visual.browser.create("chrome", r"https://fz.chinaive.com/dzswj/?username",  wait=True, visible=True, timeout=100)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mnfgdi50', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mnfgdi50')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_mnfgdi50', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问"https://fz.chinaive.com/dzswj/?username"，将浏览器对象赋值给 v_web_obj_1''', 'success':node_success_flag, 'variables':{"v_web_obj_1": str(v_web_obj_1)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mnfgdi51')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="登录头像按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=v_web_obj_1, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mnfgdi51', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mnfgdi51')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mnfgdi51', 'time':block_start_time, 'error': error, 'description':r'''在 v_web_obj_1 网页中，鼠标 左键单击 登录头像按钮''', 'success':node_success_flag, 'variables':{"v_web_obj_1": str(v_web_obj_1)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mnfgdi52')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if v_web_obj_1 is not None: 
                    visual.element.input(element="密码输入框", value=r"password_placeholder", elem_type="Chrome", index=1, window=v_web_obj_1, simulate=False, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mnfgdi52', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mnfgdi52')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mnfgdi52', 'time':block_start_time, 'error': error, 'description':r'''在 v_web_obj_1 网页 中，在 密码输入框 内填写 "password_placeholder"''', 'success':node_success_flag, 'variables':{"v_web_obj_1": str(v_web_obj_1)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mnfgdi53')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="登录按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=v_web_obj_1, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mnfgdi53', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mnfgdi53')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mnfgdi53', 'time':block_start_time, 'error': error, 'description':r'''在 v_web_obj_1 网页中，鼠标 左键单击 登录按钮''', 'success':node_success_flag, 'variables':{"v_web_obj_1": str(v_web_obj_1)}})
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
        Debug_Block_Error('canvas-node-_mnfgdi55', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mnfgdi55')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_mnfgdi55', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mnfgdi59')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        END.start()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mnfgdi59', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mnfgdi59')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mnfgdi59', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)