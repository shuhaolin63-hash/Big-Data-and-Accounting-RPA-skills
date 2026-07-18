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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x16gv')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x16gv', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9x16gv')
    # 打开新网页
    try:
        Debug_Block_Start('canvas-node-_mpyrkxgn')
        node_success_flag = True
        bank_web = visual.browser.create("chrome", r"https://fz.chinaive.com/wsyh/?username=zhanhunliren",  wait=True, visible=True, timeout=100)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpyrkxgn', error, True)
        sys.exit(1)
    finally:
        rgv.set_values({"bank_web": bank_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpyrkxgn')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_ky9vu1ek')
        node_success_flag = True
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9vu1ek', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9vu1ek')
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x16gw')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=36)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x16gw', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            sleep(3)
            Debug_Block_Success('canvas-node-_ky9x16gw')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_ky9vu1em')
        node_success_flag = True
        Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9vu1em', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9vu1em')
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_ky9x16gx')
        node_success_flag = True
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ky9x16gx', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ky9x16gx')
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)