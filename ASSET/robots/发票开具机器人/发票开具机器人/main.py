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
import START
import P00_打开业务数据表
import P01_登录电子税务局
import P02_获取数据
import P03_发票逐笔开具
import P04_退出电子税务局
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
    v_notice_alert_value_2 = r""
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_logloags')
        node_success_flag = True
        # 调用 START 子流程
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
        START.start()
        size_changer = rgv.get_value("size_changer")
        fpkj_excel = rgv.get_value("fpkj_excel")
        fpkj_sheet = rgv.get_value("fpkj_sheet")
        swj_web = rgv.get_value("swj_web")
        lines = rgv.get_value("lines")
        i = rgv.get_value("i")
        data = rgv.get_value("data")
        kp_web = rgv.get_value("kp_web")
        lzfp_web = rgv.get_value("lzfp_web")
        fpkj_win = rgv.get_value("fpkj_win")
        username = rgv.get_value("username")
        password = rgv.get_value("password")
        fpkj_excel_path = rgv.get_value("fpkj_excel_path")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloags', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloags')
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_logloagu')
        node_success_flag = True
        try:
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_lofgjgbh')
                node_success_flag = True
                # 调用 P00_打开业务数据表 子流程
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
                P00_打开业务数据表.start()
                size_changer = rgv.get_value("size_changer")
                fpkj_excel = rgv.get_value("fpkj_excel")
                fpkj_sheet = rgv.get_value("fpkj_sheet")
                swj_web = rgv.get_value("swj_web")
                lines = rgv.get_value("lines")
                i = rgv.get_value("i")
                data = rgv.get_value("data")
                kp_web = rgv.get_value("kp_web")
                lzfp_web = rgv.get_value("lzfp_web")
                fpkj_win = rgv.get_value("fpkj_win")
                username = rgv.get_value("username")
                password = rgv.get_value("password")
                fpkj_excel_path = rgv.get_value("fpkj_excel_path")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgbh', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgbh')
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_lofgjgbi')
                node_success_flag = True
                # 调用 P01_登录电子税务局 子流程
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
                P01_登录电子税务局.start()
                size_changer = rgv.get_value("size_changer")
                fpkj_excel = rgv.get_value("fpkj_excel")
                fpkj_sheet = rgv.get_value("fpkj_sheet")
                swj_web = rgv.get_value("swj_web")
                lines = rgv.get_value("lines")
                i = rgv.get_value("i")
                data = rgv.get_value("data")
                kp_web = rgv.get_value("kp_web")
                lzfp_web = rgv.get_value("lzfp_web")
                fpkj_win = rgv.get_value("fpkj_win")
                username = rgv.get_value("username")
                password = rgv.get_value("password")
                fpkj_excel_path = rgv.get_value("fpkj_excel_path")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgbi', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgbi')
            # 按照次数循环
            try:
                Debug_Block_Start('canvas-node-_lofgjgb3')
                node_success_flag = True
                for i in range(int(2), int(lines) + 1, int(1)):
                    pass
                    # 设置变量值
                    try:
                        Debug_Block_Start('canvas-node-_lofgjgbl')
                        node_success_flag = True
                        rgv.set_value("i", i)
                        i = i
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lofgjgbl', error, True)
                        sys.exit(1)
                    finally:
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lofgjgbl')
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_lofgjgbj')
                        node_success_flag = True
                        # 调用 P02_获取数据 子流程
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
                        P02_获取数据.start()
                        size_changer = rgv.get_value("size_changer")
                        fpkj_excel = rgv.get_value("fpkj_excel")
                        fpkj_sheet = rgv.get_value("fpkj_sheet")
                        swj_web = rgv.get_value("swj_web")
                        lines = rgv.get_value("lines")
                        i = rgv.get_value("i")
                        data = rgv.get_value("data")
                        kp_web = rgv.get_value("kp_web")
                        lzfp_web = rgv.get_value("lzfp_web")
                        fpkj_win = rgv.get_value("fpkj_win")
                        username = rgv.get_value("username")
                        password = rgv.get_value("password")
                        fpkj_excel_path = rgv.get_value("fpkj_excel_path")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lofgjgbj', error, True)
                        sys.exit(1)
                    finally:
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lofgjgbj')
                    # 调用子流程
                    try:
                        Debug_Block_Start('canvas-node-_lofgjgbk')
                        node_success_flag = True
                        # 调用 P03_发票逐笔开具 子流程
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
                        P03_发票逐笔开具.start()
                        size_changer = rgv.get_value("size_changer")
                        fpkj_excel = rgv.get_value("fpkj_excel")
                        fpkj_sheet = rgv.get_value("fpkj_sheet")
                        swj_web = rgv.get_value("swj_web")
                        lines = rgv.get_value("lines")
                        i = rgv.get_value("i")
                        data = rgv.get_value("data")
                        kp_web = rgv.get_value("kp_web")
                        lzfp_web = rgv.get_value("lzfp_web")
                        fpkj_win = rgv.get_value("fpkj_win")
                        username = rgv.get_value("username")
                        password = rgv.get_value("password")
                        fpkj_excel_path = rgv.get_value("fpkj_excel_path")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lofgjgbk', error, True)
                        sys.exit(1)
                    finally:
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lofgjgbk')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_lofgjgb3', error, True)
            finally:
                rgv.set_values({"i": i})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_lofgjgb3')
            # 调用子流程
            try:
                Debug_Block_Start('canvas-node-_loghnt6f')
                node_success_flag = True
                # 调用 P04_退出电子税务局 子流程
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
                P04_退出电子税务局.start()
                size_changer = rgv.get_value("size_changer")
                fpkj_excel = rgv.get_value("fpkj_excel")
                fpkj_sheet = rgv.get_value("fpkj_sheet")
                swj_web = rgv.get_value("swj_web")
                lines = rgv.get_value("lines")
                i = rgv.get_value("i")
                data = rgv.get_value("data")
                kp_web = rgv.get_value("kp_web")
                lzfp_web = rgv.get_value("lzfp_web")
                fpkj_win = rgv.get_value("fpkj_win")
                username = rgv.get_value("username")
                password = rgv.get_value("password")
                fpkj_excel_path = rgv.get_value("fpkj_excel_path")
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_loghnt6f', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_loghnt6f')
            # 弹出提示框
            try:
                Debug_Block_Start('canvas-node-_logloagq')
                node_success_flag = True
                v_notice_alert_value_2 = rpa.system.dialog.msgbox('信息', r"发票开具机器人运行完毕，感谢使用！", disappear_time=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_logloagq', error, True)
                sys.exit(1)
            finally:
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_logloagq')
            pass
        except:
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloagu', error, True)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloagu')
    # 调用子流程
    try:
        Debug_Block_Start('canvas-node-_logloagt')
        node_success_flag = True
        # 调用 END 子流程
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
        END.start()
        size_changer = rgv.get_value("size_changer")
        fpkj_excel = rgv.get_value("fpkj_excel")
        fpkj_sheet = rgv.get_value("fpkj_sheet")
        swj_web = rgv.get_value("swj_web")
        lines = rgv.get_value("lines")
        i = rgv.get_value("i")
        data = rgv.get_value("data")
        kp_web = rgv.get_value("kp_web")
        lzfp_web = rgv.get_value("lzfp_web")
        fpkj_win = rgv.get_value("fpkj_win")
        username = rgv.get_value("username")
        password = rgv.get_value("password")
        fpkj_excel_path = rgv.get_value("fpkj_excel_path")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_logloagt', error, True)
        sys.exit(1)
    finally:
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_logloagt')
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