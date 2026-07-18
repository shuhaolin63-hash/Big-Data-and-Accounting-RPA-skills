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
from rpa.sdk import logger


def Debug_Block_Start(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockStart', {'name': name})
def Debug_Block_Success(name):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockSuccess', {'name': name})
def Debug_Block_Error(name, error, outputDebugLog):
    return rpa_v33.core.agent.send('VisualDebug', 'BlockError', {'name': name, 'error': error, 'outputDebugLog': outputDebugLog})


def start():
    rgv._init()
    # 申明全局变量
    # fprz_lines
    rgv.init_value("fprz_lines", None)
    fprz_lines = rgv.get_value("fprz_lines")
    # certification_key
    rgv.init_value("certification_key", r"8888888888888888")
    certification_key = rgv.get_value("certification_key")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # fp_excel
    rgv.init_value("fp_excel", None)
    fp_excel = rgv.get_value("fp_excel")
    # fp_excel_path
    rgv.init_value("fp_excel_path", r"C:\\RPADATA\\发票认证业务数据表.xls")
    fp_excel_path = rgv.get_value("fp_excel_path")
    # username
    rgv.init_value("username", r"")
    username = rgv.get_value("username")
    # certification_web
    rgv.init_value("certification_web", None)
    certification_web = rgv.get_value("certification_web")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # fprz_sheet
    rgv.init_value("fprz_sheet", None)
    fprz_sheet = rgv.get_value("fprz_sheet")
    # result_path
    rgv.init_value("result_path", r"")
    result_path = rgv.get_value("result_path")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # i
    rgv.init_value("i", None)
    i = rgv.get_value("i")
    # password
    rgv.init_value("password", r"")
    password = rgv.get_value("password")
    # cookies
    rgv.init_value("cookies", r"")
    cookies = rgv.get_value("cookies")
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_7icg7iui')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始进行发票认证……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_7icg7iui', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_7icg7iui')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_7icg7iui', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始进行发票认证……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 打开新网页
    try:
        Debug_Block_Start('canvas-node-_xoe6jn1z')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        certification_web = visual.browser.create("chrome", 'http://fz.chinaive.com/fprz/?username='+username,  wait=True, visible=True, timeout=100)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_xoe6jn1z', error, False)
    finally: 
        rgv.set_values({"certification_web": certification_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_xoe6jn1z')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_xoe6jn1z', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问'http://fz.chinaive.com/fprz/?username='+username，将浏览器对象赋值给 certification_web''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 激活网页
    try:
        Debug_Block_Start('canvas-node-_u35ybjd3')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if certification_web is not None:
            visual.browser.activate(certification_web)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_u35ybjd3', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_u35ybjd3')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_u35ybjd3', 'time':block_start_time, 'error': error, 'description':r'''将 certification_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_16w1mvij')
        node_success_flag = True
        sleep(2)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"!{space}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_16w1mvij', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_16w1mvij')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_16w1mvij', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{space}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_ccjee2kl')
        node_success_flag = True
        sleep(0.5)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"x")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ccjee2kl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ccjee2kl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_ccjee2kl', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "x"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 填写输入框（网页）
    try:
        Debug_Block_Start('canvas-node-_j11o4ob6')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if certification_web is not None: 
            visual.element.input(element="证书密码输入框", value=certification_key, elem_type="Chrome", index=1, window=certification_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_j11o4ob6', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_j11o4ob6')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_j11o4ob6', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页 中，在 证书密码输入框 内填写 certification_key''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web),"certification_key": str(certification_key)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_suton5aw')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="登录", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_suton5aw', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_suton5aw')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_suton5aw', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 登录''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 获取已打开网页
    try:
        Debug_Block_Start('canvas-node-_0h6tj5ht')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        certification_web = visual.browser.catch("chrome", r"发票综合服务平台", mode="title", pattern="contain", timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_0h6tj5ht', error, False)
    finally: 
        rgv.set_values({"certification_web": certification_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_0h6tj5ht')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取已打开网页', 'id':'canvas-node-_0h6tj5ht', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中，根据 标题 查找打开的网页 ，将查找到的浏览器对象赋值给 certification_web''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_xfnya80q')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="抵扣勾选", elem_type="Chrome", click_type="left_once", simulate=False, index=1, window=certification_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_xfnya80q', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_xfnya80q')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_xfnya80q', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 抵扣勾选''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 点击控件（网页）
    try:
        Debug_Block_Start('canvas-node-_p7i8aswl')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        visual.element.click(element="发票抵扣勾选", elem_type="Chrome", click_type="left_once", simulate=False, index=1, window=certification_web, timeout=10)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_p7i8aswl', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_p7i8aswl')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_p7i8aswl', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 发票抵扣勾选''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 按照次数循环
    try:
        Debug_Block_Start('canvas-node-_d83uoa19')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(int(2), int(fprz_lines) + 1, int(1)):
            pass
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kw0hw6h5')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles("机器人正在认证第"+str(i-1)+"张发票……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kw0hw6h5', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kw0hw6h5')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kw0hw6h5', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在认证第"+str(i-1)+"张发票……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 获取Excel行的值
            try:
                Debug_Block_Start('canvas-node-_sbbx4fvm')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fprz_sheet is not None:
                    data = fprz_sheet.read(str(i),only_visible = True,max = 1000)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_sbbx4fvm', error, False)
            finally: 
                rgv.set_values({"data": data})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_sbbx4fvm')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel行的值', 'id':'canvas-node-_sbbx4fvm', 'time':block_start_time, 'error': error, 'description':r'''获取 fprz_sheet Sheet页的 i 行的值，并将结果赋值给 data''', 'success':node_success_flag, 'variables':{"i": str(i),"data": str(data),"fprz_sheet": str(fprz_sheet)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_t6yqz52x')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if certification_web is not None: 
                    visual.element.input(element="发票代码输入框", value=data[2], elem_type="Chrome", index=1, window=certification_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_t6yqz52x', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_t6yqz52x')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_t6yqz52x', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页 中，在 发票代码输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_xo3p8ayf')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if certification_web is not None: 
                    visual.element.input(element="发票号码输入框", value=data[3], elem_type="Chrome", index=1, window=certification_web, simulate=False, replace=True, sent_raw=True, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_xo3p8ayf', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_xo3p8ayf')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_xo3p8ayf', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页 中，在 发票号码输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                if (error is not None):
                    sys.exit(1)
            # 点击控件（网页）
            try:
                Debug_Block_Start('canvas-node-_j3ytq7s6')
                node_success_flag = True
                sleep(1.5)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                visual.element.click(element="查询", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_j3ytq7s6', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_j3ytq7s6')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_j3ytq7s6', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 查询''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                if (error is not None):
                    sys.exit(1)
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_j8pojzuc')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_fbyr48yk')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="全部勾选", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_fbyr48yk', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_fbyr48yk')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_fbyr48yk', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 全部勾选''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_pbl15znu')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="提交", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_pbl15znu', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_pbl15znu')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_pbl15znu', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 提交''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 网页截图
                    try:
                        Debug_Block_Start('canvas-node-_68npw9am')
                        node_success_flag = True
                        sleep(2)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if certification_web is not None:
                            result_path=visual.browser.screen_capture(certification_web, r"C:\RPADATA")
                        else:
                            result_path=None
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_68npw9am', error, False)
                    finally: 
                        rgv.set_values({"result_path": result_path})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_68npw9am')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'网页截图', 'id':'canvas-node-_68npw9am', 'time':block_start_time, 'error': error, 'description':r'''将 certification_web 网页截图，保存到 "C:\RPADATA" 文件夹，文件路径信息会赋值给 result_path''', 'success':node_success_flag, 'variables':{"result_path": str(result_path),"certification_web": str(certification_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 获取当前时间&日期
                    try:
                        Debug_Block_Start('canvas-node-_ecm2wl9c')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_ecm2wl9c', error, False)
                    finally: 
                        rgv.set_values({"v_time": v_time})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_ecm2wl9c')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_ecm2wl9c', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_1f9iy83u')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        os.rename(result_path,os.path.join("C:\RPADATA",(str(data[5])+'认证结果'+str(v_time)+'.png')))
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_1f9iy83u', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_1f9iy83u')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_1f9iy83u', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_s88w6zhl')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="“勾选认证信息”窗口的确定按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=20)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_s88w6zhl', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_s88w6zhl')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_s88w6zhl', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 “勾选认证信息”窗口的确定按钮''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_13yr9y3w')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="“提交成功”窗口的确定按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=certification_web, timeout=20)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_13yr9y3w', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_13yr9y3w')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_13yr9y3w', 'time':block_start_time, 'error': error, 'description':r'''在 certification_web 网页中，鼠标 左键单击 “提交成功”窗口的确定按钮''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 出现字幕
                    try:
                        Debug_Block_Start('canvas-node-_kw0d6hiq')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.system.dialog.subtitles(r"未找到，请重新运行机器人！", fontColor='255,255,0,0', fontSize=size_changer)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kw0d6hiq', error, False)
                    finally: 
                        if node_success_flag == True:
                            sleep(3)
                            Debug_Block_Success('canvas-node-_kw0d6hiq')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kw0d6hiq', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "未找到，请重新运行机器人！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_kw0grmhi')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        sys.exit()
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kw0grmhi', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kw0grmhi')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kw0grmhi', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_j8pojzuc', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_j8pojzuc')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_j8pojzuc', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_d83uoa19', error, False)
    finally: 
        rgv.set_values({"i": i})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_d83uoa19')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'按照次数循环', 'id':'canvas-node-_d83uoa19', 'time':block_start_time, 'error': error, 'description':r'''从 2 开始到 fprz_lines 结束，步长 1 ，每次循环的值赋值给 i''', 'success':node_success_flag, 'variables':{"fprz_lines": str(fprz_lines),"i": str(i)}})
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kw0grmhj')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"认证完毕，机器人正在关闭打开的文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kw0grmhj', error, False)
    finally: 
        if node_success_flag == True:
            sleep(2)
            Debug_Block_Success('canvas-node-_kw0grmhj')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kw0grmhj', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "认证完毕，机器人正在关闭打开的文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 激活网页
    try:
        Debug_Block_Start('canvas-node-_r6aqfmfi')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if certification_web is not None:
            visual.browser.activate(certification_web)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_r6aqfmfi', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_r6aqfmfi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_r6aqfmfi', 'time':block_start_time, 'error': error, 'description':r'''将 certification_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"certification_web": str(certification_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_9f0za7a1')
        node_success_flag = True
        sleep(1)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"^{w}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_9f0za7a1', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_9f0za7a1')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_9f0za7a1', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "^{w}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_l346fpn0')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_vxqibc2c')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_29z3spc4')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(os.path.basename(fp_excel_path).split('.')[0], mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_29z3spc4', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_29z3spc4')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_29z3spc4', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(fp_excel_path).split('.')[0] 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_tph4g1gn')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_tph4g1gn', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_tph4g1gn')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_tph4g1gn', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_vxqibc2c', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_vxqibc2c')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_vxqibc2c', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            # 激活窗口
            try:
                Debug_Block_Start('canvas-node-_7yp5po0h')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fp_win is not None: fp_win.activate()
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_7yp5po0h', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_7yp5po0h')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_7yp5po0h', 'time':block_start_time, 'error': error, 'description':r'''激活 fp_win 窗口''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                if (error is not None):
                    sys.exit(1)
            # 输入热键
            try:
                Debug_Block_Start('canvas-node-_fj2rpbf2')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.ui.win32.send_key(r"!{F4}")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_fj2rpbf2', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_fj2rpbf2')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_fj2rpbf2', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        except:
            # 记录日志
            try:
                Debug_Block_Start('canvas-node-_l346hm6q')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger.info(r''' ''')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_l346hm6q', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_l346hm6q')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_l346hm6q', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l346fpn0', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l346fpn0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_l346fpn0', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})