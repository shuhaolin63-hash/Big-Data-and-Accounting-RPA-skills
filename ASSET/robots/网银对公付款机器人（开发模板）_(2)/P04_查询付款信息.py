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
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_mpy3pbai')
        node_success_flag = True
        try:
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbi')
                node_success_flag = True
                visual.element.click(element="账户管理", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbi', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbi')
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbj')
                node_success_flag = True
                visual.element.click(element="明细查询", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbj', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbj')
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbk')
                node_success_flag = True
                if bank_web is not None: 
                    visual.element.input(element="交易日期起始值输入框", value=data[13], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbk', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbk')
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbl')
                node_success_flag = True
                if bank_web is not None: 
                    visual.element.input(element="交易日期终止值输入框", value=data[13], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbl', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbl')
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbm')
                node_success_flag = True
                if bank_web is not None: 
                    visual.element.input(element="对方账号输入框", value=data[4], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbm', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbm')
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbn')
                node_success_flag = True
                if bank_web is not None: 
                    visual.element.input(element="交易金额起始值输入框", value=data[6], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbn', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbn')
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbo')
                node_success_flag = True
                if bank_web is not None: 
                    visual.element.input(element="交易金额终止值输入框", value=data[6], elem_type="Chrome", index=1, window=bank_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbo', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbo')
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbp')
                node_success_flag = True
                visual.element.click(element="转出", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbp', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbp')
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbq')
                node_success_flag = True
                visual.element.click(element="查询", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbq', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbq')
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbw')
                node_success_flag = True
                visual.element.click(element="回单", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=bank_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbw', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbw')
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_mpy3pbbx')
                node_success_flag = True
                sleep(3)
                rpa.ui.win32.send_key(r"!{s}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbbx', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbbx')
            pass
        except:
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbai', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbai')
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)