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
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_fg92xdfl')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人正在进行工行网银逐笔支付……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_fg92xdfl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_fg92xdfl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_fg92xdfl', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在进行工行网银逐笔支付……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 条件分支
    try:
        Debug_Block_Start('canvas-node-_z95d6b8u')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if (data[1]=='对公'):
            pass
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_uht15gh1')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="付款业务", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_uht15gh1', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_uht15gh1')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_uht15gh1', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 付款业务''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_i05gy29x')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="网上汇款", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_i05gy29x', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_i05gy29x')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_i05gy29x', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 网上汇款''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_v7bmp7b4')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="转账汇款", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_v7bmp7b4', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_v7bmp7b4')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_v7bmp7b4', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 转账汇款''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_39dw6hd8')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="逐笔支付", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_39dw6hd8', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_39dw6hd8')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_39dw6hd8', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 逐笔支付''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_pq8f61fp')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款单位输入框", value=data[2], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_pq8f61fp', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_pq8f61fp')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_pq8f61fp', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款单位输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_im9c00vf')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款账号输入框", value=data[4], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_im9c00vf', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_im9c00vf')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_im9c00vf', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款账号输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_3172klcy')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="开户行输入框", value=data[3], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_3172klcy', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_3172klcy')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_3172klcy', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 开户行输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_24inrsxl')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="汇款金额输入框", value=data[6], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_24inrsxl', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_24inrsxl')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_24inrsxl', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 汇款金额输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（网页）
            try:
                Debug_Block_Start('canvas-node-_kzz0upyk')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    pyperclip.copy(data[7])                                                                         
                    visual.element.input_hotkey("汇款用途输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kzz0upyk', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(0.5)
                    Debug_Block_Success('canvas-node-_kzz0upyk')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_kzz0upyk', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 汇款用途输入框 内填写 data[7]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_40i6f8d7')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="提交", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_40i6f8d7', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_40i6f8d7')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_40i6f8d7', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 提交''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
        else:
            pass
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_jopr4c73')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="付款业务", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_jopr4c73', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_jopr4c73')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_jopr4c73', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 付款业务''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_oalq9pld')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="企业财务室", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_oalq9pld', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_oalq9pld')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_oalq9pld', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 企业财务室''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_8bk87pkf')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="企业财务室逐笔支付", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_8bk87pkf', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_8bk87pkf')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_8bk87pkf', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 企业财务室逐笔支付''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_jcs65bpq')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款人输入框", value=data[2], elem_type="Chrome", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_jcs65bpq', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_jcs65bpq')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_jcs65bpq', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款人输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_y0ba21yk')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款账号输入框", value=data[4], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_y0ba21yk', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_y0ba21yk')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_y0ba21yk', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款账号输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_ri62y5pl')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="汇款金额输入框", value=data[6], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_ri62y5pl', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_ri62y5pl')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_ri62y5pl', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 汇款金额输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_jd2n0zcr')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="汇款用途输入框", value=data[7], elem_type="IE", index=1, window=bank_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_jd2n0zcr', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_jd2n0zcr')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_jd2n0zcr', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 汇款用途输入框 内填写 data[7]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（网页）
            try:
                Debug_Block_Start('canvas-node-_kzz0upyl')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    pyperclip.copy(data[7])                                                                         
                    visual.element.input_hotkey("汇款用途输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kzz0upyl', error, False)
            finally: 
                if node_success_flag == True:
                    sleep(0.5)
                    Debug_Block_Success('canvas-node-_kzz0upyl')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_kzz0upyl', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 汇款用途输入框 内填写 data[7]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_escaqjt6')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="提交", elem_type="IE", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_escaqjt6', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_escaqjt6')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_escaqjt6', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 提交''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_z95d6b8u', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_z95d6b8u')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'条件分支', 'id':'canvas-node-_z95d6b8u', 'time':block_start_time, 'error': error, 'description':r'''if-else条件分支''', 'success':node_success_flag, 'variables':{}})