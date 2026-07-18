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
    # 申明自动创建变量
    v_excel_obj_2 = None
    v_file_path_2 = r""
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mpy3pba8')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpyrkxgm')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="付款业务", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpyrkxgm', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpyrkxgm')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpyrkxgm', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 付款业务''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbb9')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="网上汇款", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbb9', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbb9')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbb9', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 网上汇款''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbba')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="转账汇款", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbba', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbba')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbba', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 转账汇款''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbb')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="逐笔支付", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbb', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbb')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbbb', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 逐笔支付''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbc')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款单位输入框", value=data[2], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbc', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbc')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mpy3pbbc', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款单位输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbd')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="收款账号输入框", value=data[4], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbd', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbd')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mpy3pbbd', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 收款账号输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbe')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="开户行输入框", value=data[3], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbe', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbe')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mpy3pbbe', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 开户行输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbf')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    visual.element.input(element="汇款金额输入框", value=data[6], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbf', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbf')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_mpy3pbbf', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页 中，在 汇款金额输入框 内填写 data[6]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 通过剪贴方式输入（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbg')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if bank_web is not None: 
                    pyperclip.copy(data[7])                                                                         
                    visual.element.input_hotkey("汇款用途输入框", "VK_CONTROL|V", elem_type="Chrome", replace=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbg', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbg')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_mpy3pbbg', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，通过剪贴方式在 汇款用途输入框 内填写 data[7]''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbh')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="提交", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbh', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbh')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_mpy3pbbh', 'time':block_start_time, 'error': error, 'description':r'''在 bank_web 网页中，鼠标 左键单击 提交''', 'success':node_success_flag, 'variables':{"bank_web": str(bank_web)}})
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
        Debug_Block_Error('canvas-node-_mpy3pba8', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pba8')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_mpy3pba8', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)