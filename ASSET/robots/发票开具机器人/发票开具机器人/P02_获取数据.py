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
    # 获取Excel行的值
    try:
        Debug_Block_Start('canvas-node-_lofgjgb2')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpkj_sheet is not None:
            data = fpkj_sheet.read(str(i),only_visible = True,max = 1000)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgb2', error, False)
    finally: 
        rgv.set_values({"data": data})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgb2')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel行的值', 'id':'canvas-node-_lofgjgb2', 'time':block_start_time, 'error': error, 'description':r'''获取 fpkj_sheet Sheet页的 i 行的值，并将结果赋值给 data''', 'success':node_success_flag, 'variables':{"i": str(i),"data": str(data),"fpkj_sheet": str(fpkj_sheet)}})
        if (error is not None):
            sys.exit(1)
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