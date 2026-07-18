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
        Debug_Block_Start('canvas-node-_l4m1ucji')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l4m1ucji', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l4m1ucji')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_l4m1ucjj')
        node_success_flag = True
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l4m1ucjj', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l4m1ucjj')
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_l4m1ucjk')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l4m1ucjk', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_l4m1ucjk')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_l4m1ucjl')
        node_success_flag = True
        Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l4m1ucjl', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l4m1ucjl')
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_l4m1ucjm')
        node_success_flag = True
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l4m1ucjm', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l4m1ucjm')