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
    # data
    rgv.init_value("data", None)
    data = rgv.get_value("data")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # bankkey
    rgv.init_value("bankkey", r"123456")
    bankkey = rgv.get_value("bankkey")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # wy_excel
    rgv.init_value("wy_excel", None)
    wy_excel = rgv.get_value("wy_excel")
    # wy_excel_path
    rgv.init_value("wy_excel_path", r"C:\\RPADATA\网银付款业务数据表.xls")
    wy_excel_path = rgv.get_value("wy_excel_path")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # username
    rgv.init_value("username", r" ")
    username = rgv.get_value("username")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # wyfk_sheet
    rgv.init_value("wyfk_sheet", None)
    wyfk_sheet = rgv.get_value("wyfk_sheet")
    # wyfk_lines
    rgv.init_value("wyfk_lines", None)
    wyfk_lines = rgv.get_value("wyfk_lines")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # Running_state
    rgv.init_value("Running_state", r"")
    Running_state = rgv.get_value("Running_state")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # 申明自动创建变量
    date = r""
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_xs3dzdfs')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在查询付款回单……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_xs3dzdfs', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_xs3dzdfs')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_xs3dzdfs', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在查询付款回单……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_pzjh3mu0')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="账户管理", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_pzjh3mu0', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_pzjh3mu0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_pzjh3mu0', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 账户管理''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_eyq1j8wp')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="明细查询", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_eyq1j8wp', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_eyq1j8wp')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_eyq1j8wp', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 明细查询''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 获取当前时间和日期
    try:
        Debug_Block_Start('canvas-node-_kwd8cmvg')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        date = datetime.datetime.now().strftime(r'%Y-%m-%d'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwd8cmvg', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwd8cmvg')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间和日期', 'id':'canvas-node-_kwd8cmvg', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 date''', 'success':node_success_flag, 'variables':{"date": str(date)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_l276bzu0')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            pyperclip.copy(date)                                                                         
            visual.element.input_hotkey("交易日期起始值输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l276bzu0', error, False)
    finally: 
        if node_success_flag == True:
            sleep(0.5)
            Debug_Block_Success('canvas-node-_l276bzu0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_l276bzu0', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 交易日期起始值输入框 内填写 date''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web),"date": str(date)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_l276bzu1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            pyperclip.copy(date)                                                                         
            visual.element.input_hotkey("交易日期终止值输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l276bzu1', error, False)
    finally: 
        if node_success_flag == True:
            sleep(0.5)
            Debug_Block_Success('canvas-node-_l276bzu1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_l276bzu1', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 交易日期终止值输入框 内填写 date''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web),"date": str(date)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_b1nf31qd')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="对方账号输入框", value=data[4], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_b1nf31qd', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_b1nf31qd')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_b1nf31qd', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 对方账号输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_zvh2ywuk')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="交易金额起始值输入框", value=data[6], elem_type="IE", index=1, window=bank_web, simulate=False, replace=False, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_zvh2ywuk', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_zvh2ywuk')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_zvh2ywuk', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 交易金额起始值输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_qo0shg6i')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="交易金额终止值输入框", value=data[6], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_qo0shg6i', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_qo0shg6i')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_qo0shg6i', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 交易金额终止值输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_t7ykg0lg')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="转出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_t7ykg0lg', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_t7ykg0lg')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_t7ykg0lg', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 转出''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_9948lu2v')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="查询", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_9948lu2v', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_9948lu2v')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_9948lu2v', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 查询''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_m7g0cjud')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="回单", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_m7g0cjud', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_m7g0cjud')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_m7g0cjud', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 回单''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_d6tshi6w')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 获取窗口
            try:
                Debug_Block_Start('canvas-node-_or4k3ht8')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                save_as_dialog = visual.window.catch(r"另存为", mode="substr", process_name="", class_name="", timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_or4k3ht8', error, False)
            finally: 
                rgv.set_values({"save_as_dialog": save_as_dialog})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_or4k3ht8')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_or4k3ht8', 'time':block_start_time, 'error': error, 'description':r'''根据 "另存为" 查找打开的窗口标题，将查找到的窗口对象赋值给 save_as_dialog''', 'success':node_success_flag, 'variables':{"save_as_dialog": str(save_as_dialog)}})
                if (error is not None):
                    sys.exit(1)
            # 获取当前时间&日期
            try:
                Debug_Block_Start('canvas-node-_gfkptq93')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_gfkptq93', error, False)
            finally: 
                rgv.set_values({"v_time": v_time})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_gfkptq93')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_gfkptq93', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（窗口）
            try:
                Debug_Block_Start('canvas-node-_lp0z4xtq')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if save_as_dialog is not None: 
                    pyperclip.copy(os.path.join("C:\RPADATA", (date+data[2]+'回单'+data[6]+'元'+str(v_time)+'.pdf')))                                                                         
                    visual.element.input_hotkey("文件名输入框", "VK_CONTROL|V", elem_type="WinUI", replace=True, index=1, window=save_as_dialog, timeout=20)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lp0z4xtq', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(0.5)
                    Debug_Block_Success('canvas-node-_lp0z4xtq')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（窗口）', 'id':'canvas-node-_lp0z4xtq', 'time':block_start_time, 'error': error, 'description':r'''在 save_as_dialog 中，通过剪贴方式在 文件名输入框 内填写 os.path.join("C:\RPADATA", (date+data[2]+'回单'+data[6]+'元'+str(v_time)+'.pdf'))''', 'success':node_success_flag, 'variables':{"save_as_dialog": str(save_as_dialog)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_d7h551i2')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{s}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_d7h551i2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_d7h551i2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_d7h551i2', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{s}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_r54mlq4y')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="欢迎页面", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_r54mlq4y', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_r54mlq4y')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_r54mlq4y', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 欢迎页面''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kvkonlro')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles(r"下载成功！如需下载至指定路径，请开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvkonlro', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(3)
                    Debug_Block_Success('canvas-node-_kvkonlro')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvkonlro', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "下载成功！如需下载至指定路径，请开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_d6tshi6w', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_d6tshi6w')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_d6tshi6w', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})