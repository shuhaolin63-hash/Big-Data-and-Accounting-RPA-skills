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
import Assess


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x3pix')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x3pix', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9x3pix')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_ky9x3pix', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始运行，请输入实践平台账号及密码！"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_ky9uvfp8')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9uvfp8', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9uvfp8')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_ky9uvfp8', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x3piy')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x3piy', error, False)
    finally: 
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_ky9x3piy')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_ky9x3piy', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在自动识别测评任务！"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_ky9uvfpa')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9uvfpa', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9uvfpa')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_ky9uvfpa', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x3piz')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x3piz', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9x3piz')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭字幕', 'id':'canvas-node-_ky9x3piz', 'time':block_start_time, 'error': error, 'description':r'''''', 'success':node_success_flag, 'variables':{}})