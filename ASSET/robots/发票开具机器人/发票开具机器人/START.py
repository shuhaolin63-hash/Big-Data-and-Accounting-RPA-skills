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
        Debug_Block_Start('canvas-node-_logsxyx9')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人开始运行，请输入实践平台账号及密码！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyx9', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyx9')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_logsxyxb')
        node_success_flag = True
        cookies, username, password = Assess.start('auto_auth')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxb', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxb')
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_logsxyxc')
        node_success_flag = True
        rgv.set_value("username", username)
        username = username
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxc', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxc')
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_logsxyxd')
        node_success_flag = True
        rgv.set_value("password", password)
        password = password
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxd', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxd')
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_logsxyxe')
        node_success_flag = True
        rpa.system.dialog.subtitles(r"机器人正在自动识别测评任务！", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxe', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxe')
    # 调用自定义脚本
    try:
        Debug_Block_Start('canvas-node-_logsxyxf')
        node_success_flag = True
        path = Assess.start('auto_start')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxf', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxf')
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_logsxyxg')
        node_success_flag = True
        rgv.set_value("fpkj_excel_path", path or fpkj_excel_path)
        fpkj_excel_path = path or fpkj_excel_path
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxg', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxg')
    # 关闭字幕
    try:
        Debug_Block_Start('canvas-node-_logsxyxh')
        node_success_flag = True
        rpa.system.dialog.subtitles_disappear()
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logsxyxh', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logsxyxh')