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
import START
import P01_登录工行网银
import P02_获取数据
import P03_逐笔付款
import P04_查询付款信息
import P05_退出工行网银
import END


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
    v_notice_alert_value_1 = r""
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mpy3pbc3')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 START 子流程
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("data", data)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        START.start()
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        data = rgv.get_value("data")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbc3', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbc3')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpy3pbc3', 'time':block_start_time, 'error': error, 'description':r'''调用 START 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mq1tusrq')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 P01_登录工行网银 子流程
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("data", data)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        P01_登录工行网银.start()
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        data = rgv.get_value("data")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mq1tusrq', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mq1tusrq')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mq1tusrq', 'time':block_start_time, 'error': error, 'description':r'''调用 P01_登录工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 按照次数循环
    try:
        Debug_Block_Start('canvas-node-_mpy3pbc4')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(int(2), int(4) + 1, int(1)):
            pass
            # 设置变量值
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc5')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rgv.set_value("i", i)
                i = i
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc5', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc5')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_mpy3pbc5', 'time':block_start_time, 'error': error, 'description':r'''设置变量 i 的值为 i''', 'success':node_success_flag, 'variables':{"i": str(i)}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc6')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P02_获取数据 子流程
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("data", data)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                P02_获取数据.start()
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                data = rgv.get_value("data")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc6', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc6')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpy3pbc6', 'time':block_start_time, 'error': error, 'description':r'''调用 P02_获取数据 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc7')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P03_逐笔付款 子流程
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("data", data)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                P03_逐笔付款.start()
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                data = rgv.get_value("data")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc7', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc7')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpy3pbc7', 'time':block_start_time, 'error': error, 'description':r'''调用 P03_逐笔付款 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_mpy3pbc8')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 调用 P04_查询付款信息 子流程
                rgv.set_value("wyfk_sheet", wyfk_sheet)
                rgv.set_value("data", data)
                rgv.set_value("bank_web", bank_web)
                rgv.set_value("i", i)
                P04_查询付款信息.start()
                wyfk_sheet = rgv.get_value("wyfk_sheet")
                data = rgv.get_value("data")
                bank_web = rgv.get_value("bank_web")
                i = rgv.get_value("i")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_mpy3pbc8', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_mpy3pbc8')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpy3pbc8', 'time':block_start_time, 'error': error, 'description':r'''调用 P04_查询付款信息 子流程''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbc4', error, False)
    finally: 
        rgv.set_values({"i": i})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbc4')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'按照次数循环', 'id':'canvas-node-_mpy3pbc4', 'time':block_start_time, 'error': error, 'description':r'''从 2 开始到 4 结束，步长 1 ，每次循环的值赋值给 i''', 'success':node_success_flag, 'variables':{"i": str(i)}})
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mpy3pbc9')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 P05_退出工行网银 子流程
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("data", data)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        P05_退出工行网银.start()
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        data = rgv.get_value("data")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbc9', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbc9')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mpy3pbc9', 'time':block_start_time, 'error': error, 'description':r'''调用 P05_退出工行网银 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 弹出提示框
    try:
        Debug_Block_Start('canvas-node-_mpy3pbca')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        v_notice_alert_value_1 = rpa.system.dialog.msgbox('信息', r"网银对公付款机器人运行完毕，感谢使用！", disappear_time=3)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mpy3pbca', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mpy3pbca')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'弹出提示框', 'id':'canvas-node-_mpy3pbca', 'time':block_start_time, 'error': error, 'description':r'''弹出提示框''', 'success':node_success_flag, 'variables':{"v_notice_alert_value_1": str(v_notice_alert_value_1)}})
        if (error is not None):
            sys.exit(1)
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_mq1tusrr')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 调用 END 子流程
        rgv.set_value("wyfk_sheet", wyfk_sheet)
        rgv.set_value("data", data)
        rgv.set_value("bank_web", bank_web)
        rgv.set_value("i", i)
        END.start()
        wyfk_sheet = rgv.get_value("wyfk_sheet")
        data = rgv.get_value("data")
        bank_web = rgv.get_value("bank_web")
        i = rgv.get_value("i")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_mq1tusrr', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_mq1tusrr')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用子流程', 'id':'canvas-node-_mq1tusrr', 'time':block_start_time, 'error': error, 'description':r'''调用 END 子流程''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 回写全局变量值
    rgv.set_value("wyfk_sheet", wyfk_sheet)
    rgv.set_value("data", data)
    rgv.set_value("bank_web", bank_web)
    rgv.set_value("i", i)