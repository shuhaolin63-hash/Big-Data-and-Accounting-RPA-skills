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
    # wycx_lines
    rgv.init_value("wycx_lines", None)
    wycx_lines = rgv.get_value("wycx_lines")
    # wy_win
    rgv.init_value("wy_win", None)
    wy_win = rgv.get_value("wy_win")
    # bankkey
    rgv.init_value("bankkey", r"123456")
    bankkey = rgv.get_value("bankkey")
    # tsk_value
    rgv.init_value("tsk_value", r"")
    tsk_value = rgv.get_value("tsk_value")
    # wy_excel
    rgv.init_value("wy_excel", None)
    wy_excel = rgv.get_value("wy_excel")
    # wy_excel_path
    rgv.init_value("wy_excel_path", r"C:\\RPADATA\\收款查询业务数据表.xls")
    wy_excel_path = rgv.get_value("wy_excel_path")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # bank_web
    rgv.init_value("bank_web", None)
    bank_web = rgv.get_value("bank_web")
    # u
    rgv.init_value("u", None)
    u = rgv.get_value("u")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # save_as_dialog
    rgv.init_value("save_as_dialog", None)
    save_as_dialog = rgv.get_value("save_as_dialog")
    # account_web
    rgv.init_value("account_web", None)
    account_web = rgv.get_value("account_web")
    # wycx_sheet
    rgv.init_value("wycx_sheet", None)
    wycx_sheet = rgv.get_value("wycx_sheet")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_ejgv7wqt')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles("机器人正在查询第"+str(u-1)+"笔收款……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ejgv7wqt', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ejgv7wqt')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_ejgv7wqt', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在查询第"+str(u-1)+"笔收款……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_5vgb56qk')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="账户管理", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_5vgb56qk', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_5vgb56qk')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_5vgb56qk', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 账户管理''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_1wczv0d4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="明细查询", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_1wczv0d4', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_1wczv0d4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_1wczv0d4', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 明细查询''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_l276l9ke')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            pyperclip.copy(data[3])                                                                         
            visual.element.input_hotkey("交易日期起始值输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l276l9ke', error, False)
    finally: 
        if node_success_flag == True:
            sleep(0.5)
            Debug_Block_Success('canvas-node-_l276l9ke')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_l276l9ke', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 交易日期起始值输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 通过剪贴方式输入（网页）
    try:
        Debug_Block_Start('canvas-node-_l276l9kf')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            pyperclip.copy(data[3])                                                                         
            visual.element.input_hotkey("交易日期终止值输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l276l9kf', error, False)
    finally: 
        if node_success_flag == True:
            sleep(0.5)
            Debug_Block_Success('canvas-node-_l276l9kf')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_l276l9kf', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 交易日期终止值输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_sg5nv5jd')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="对方账号输入框", value=data[2], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_sg5nv5jd', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_sg5nv5jd')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_sg5nv5jd', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 对方账号输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_e39q8kct')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="交易金额起始值输入框", value=data[4], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_e39q8kct', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_e39q8kct')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_e39q8kct', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 交易金额起始值输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_7ir83xab')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bank_web is not None: 
            visual.element.input(element="交易金额终止值输入框", value=data[4], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_7ir83xab', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_7ir83xab')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_7ir83xab', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 交易金额终止值输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_1r63476s')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="转入", elem_type="Chrome", click_type="left_once", simulate=False, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_1r63476s', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_1r63476s')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_1r63476s', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 转入''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_oxw4dti1')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="查询", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_oxw4dti1', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_oxw4dti1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_oxw4dti1', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 查询''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
        if (error is not None):
            sys.exit(1)
    # 写入Excel单元格
    try:
        Debug_Block_Start('canvas-node-_kwda87qx')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if wycx_sheet is not None:
            region= r"G" + str(1)                               
            wycx_sheet.write(region, r"到账情况", start_row=1, start_col='A', max=1000)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwda87qx', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwda87qx')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel单元格', 'id':'canvas-node-_kwda87qx', 'time':block_start_time, 'error': error, 'description':r'''在 wycx_sheet Sheet页的 G 1 单元写入 "到账情况"  ''', 'success':node_success_flag, 'variables':{"wycx_sheet": str(wycx_sheet)}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_kwda87qt')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_nid6u0yw')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="回单", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=5)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_nid6u0yw', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_nid6u0yw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_nid6u0yw', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 回单''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_5vsp8d6l')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_sq169b5b')
                        node_success_flag = True
                        sleep(1)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        save_as_dialog = visual.window.catch(r"另存为", mode="substr", process_name="", class_name="", timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_sq169b5b', error, False)
                    finally: 
                        rgv.set_values({"save_as_dialog": save_as_dialog})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_sq169b5b')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_sq169b5b', 'time':block_start_time, 'error': error, 'description':r'''根据 "另存为" 查找打开的窗口标题，将查找到的窗口对象赋值给 save_as_dialog''', 'success':node_success_flag, 'variables':{"save_as_dialog": str(save_as_dialog)}})
                        if (error is not None):
                            sys.exit(1)
                    # 获取当前时间&日期
                    try:
                        Debug_Block_Start('canvas-node-_cvb4zlts')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_cvb4zlts', error, False)
                    finally: 
                        rgv.set_values({"v_time": v_time})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_cvb4zlts')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_cvb4zlts', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
                        if (error is not None):
                            sys.exit(1)
                    # 通过剪贴方式输入（窗口）
                    try:
                        Debug_Block_Start('canvas-node-_co2sfy08')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if save_as_dialog is not None: 
                            pyperclip.copy(os.path.join("C:\RPADATA", (data[3]+data[1]+'回单'+data[4]+'元'+str(v_time)+'.pdf')))                                                                         
                            visual.element.input_hotkey("文件名输入框", "VK_CONTROL|V", elem_type="WinUI", replace=True, index=1, window=save_as_dialog, timeout=20)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_co2sfy08', error, False)
                    finally: 
                        if node_success_flag == True:
                            sleep(0.5)
                            Debug_Block_Success('canvas-node-_co2sfy08')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（窗口）', 'id':'canvas-node-_co2sfy08', 'time':block_start_time, 'error': error, 'description':r'''在 save_as_dialog 中，通过剪贴方式在 文件名输入框 内填写 os.path.join("C:\RPADATA", (data[3]+data[1]+'回单'+data[4]+'元'+str(v_time)+'.pdf'))''', 'success':node_success_flag, 'variables':{"save_as_dialog": str(save_as_dialog)}})
                        if (error is not None):
                            sys.exit(1)
                    # 输入热键
                    try:
                        Debug_Block_Start('canvas-node-_cdt18nlq')
                        node_success_flag = True
                        sleep(1)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.ui.win32.send_key(r"!{s}")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_cdt18nlq', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_cdt18nlq')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_cdt18nlq', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{s}"''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 出现字幕
                    try:
                        Debug_Block_Start('canvas-node-_kw1o6ran')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.system.dialog.subtitles(r"下载成功！如需下载至指定路径，请您开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！", fontColor='255,255,0,0', fontSize=size_changer)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kw1o6ran', error, False)
                    finally: 
                        if node_success_flag == True:
                            sleep(3)
                            Debug_Block_Success('canvas-node-_kw1o6ran')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kw1o6ran', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "下载成功！如需下载至指定路径，请您开启Chrome浏览器的“下载前询问每个文件的保存位置”功能！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_5vsp8d6l', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_5vsp8d6l')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_5vsp8d6l', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            # 写入Excel单元格
            try:
                Debug_Block_Start('canvas-node-_kwda87r2')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if wycx_sheet is not None:
                    region= r"G" + str(u)                               
                    wycx_sheet.write(region, r"已到账", start_row=1, start_col='A', max=1000)
                    wycx_sheet.excel.save(file=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwda87r2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwda87r2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel单元格', 'id':'canvas-node-_kwda87r2', 'time':block_start_time, 'error': error, 'description':r'''在 wycx_sheet Sheet页的 G  u 单元写入 "已到账"  并保存''', 'success':node_success_flag, 'variables':{"u": str(u),"wycx_sheet": str(wycx_sheet)}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kwda87r4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles("第"+str(u-1)+"笔收款未到账，请核实！", fontColor='255,255,0,0', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwda87r4', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(4)
                    Debug_Block_Success('canvas-node-_kwda87r4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kwda87r4', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "第"+str(u-1)+"笔收款未到账，请核实！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 写入Excel单元格
            try:
                Debug_Block_Start('canvas-node-_kwda87r3')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if wycx_sheet is not None:
                    region= r"G" + str(u)                               
                    wycx_sheet.write(region, r"未到账", start_row=1, start_col='A', max=1000)
                    wycx_sheet.excel.save(file=None)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kwda87r3', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kwda87r3')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel单元格', 'id':'canvas-node-_kwda87r3', 'time':block_start_time, 'error': error, 'description':r'''在 wycx_sheet Sheet页的 G  u 单元写入 "未到账"  并保存''', 'success':node_success_flag, 'variables':{"u": str(u),"wycx_sheet": str(wycx_sheet)}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwda87qt', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwda87qt')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_kwda87qt', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("data", data)
    rgv.set_value("wycx_lines", wycx_lines)
    rgv.set_value("wy_win", wy_win)
    rgv.set_value("bankkey", bankkey)
    rgv.set_value("tsk_value", tsk_value)
    rgv.set_value("wy_excel", wy_excel)
    rgv.set_value("wy_excel_path", wy_excel_path)
    rgv.set_value("username", username)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("u", u)
    rgv.set_value("v_time", v_time)
    rgv.set_value("save_as_dialog", save_as_dialog)
    rgv.set_value("account_web", account_web)
    rgv.set_value("wycx_sheet", wycx_sheet)
    rgv.set_value("size_changer", size_changer)
    rgv.set_value("password", password)
    rgv.set_value("cookies", cookies)