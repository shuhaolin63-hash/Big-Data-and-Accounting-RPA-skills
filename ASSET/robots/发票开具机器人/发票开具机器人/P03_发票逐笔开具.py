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
    # 申明自动创建变量
    lcw_win = None
    v_time = r""
    v_notice_alert_value_1 = r""
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_logloah1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles("机器人正在开具第"+str(int(i)-1)+"笔发票……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloah1', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloah1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_logloah1', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在开具第"+str(int(i)-1)+"笔发票……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgb9')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="开票业务", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=swj_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgb9', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgb9')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgb9', 'time':block_start_time, 'error': error, 'description':r'''在 swj_web 网页中，鼠标 左键单击 开票业务''', 'success':node_success_flag, 'variables':{"swj_web": str(swj_web)}})
        if (error is not None):
            sys.exit(1)
    # 获取已打开网页
    try:
        Debug_Block_Start('canvas-node-_lofgjgba')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        kp_web = visual.browser.catch("chrome", r"https://fz.chinaive.com/dzswj/billingService", mode="url", pattern="contain", timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgba', error, False)
    finally: 
        rgv.set_values({"kp_web": kp_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgba')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取已打开网页', 'id':'canvas-node-_lofgjgba', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中，根据 URL 查找打开的网页 ，将查找到的浏览器对象赋值给 kp_web''', 'success':node_success_flag, 'variables':{"kp_web": str(kp_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbb')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="蓝字发票开具", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=kp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbb', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgbb')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgbb', 'time':block_start_time, 'error': error, 'description':r'''在 kp_web 网页中，鼠标 左键单击 蓝字发票开具''', 'success':node_success_flag, 'variables':{"kp_web": str(kp_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbc')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="立即开票", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=kp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbc', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgbc')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgbc', 'time':block_start_time, 'error': error, 'description':r'''在 kp_web 网页中，鼠标 左键单击 立即开票''', 'success':node_success_flag, 'variables':{"kp_web": str(kp_web)}})
        if (error is not None):
            sys.exit(1)
    # 设置下拉框选项（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbd')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.set_select_item("票类下拉框", elem_type="Chrome", option_mode="text", item_index=1, item_text=data[1], text_match_mode='match', index=1, window=kp_web, timeout=20)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbd', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgbd')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置下拉框选项（网页）', 'id':'canvas-node-_lofgjgbd', 'time':block_start_time, 'error': error, 'description':r'''在 kp_web 网页中，点击 票类下拉框 ，上传  文件''', 'success':node_success_flag, 'variables':{"kp_web": str(kp_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbe')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="确定", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=kp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbe', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgbe')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgbe', 'time':block_start_time, 'error': error, 'description':r'''在 kp_web 网页中，鼠标 左键单击 确定''', 'success':node_success_flag, 'variables':{"kp_web": str(kp_web)}})
        if (error is not None):
            sys.exit(1)
    # 获取已打开网页
    try:
        Debug_Block_Start('canvas-node-_lofgjgbm')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        lzfp_web = visual.browser.catch("chrome", r"https://fz.chinaive.com/dzswj/immediateDraftPage?parm", mode="url", pattern="contain", timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbm', error, False)
    finally: 
        rgv.set_values({"lzfp_web": lzfp_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgbm')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取已打开网页', 'id':'canvas-node-_lofgjgbm', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中，根据 URL 查找打开的网页 ，将查找到的浏览器对象赋值给 lzfp_web''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lqxeuxqx')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[2])                                                                         
            visual.element.input_hotkey("购买方名称输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lqxeuxqx', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lqxeuxqx')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lqxeuxqx', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 购买方名称输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_loghnt6e')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[3])                                                                         
            visual.element.input_hotkey("购买方纳税人识别号输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_loghnt6e', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_loghnt6e')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_loghnt6e', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 购买方纳税人识别号输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbp')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[4])                                                                         
            visual.element.input_hotkey("购买方地址输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbp', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lofgjgbp')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lofgjgbp', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 购买方地址输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbq')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[5])                                                                         
            visual.element.input_hotkey("电话输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbq', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lofgjgbq')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lofgjgbq', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 电话输入框 内填写 data[5]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lqxeuxqy')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[6])                                                                         
            visual.element.input_hotkey("购方开户银行输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lqxeuxqy', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lqxeuxqy')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lqxeuxqy', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 购方开户银行输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lqxeuxqz')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[7])                                                                         
            visual.element.input_hotkey("银行账号输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lqxeuxqz', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lqxeuxqz')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lqxeuxqz', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 银行账号输入框 内填写 data[7]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbv')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[8])                                                                         
            visual.element.input_hotkey("项目名称输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbv', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lofgjgbv')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lofgjgbv', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 项目名称输入框 内填写 data[8]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgbx')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            pyperclip.copy(data[9])                                                                         
            visual.element.input_hotkey("规格型号输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgbx', error, False)
    finally: 
        if node_success_flag == True:
            sleep(1)
            Debug_Block_Success('canvas-node-_lofgjgbx')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_lofgjgbx', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，通过剪贴方式在 规格型号输入框 内填写 data[9]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgby')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            visual.element.input(element="单位输入框", value=data[10], elem_type="Chrome", index=1, window=lzfp_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgby', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgby')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_lofgjgby', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页 中，在 单位输入框 内填写 data[10]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgc9')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            visual.element.input(element="数量输入框", value=data[11], elem_type="Chrome", index=1, window=lzfp_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgc9', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgc9')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_lofgjgc9', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页 中，在 数量输入框 内填写 data[11]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgca')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if lzfp_web is not None: 
            visual.element.input(element="单价输入框", value=data[12], elem_type="Chrome", index=1, window=lzfp_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgca', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgca')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_lofgjgca', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页 中，在 单价输入框 内填写 data[12]''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_loghnt6h')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"{tab}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_loghnt6h', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_loghnt6h')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_loghnt6h', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "{tab}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_lsu6cqqi')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"{tab}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lsu6cqqi', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lsu6cqqi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lsu6cqqi', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "{tab}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_loghnt6i')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key({'13%':'{down}',
        '9%':'{down 2}',
        '6%':'{down 3}',
        '5%':'{down 4}',
        '3%':'{down 5}',
        '减按1.5%计算':'{down 6}',
        '1%':'{down 7}',
        '免税':'{down 8}'
        }
        [data[14]])
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_loghnt6i', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_loghnt6i')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_loghnt6i', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 {'13%':'{down}',
    '9%':'{down 2}',
    '6%':'{down 3}',
    '5%':'{down 4}',
    '3%':'{down 5}',
    '减按1.5%计算':'{down 6}',
    '1%':'{down 7}',
    '免税':'{down 8}'
    }
    [data[14]]''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_lsu6cqqj')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"{tab}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lsu6cqqj', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lsu6cqqj')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lsu6cqqj', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "{tab}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lofgjgc2')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="发票开具按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgc2', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgc2')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lofgjgc2', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，鼠标 左键单击 发票开具按钮''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_lqxeuxqv')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="发票下载PDF", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=lzfp_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lqxeuxqv', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lqxeuxqv')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_lqxeuxqv', 'time':block_start_time, 'error': error, 'description':r'''在 lzfp_web 网页中，鼠标 左键单击 发票下载PDF''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
        if (error is not None):
            sys.exit(1)
    # 获取当前时间和日期
    try:
        Debug_Block_Start('canvas-node-_lofgjgc5')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_lofgjgc5', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_lofgjgc5')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间和日期', 'id':'canvas-node-_lofgjgc5', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_logloah2')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 获取窗口
            try:
                Debug_Block_Start('canvas-node-_lofgjgc3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                lcw_win = visual.window.catch(r"另存为", mode="substr", process_name="", class_name="", timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgc3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgc3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_lofgjgc3', 'time':block_start_time, 'error': error, 'description':r'''根据 "另存为" 查找打开的窗口标题，将查找到的窗口对象赋值给 lcw_win''', 'success':node_success_flag, 'variables':{"lcw_win": str(lcw_win)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（窗口）
            try:
                Debug_Block_Start('canvas-node-_lofgjgc4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if lcw_win is not None: 
                    pyperclip.copy(os.path.join("C:\RPADATA",(data[2]+data[13]+'元'+str(v_time))))                                                                         
                    visual.element.input_hotkey("文件名输入框", "VK_CONTROL|V", elem_type="WinUI", replace=True, index=1, window=lcw_win, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgc4', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(1)
                    Debug_Block_Success('canvas-node-_lofgjgc4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（窗口）', 'id':'canvas-node-_lofgjgc4', 'time':block_start_time, 'error': error, 'description':r'''在 lcw_win 中，通过剪贴方式在 文件名输入框 内填写 os.path.join("C:\RPADATA",(data[2]+data[13]+'元'+str(v_time)))''', 'success':node_success_flag, 'variables':{"lcw_win": str(lcw_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_lqxeuxqw')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{s}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lqxeuxqw', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lqxeuxqw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lqxeuxqw', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{s}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 关闭网页
            try:
                Debug_Block_Start('canvas-node-_loghnt66')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if lzfp_web is not None:
                    lzfp_web.close()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_loghnt66', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_loghnt66')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'关闭网页', 'id':'canvas-node-_loghnt66', 'time':block_start_time, 'error': error, 'description':r'''关闭 lzfp_web 网页''', 'success':node_success_flag, 'variables':{"lzfp_web": str(lzfp_web)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_logsxyx3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"下载成功！如需下载至指定路径，请开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logsxyx3', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(5)
                    Debug_Block_Success('canvas-node-_logsxyx3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_logsxyx3', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "下载成功！如需下载至指定路径，请开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloah2', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloah2')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_logloah2', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
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