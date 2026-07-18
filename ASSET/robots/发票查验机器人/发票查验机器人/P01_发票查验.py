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
import invoice_collect
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
    # tsk_value
    rgv.init_value("tsk_value", r"")
    tsk_value = rgv.get_value("tsk_value")
    # v_time
    rgv.init_value("v_time", r"")
    v_time = rgv.get_value("v_time")
    # fp_excel_path
    rgv.init_value("fp_excel_path", r"C:/RPADATA/发票查验业务数据表.xls")
    fp_excel_path = rgv.get_value("fp_excel_path")
    # fp_excel
    rgv.init_value("fp_excel", None)
    fp_excel = rgv.get_value("fp_excel")
    # Vcode
    rgv.init_value("Vcode", r"flase")
    Vcode = rgv.get_value("Vcode")
    # web_result
    rgv.init_value("web_result", r"")
    web_result = rgv.get_value("web_result")
    # username
    rgv.init_value("username", r" ")
    username = rgv.get_value("username")
    # fp_win
    rgv.init_value("fp_win", None)
    fp_win = rgv.get_value("fp_win")
    # v_date
    rgv.init_value("v_date", r"")
    v_date = rgv.get_value("v_date")
    # fpcy_excel_path
    rgv.init_value("fpcy_excel_path", r"")
    fpcy_excel_path = rgv.get_value("fpcy_excel_path")
    # fpcy_cyjg_excel
    rgv.init_value("fpcy_cyjg_excel", None)
    fpcy_cyjg_excel = rgv.get_value("fpcy_cyjg_excel")
    # lines_number
    rgv.init_value("lines_number", 1)
    lines_number = rgv.get_value("lines_number")
    # fpcyxx_sheet_name
    rgv.init_value("fpcyxx_sheet_name", r"发票查验信息")
    fpcyxx_sheet_name = rgv.get_value("fpcyxx_sheet_name")
    # check_html
    rgv.init_value("check_html", r"")
    check_html = rgv.get_value("check_html")
    # fpcyjg_sheet_name
    rgv.init_value("fpcyjg_sheet_name", r"发票查验结果")
    fpcyjg_sheet_name = rgv.get_value("fpcyjg_sheet_name")
    # fpcy_cyjg_sheet
    rgv.init_value("fpcy_cyjg_sheet", None)
    fpcy_cyjg_sheet = rgv.get_value("fpcy_cyjg_sheet")
    # size_changer
    rgv.init_value("size_changer", 36)
    size_changer = rgv.get_value("size_changer")
    # invoice_web
    rgv.init_value("invoice_web", None)
    invoice_web = rgv.get_value("invoice_web")
    # fpcy_sheet
    rgv.init_value("fpcy_sheet", None)
    fpcy_sheet = rgv.get_value("fpcy_sheet")
    # data
    rgv.init_value("data", [])
    data = rgv.get_value("data")
    # fpcy_cyxx_sheet
    rgv.init_value("fpcy_cyxx_sheet", None)
    fpcy_cyxx_sheet = rgv.get_value("fpcy_cyxx_sheet")
    # fpcy_lines
    rgv.init_value("fpcy_lines", None)
    fpcy_lines = rgv.get_value("fpcy_lines")
    # verification_code
    rgv.init_value("verification_code", r"")
    verification_code = rgv.get_value("verification_code")
    # result_path
    rgv.init_value("result_path", r"")
    result_path = rgv.get_value("result_path")
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
        Debug_Block_Start('canvas-node-_kwbwkd5z')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"机器人开始进行发票查验……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kwbwkd5z', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kwbwkd5z')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kwbwkd5z', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人开始进行发票查验……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 获取当前时间&日期
    try:
        Debug_Block_Start('canvas-node-_ims4anoi')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        v_date = datetime.datetime.now().strftime(r'%Y年%m月%d日'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ims4anoi', error, False)
    finally: 
        rgv.set_values({"v_date": v_date})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ims4anoi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_ims4anoi', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_date''', 'success':node_success_flag, 'variables':{"v_date": str(v_date)}})
        if (error is not None):
            sys.exit(1)
    # 获取当前时间&日期
    try:
        Debug_Block_Start('canvas-node-_51lg6mvw')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_51lg6mvw', error, False)
    finally: 
        rgv.set_values({"v_time": v_time})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_51lg6mvw')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_51lg6mvw', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
        if (error is not None):
            sys.exit(1)
    # 设置变量值
    try:
        Debug_Block_Start('canvas-node-_w57yy2up')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rgv.set_value("fpcy_excel_path", str(os.path.dirname(fp_excel_path)+"/【"+v_date+"】发票查验结果"+v_time+".xlsx").replace('/','\\'))
        fpcy_excel_path = str(os.path.dirname(fp_excel_path)+"/【"+v_date+"】发票查验结果"+v_time+".xlsx").replace('/','\\')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_w57yy2up', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_w57yy2up')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_w57yy2up', 'time':block_start_time, 'error': error, 'description':r'''设置变量 fpcy_excel_path 的值为 str(os.path.dirname(fp_excel_path)+"/【"+v_date+"】发票查验结果"+v_time+".xlsx").replace('/','\\')''', 'success':node_success_flag, 'variables':{"fpcy_excel_path": str(fpcy_excel_path)}})
        if (error is not None):
            sys.exit(1)
    # 启动Excel
    try:
        Debug_Block_Start('canvas-node-_7jyu1gnx')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fpcy_cyjg_excel = rpa.app.microsoft.excel.create(visible=True)
        fpcy_cyjg_excel.save(file=fpcy_excel_path,suffix=None)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_7jyu1gnx', error, False)
    finally: 
        rgv.set_values({"fpcy_cyjg_excel": fpcy_cyjg_excel})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_7jyu1gnx')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'启动Excel', 'id':'canvas-node-_7jyu1gnx', 'time':block_start_time, 'error': error, 'description':r'''根据匹配，查找已打开的Excel，将查找到的Excel对象赋值给 fpcy_cyjg_excel''', 'success':node_success_flag, 'variables':{"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"": str(),"fpcy_excel_path": str(fpcy_excel_path)}})
        if (error is not None):
            sys.exit(1)
    # 创建Sheet页
    try:
        Debug_Block_Start('canvas-node-_x0vi49rk')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyjg_excel is None:
            fpcy_cyjg_sheet = None   
        else:
            sheets = fpcy_cyjg_excel.get_sheets()
            location = fpcy_cyjg_excel.get_sheet(sheets[0].name)
            fpcy_cyjg_sheet = fpcy_cyjg_excel.add_sheet(fpcyjg_sheet_name, location.name, relative='before')
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_x0vi49rk', error, False)
    finally: 
        rgv.set_values({"fpcy_cyjg_sheet": fpcy_cyjg_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_x0vi49rk')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'创建Sheet页', 'id':'canvas-node-_x0vi49rk', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_excel Excel对象中创建Sheet页 fpcyjg_sheet_name，并将新建的Sheet页对象赋值给 fpcy_cyjg_sheet''', 'success':node_success_flag, 'variables':{"fpcy_cyjg_sheet": str(fpcy_cyjg_sheet),"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"fpcyjg_sheet_name": str(fpcyjg_sheet_name)}})
        if (error is not None):
            sys.exit(1)
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_nold9p2g')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyjg_excel is not None:
            sheet = fpcy_cyjg_excel.get_sheet(fpcyjg_sheet_name)
            if sheet is not None:
                sheet.activate()
                fpcy_cyjg_sheet= fpcy_cyjg_excel.get_sheet()
        else:
            fpcy_cyjg_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_nold9p2g', error, False)
    finally: 
        rgv.set_values({"fpcy_cyjg_sheet": fpcy_cyjg_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_nold9p2g')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_nold9p2g', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_excel Excel对象中激活Sheet页 fpcyjg_sheet_name，将对应的Sheet页对象赋值给 fpcy_cyjg_sheet''', 'success':node_success_flag, 'variables':{"fpcy_cyjg_sheet": str(fpcy_cyjg_sheet),"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"fpcyjg_sheet_name": str(fpcyjg_sheet_name)}})
        if (error is not None):
            sys.exit(1)
    # 写入Excel行
    try:
        Debug_Block_Start('canvas-node-_j02u6zrf')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyjg_sheet is not None:
            region= str(1)                               
            fpcy_cyjg_sheet.write(region, ['序号','发票类型','发票代码','发票号码','开票日期','校验码','小写不含税金额','查验状态'], start_row=1, start_col=r"A", max=1000)
            fpcy_cyjg_sheet.excel.save(file=None)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_j02u6zrf', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_j02u6zrf')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel行', 'id':'canvas-node-_j02u6zrf', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_sheet Sheet页中，从 A1 开始写入行 ['序号','发票类型','发票代码','发票号码','开票日期','校验码','小写不含税金额','查验状态']  并保存''', 'success':node_success_flag, 'variables':{"fpcy_cyjg_sheet": str(fpcy_cyjg_sheet)}})
        if (error is not None):
            sys.exit(1)
    # 重命名Sheet页
    try:
        Debug_Block_Start('canvas-node-_n9u7wj7f')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyjg_excel is not None:
            fpcy_cyjg_excel.rename_sheet(r"Sheet1",fpcyxx_sheet_name)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_n9u7wj7f', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_n9u7wj7f')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'重命名Sheet页', 'id':'canvas-node-_n9u7wj7f', 'time':block_start_time, 'error': error, 'description':r'''将 fpcy_cyjg_excel Excel对象中的 "Sheet1" 修改为 fpcyxx_sheet_name''', 'success':node_success_flag, 'variables':{"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"fpcyxx_sheet_name": str(fpcyxx_sheet_name)}})
        if (error is not None):
            sys.exit(1)
    # 激活Sheet页
    try:
        Debug_Block_Start('canvas-node-_hs1j7ide')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyjg_excel is not None:
            sheet = fpcy_cyjg_excel.get_sheet(fpcyxx_sheet_name)
            if sheet is not None:
                sheet.activate()
                fpcy_cyxx_sheet= fpcy_cyjg_excel.get_sheet()
        else:
            fpcy_cyxx_sheet = None
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_hs1j7ide', error, False)
    finally: 
        rgv.set_values({"fpcy_cyxx_sheet": fpcy_cyxx_sheet})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_hs1j7ide')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_hs1j7ide', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_excel Excel对象中激活Sheet页 fpcyxx_sheet_name，将对应的Sheet页对象赋值给 fpcy_cyxx_sheet''', 'success':node_success_flag, 'variables':{"fpcy_cyxx_sheet": str(fpcy_cyxx_sheet),"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"fpcyxx_sheet_name": str(fpcyxx_sheet_name)}})
        if (error is not None):
            sys.exit(1)
    # 写入Excel行
    try:
        Debug_Block_Start('canvas-node-_c39ql0yv')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if fpcy_cyxx_sheet is not None:
            region= str(1)                               
            fpcy_cyxx_sheet.write(region, ['序号','发票类型','发票代码','发票号码','开票日期','购买方名称','购买方纳税人识别号','购买方地址、电话','购买方开户行及账号','货物或应税劳务、服务名称','规格型号','单位','数量','单价','金额','税率','税额','金额合计','税额合计','价税合计（大写）','价税合计（小写）','销售方名称','销售方纳税人识别号','销售方地址、电话','开户行及账号'], start_row=1, start_col=r"A", max=1000)
            fpcy_cyxx_sheet.excel.save(file=None)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_c39ql0yv', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_c39ql0yv')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel行', 'id':'canvas-node-_c39ql0yv', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyxx_sheet Sheet页中，从 A1 开始写入行 ['序号','发票类型','发票代码','发票号码','开票日期','购买方名称','购买方纳税人识别号','购买方地址、电话','购买方开户行及账号','货物或应税劳务、服务名称','规格型号','单位','数量','单价','金额','税率','税额','金额合计','税额合计','价税合计（大写）','价税合计（小写）','销售方名称','销售方纳税人识别号','销售方地址、电话','开户行及账号']  并保存''', 'success':node_success_flag, 'variables':{"fpcy_cyxx_sheet": str(fpcy_cyxx_sheet)}})
        if (error is not None):
            sys.exit(1)
    # 打开新网页
    try:
        Debug_Block_Start('canvas-node-_juyej5im')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        invoice_web = visual.browser.create("chrome", 'http://fz.chinaive.com/fpcy/?username=' + username,  wait=True, visible=True, timeout=100)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_juyej5im', error, False)
    finally: 
        rgv.set_values({"invoice_web": invoice_web})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_juyej5im')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'打开新网页', 'id':'canvas-node-_juyej5im', 'time':block_start_time, 'error': error, 'description':r'''在 chrome 中新建网页访问'http://fz.chinaive.com/fpcy/?username=' + username，将浏览器对象赋值给 invoice_web''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
        if (error is not None):
            sys.exit(1)
    # 激活网页
    try:
        Debug_Block_Start('canvas-node-_bxn98q1g')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if invoice_web is not None:
            visual.browser.activate(invoice_web)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_bxn98q1g', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_bxn98q1g')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_bxn98q1g', 'time':block_start_time, 'error': error, 'description':r'''将 invoice_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_imbebe44')
        node_success_flag = True
        sleep(3)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"!{space}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_imbebe44', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_imbebe44')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_imbebe44', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{space}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_nn2hukzi')
        node_success_flag = True
        sleep(0.5)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"x")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_nn2hukzi', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_nn2hukzi')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_nn2hukzi', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "x"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 按照次数循环
    try:
        Debug_Block_Start('canvas-node-_n6d7444b')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(int(2), int(fpcy_lines) + 1, int(1)):
            pass
            # 出现字幕
            try:
                Debug_Block_Start('canvas-node-_kvvwzira')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rpa.system.dialog.subtitles("机器人正在查验第"+str(i-1)+"张发票……", fontColor='255,0,0,255', fontSize=size_changer)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_kvvwzira', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_kvvwzira')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvvwzira', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "机器人正在查验第"+str(i-1)+"张发票……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                if (error is not None):
                    sys.exit(1)
            # 获取Excel行的值
            try:
                Debug_Block_Start('canvas-node-_p53f3drw')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if fpcy_sheet is not None:
                    data = fpcy_sheet.read(str(i),only_visible = True,max = 1000)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_p53f3drw', error, False)
            finally: 
                rgv.set_values({"data": data})
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_p53f3drw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取Excel行的值', 'id':'canvas-node-_p53f3drw', 'time':block_start_time, 'error': error, 'description':r'''获取 fpcy_sheet Sheet页的 i 行的值，并将结果赋值给 data''', 'success':node_success_flag, 'variables':{"i": str(i),"data": str(data),"fpcy_sheet": str(fpcy_sheet)}})
                if (error is not None):
                    sys.exit(1)
            # 激活网页
            try:
                Debug_Block_Start('canvas-node-_l1yj6rzk')
                node_success_flag = True
                sleep(1)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None:
                    visual.browser.activate(invoice_web)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_l1yj6rzk', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_l1yj6rzk')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_l1yj6rzk', 'time':block_start_time, 'error': error, 'description':r'''将 invoice_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_tmtn218d')
                node_success_flag = True
                sleep(0.5)
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="发票代码输入框", value=data[2], elem_type="IE", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_tmtn218d', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_tmtn218d')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_tmtn218d', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 发票代码输入框 内填写 data[2]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_0n7in35w')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="发票号码输入框", value=data[3], elem_type="IE", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_0n7in35w', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_0n7in35w')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_0n7in35w', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 发票号码输入框 内填写 data[3]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 填写输入框（网页）
            try:
                Debug_Block_Start('canvas-node-_n1hzu4yw')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if invoice_web is not None: 
                    visual.element.input(element="开票日期输入框", value=data[4], elem_type="IE", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_n1hzu4yw', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_n1hzu4yw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_n1hzu4yw', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 开票日期输入框 内填写 data[4]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                if (error is not None):
                    sys.exit(1)
            # 条件分支
            try:
                Debug_Block_Start('canvas-node-_xhz2ll7j')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if ('专用' in data[1]):
                    pass
                    # 填写输入框（网页）
                    try:
                        Debug_Block_Start('canvas-node-_oet2vait')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if invoice_web is not None: 
                            visual.element.input(element="校验码输入框", value=data[15], elem_type="IE", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_oet2vait', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_oet2vait')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_oet2vait', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 校验码输入框 内填写 data[15]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                else:
                    pass
                    # 填写输入框（网页）
                    try:
                        Debug_Block_Start('canvas-node-_u565h2cz')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if invoice_web is not None: 
                            visual.element.input(element="校验码输入框", value=data[5][-6:], elem_type="IE", index=1, window=invoice_web, simulate=True, replace=True, sent_raw=False, wait_mili_seconds=20, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_u565h2cz', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_u565h2cz')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'填写输入框（网页）', 'id':'canvas-node-_u565h2cz', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页 中，在 校验码输入框 内填写 data[5][-6:]''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_xhz2ll7j', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_xhz2ll7j')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'条件分支', 'id':'canvas-node-_xhz2ll7j', 'time':block_start_time, 'error': error, 'description':r'''if-else条件分支''', 'success':node_success_flag, 'variables':{}})
            # 条件循环
            try:
                Debug_Block_Start('canvas-node-_jnpx05rx')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                while (Vcode != "true"):
                    pass
                    # 获取网页元素的属性值
                    try:
                        Debug_Block_Start('canvas-node-_bi80c5bu')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        verification_code = visual.element.attr("验证码", elem_type="Chrome", attrname=r"value", index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_bi80c5bu', error, False)
                    finally: 
                        rgv.set_values({"verification_code": verification_code})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_bi80c5bu')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取网页元素的属性值', 'id':'canvas-node-_bi80c5bu', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，获取 验证码的 "value" 属性值，将结果赋值给 verification_code''', 'success':node_success_flag, 'variables':{"verification_code": str(verification_code),"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 通过剪贴方式输入（网页）
                    try:
                        Debug_Block_Start('canvas-node-_kzy1vt7p')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if invoice_web is not None: 
                            pyperclip.copy(verification_code)                                                                         
                            visual.element.input_hotkey("验证码输入框", "VK_CONTROL|V", elem_type="IE", replace=True, index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kzy1vt7p', error, False)
                    finally: 
                        if node_success_flag == True:
                            sleep(0.5)
                            Debug_Block_Success('canvas-node-_kzy1vt7p')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'通过剪贴方式输入（网页）', 'id':'canvas-node-_kzy1vt7p', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，通过剪贴方式在 验证码输入框 内填写 verification_code''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web),"verification_code": str(verification_code)}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_9m9udu3a')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="查验", elem_type="IE", click_type="left_once", simulate=True, index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_9m9udu3a', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_9m9udu3a')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_9m9udu3a', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，鼠标 左键单击 查验''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 捕获异常和重试
                    try:
                        Debug_Block_Start('canvas-node-_d2c31fjz')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        try:
                            # 点击控件（网页）
                            try:
                                Debug_Block_Start('canvas-node-_7pw57yug')
                                node_success_flag = True
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                visual.element.click(element="确定", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=invoice_web, timeout=2)
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_7pw57yug', error, False)
                            finally: 
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_7pw57yug')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_7pw57yug', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，鼠标 左键单击 确定''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                                if (error is not None):
                                    sys.exit(1)
                            pass
                        except:
                            # 设置变量值
                            try:
                                Debug_Block_Start('canvas-node-_37773a0n')
                                node_success_flag = True
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                rgv.set_value("Vcode", r"true")
                                Vcode = r"true"
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_37773a0n', error, False)
                            finally: 
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_37773a0n')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_37773a0n', 'time':block_start_time, 'error': error, 'description':r'''设置变量 Vcode 的值为 "true"''', 'success':node_success_flag, 'variables':{"Vcode": str(Vcode)}})
                                if (error is not None):
                                    sys.exit(1)
                            pass
                        finally:
                            pass
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_d2c31fjz', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_d2c31fjz')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_d2c31fjz', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_jnpx05rx', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_jnpx05rx')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'条件循环', 'id':'canvas-node-_jnpx05rx', 'time':block_start_time, 'error': error, 'description':r'''使用 while 循环，注意避免发生死循环''', 'success':node_success_flag, 'variables':{}})
            # 设置变量值
            try:
                Debug_Block_Start('canvas-node-_f4mvsbuw')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                rgv.set_value("Vcode", r"flase")
                Vcode = r"flase"
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_f4mvsbuw', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_f4mvsbuw')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_f4mvsbuw', 'time':block_start_time, 'error': error, 'description':r'''设置变量 Vcode 的值为 "flase"''', 'success':node_success_flag, 'variables':{"Vcode": str(Vcode)}})
                if (error is not None):
                    sys.exit(1)
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_sgmt464m')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取文本（网页）
                    try:
                        Debug_Block_Start('canvas-node-_v2m4p8rt')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        web_result = visual.element.get_text("发票查验明细", elem_type="Chrome", index=1, window=invoice_web, timeout=2)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_v2m4p8rt', error, False)
                    finally: 
                        rgv.set_values({"web_result": web_result})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_v2m4p8rt')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取文本（网页）', 'id':'canvas-node-_v2m4p8rt', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，获取 发票查验明细 的文本，将结果赋值给 web_result''', 'success':node_success_flag, 'variables':{"web_result": str(web_result),"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 出现字幕
                    try:
                        Debug_Block_Start('canvas-node-_kvsv7m0s')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.system.dialog.subtitles("第"+str(i-1)+"张发票查验成功！", fontColor='255,0,0,255', fontSize=size_changer)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvsv7m0s', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvsv7m0s')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvsv7m0s', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "第"+str(i-1)+"张发票查验成功！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                        if (error is not None):
                            sys.exit(1)
                    # 网页截图
                    try:
                        Debug_Block_Start('canvas-node-_th76jy17')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if invoice_web is not None:
                            result_path=visual.browser.screen_capture(invoice_web, r"C:\RPADATA")
                        else:
                            result_path=None
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_th76jy17', error, False)
                    finally: 
                        rgv.set_values({"result_path": result_path})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_th76jy17')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'网页截图', 'id':'canvas-node-_th76jy17', 'time':block_start_time, 'error': error, 'description':r'''将 invoice_web 网页截图，保存到 "C:\RPADATA" 文件夹，文件路径信息会赋值给 result_path''', 'success':node_success_flag, 'variables':{"result_path": str(result_path),"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 获取当前时间&日期
                    try:
                        Debug_Block_Start('canvas-node-_qso1hkgz')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_qso1hkgz', error, False)
                    finally: 
                        rgv.set_values({"v_time": v_time})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_qso1hkgz')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_qso1hkgz', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_9wo4g2p7')
                        node_success_flag = True
                        sleep(1)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        os.rename(result_path,os.path.join("C:\RPADATA",('发票号码'+str(data[3])+'查验结果'+str(v_time)+'.png')))
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_9wo4g2p7', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_9wo4g2p7')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_9wo4g2p7', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 获取网页元素的HTML代码
                    try:
                        Debug_Block_Start('canvas-node-_k640mv70')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        check_html = visual.element.get_html("获取发票查验明细页面HTML", elem_type="Chrome", index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_k640mv70', error, False)
                    finally: 
                        rgv.set_values({"check_html": check_html})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_k640mv70')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取网页元素的HTML代码', 'id':'canvas-node-_k640mv70', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，获取 获取发票查验明细页面HTML 的HTML片段，将结果赋值给 check_html''', 'success':node_success_flag, 'variables':{"check_html": str(check_html),"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 添加列表项
                    try:
                        Debug_Block_Start('canvas-node-_ug2mqlv3')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        array = data
                        array.append(r"已获取发票信息")
                        data = array
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_ug2mqlv3', error, False)
                    finally: 
                        rgv.set_values({"data": data})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_ug2mqlv3')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'添加列表项', 'id':'canvas-node-_ug2mqlv3', 'time':block_start_time, 'error': error, 'description':r'''在列表 data 在列表尾部添加 "已获取发票信息"''', 'success':node_success_flag, 'variables':{"data": str(data),"data": str(data)}})
                        if (error is not None):
                            sys.exit(1)
                    # 写入Excel行
                    try:
                        Debug_Block_Start('canvas-node-_vn4mp7gh')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fpcy_cyjg_sheet is not None:
                            region= str(i)                               
                            fpcy_cyjg_sheet.write(region, [data[0],data[1],data[2],data[3],data[4],data[5],data[15],data[26]], start_row=1, start_col=r"A", max=1000)
                            fpcy_cyjg_sheet.excel.save(file=None)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_vn4mp7gh', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_vn4mp7gh')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel行', 'id':'canvas-node-_vn4mp7gh', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_sheet Sheet页中，从 A i 开始写入行 [data[0],data[1],data[2],data[3],data[4],data[5],data[15],data[26]]  并保存''', 'success':node_success_flag, 'variables':{"i": str(i),"fpcy_cyjg_sheet": str(fpcy_cyjg_sheet)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_vl59eiv3')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        data=invoice_collect.start(check_html)
                        data.insert(0,i-1)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_vl59eiv3', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_vl59eiv3')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_vl59eiv3', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 记录日志
                    try:
                        Debug_Block_Start('canvas-node-_dh3g32la')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        logger.info(data)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_dh3g32la', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_dh3g32la')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_dh3g32la', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{"data": str(data)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_xkk2r9tt')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        print(data)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_xkk2r9tt', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_xkk2r9tt')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_xkk2r9tt', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_qq2332un')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="“发票查验结果”窗口的关闭按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_qq2332un', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_qq2332un')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_qq2332un', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，鼠标 左键单击 “发票查验结果”窗口的关闭按钮''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 设置变量值
                    try:
                        Debug_Block_Start('canvas-node-_n1tmgc0s')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rgv.set_value("lines_number", lines_number+1)
                        lines_number = lines_number+1
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_n1tmgc0s', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_n1tmgc0s')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'设置变量值', 'id':'canvas-node-_n1tmgc0s', 'time':block_start_time, 'error': error, 'description':r'''设置变量 lines_number 的值为 lines_number+1''', 'success':node_success_flag, 'variables':{"lines_number": str(lines_number)}})
                        if (error is not None):
                            sys.exit(1)
                    # 激活Sheet页
                    try:
                        Debug_Block_Start('canvas-node-_l2q171ei')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fpcy_cyjg_excel is not None:
                            sheet = fpcy_cyjg_excel.get_sheet(fpcyxx_sheet_name)
                            if sheet is not None:
                                sheet.activate()
                                fpcy_cyxx_sheet= fpcy_cyjg_excel.get_sheet()
                        else:
                            fpcy_cyxx_sheet = None
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_l2q171ei', error, False)
                    finally: 
                        rgv.set_values({"fpcy_cyxx_sheet": fpcy_cyxx_sheet})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_l2q171ei')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活Sheet页', 'id':'canvas-node-_l2q171ei', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_excel Excel对象中激活Sheet页 fpcyxx_sheet_name，将对应的Sheet页对象赋值给 fpcy_cyxx_sheet''', 'success':node_success_flag, 'variables':{"fpcy_cyxx_sheet": str(fpcy_cyxx_sheet),"fpcy_cyjg_excel": str(fpcy_cyjg_excel),"fpcyxx_sheet_name": str(fpcyxx_sheet_name)}})
                        if (error is not None):
                            sys.exit(1)
                    # 写入Excel行
                    try:
                        Debug_Block_Start('canvas-node-_7dic5ef8')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fpcy_cyxx_sheet is not None:
                            region= str(lines_number)                               
                            fpcy_cyxx_sheet.write(region, data, start_row=1, start_col=r"A", max=1000)
                            fpcy_cyxx_sheet.excel.save(file=None)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_7dic5ef8', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_7dic5ef8')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel行', 'id':'canvas-node-_7dic5ef8', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyxx_sheet Sheet页中，从 A lines_number 开始写入行 data  并保存''', 'success':node_success_flag, 'variables':{"lines_number": str(lines_number),"fpcy_cyxx_sheet": str(fpcy_cyxx_sheet),"data": str(data)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                except:
                    # 出现字幕
                    try:
                        Debug_Block_Start('canvas-node-_kvsv7m0t')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.system.dialog.subtitles("第"+str(i-1)+"张发票查验有误，请确认此张发票信息是否正确！", fontColor='255,255,0,0', fontSize=size_changer)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kvsv7m0t', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kvsv7m0t')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvsv7m0t', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "第"+str(i-1)+"张发票查验有误，请确认此张发票信息是否正确！"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
                        if (error is not None):
                            sys.exit(1)
                    # 网页截图
                    try:
                        Debug_Block_Start('canvas-node-_g8xfg9lk')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if invoice_web is not None:
                            result_path=visual.browser.screen_capture(invoice_web, r"C:\RPADATA")
                        else:
                            result_path=None
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_g8xfg9lk', error, False)
                    finally: 
                        rgv.set_values({"result_path": result_path})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_g8xfg9lk')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'网页截图', 'id':'canvas-node-_g8xfg9lk', 'time':block_start_time, 'error': error, 'description':r'''将 invoice_web 网页截图，保存到 "C:\RPADATA" 文件夹，文件路径信息会赋值给 result_path''', 'success':node_success_flag, 'variables':{"result_path": str(result_path),"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 获取当前时间&日期
                    try:
                        Debug_Block_Start('canvas-node-_eqzf2m0p')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        v_time = datetime.datetime.now().strftime(r'%H%M%S'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_eqzf2m0p', error, False)
                    finally: 
                        rgv.set_values({"v_time": v_time})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_eqzf2m0p')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取当前时间&日期', 'id':'canvas-node-_eqzf2m0p', 'time':block_start_time, 'error': error, 'description':r'''获取当前时间，将结果赋值给 v_time''', 'success':node_success_flag, 'variables':{"v_time": str(v_time)}})
                        if (error is not None):
                            sys.exit(1)
                    # 调用自定义脚本
                    try:
                        Debug_Block_Start('canvas-node-_kl8k714d')
                        node_success_flag = True
                        sleep(1)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        os.rename(result_path,os.path.join("C:\RPADATA",('【查验异常】发票号码'+str(data[3])+'查验结果'+str(v_time)+'.png')))
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_kl8k714d', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_kl8k714d')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'调用自定义脚本', 'id':'canvas-node-_kl8k714d', 'time':block_start_time, 'error': error, 'description':r'''调用自定义脚本''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 点击控件（网页）
                    try:
                        Debug_Block_Start('canvas-node-_od96k3j3')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        visual.element.click(element="”查无此票“窗口的关闭按钮", elem_type="Chrome", click_type="left_once", simulate=True, index=1, window=invoice_web, timeout=10)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_od96k3j3', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_od96k3j3')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'点击控件（网页）', 'id':'canvas-node-_od96k3j3', 'time':block_start_time, 'error': error, 'description':r'''在 invoice_web 网页中，鼠标 左键单击 ”查无此票“窗口的关闭按钮''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
                        if (error is not None):
                            sys.exit(1)
                    # 添加列表项
                    try:
                        Debug_Block_Start('canvas-node-_fuedu9s9')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        array = data
                        array.append(r"查验有误")
                        data = array
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_fuedu9s9', error, False)
                    finally: 
                        rgv.set_values({"data": data})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_fuedu9s9')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'添加列表项', 'id':'canvas-node-_fuedu9s9', 'time':block_start_time, 'error': error, 'description':r'''在列表 data 在列表尾部添加 "查验有误"''', 'success':node_success_flag, 'variables':{"data": str(data),"data": str(data)}})
                        if (error is not None):
                            sys.exit(1)
                    # 写入Excel行
                    try:
                        Debug_Block_Start('canvas-node-_7v9v8ywl')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fpcy_cyjg_sheet is not None:
                            region= str(i)                               
                            fpcy_cyjg_sheet.write(region, [data[0],data[1],data[2],data[3],data[4],data[5],data[15],data[26]], start_row=1, start_col=r"A", max=1000)
                            fpcy_cyjg_sheet.excel.save(file=None)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_7v9v8ywl', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_7v9v8ywl')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'写入Excel行', 'id':'canvas-node-_7v9v8ywl', 'time':block_start_time, 'error': error, 'description':r'''在 fpcy_cyjg_sheet Sheet页中，从 A i 开始写入行 [data[0],data[1],data[2],data[3],data[4],data[5],data[15],data[26]]  并保存''', 'success':node_success_flag, 'variables':{"i": str(i),"fpcy_cyjg_sheet": str(fpcy_cyjg_sheet)}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_sgmt464m', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_sgmt464m')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_sgmt464m', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_n6d7444b', error, False)
    finally: 
        rgv.set_values({"i": i})
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_n6d7444b')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'按照次数循环', 'id':'canvas-node-_n6d7444b', 'time':block_start_time, 'error': error, 'description':r'''从 2 开始到 fpcy_lines 结束，步长 1 ，每次循环的值赋值给 i''', 'success':node_success_flag, 'variables':{"fpcy_lines": str(fpcy_lines),"i": str(i)}})
    # 出现字幕
    try:
        Debug_Block_Start('canvas-node-_kvm6yo2n')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.system.dialog.subtitles(r"查验完毕，机器人正在关闭打开的文件……", fontColor='255,0,0,255', fontSize=size_changer)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_kvm6yo2n', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_kvm6yo2n')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'出现字幕', 'id':'canvas-node-_kvm6yo2n', 'time':block_start_time, 'error': error, 'description':r'''屏幕下方出现字幕 "查验完毕，机器人正在关闭打开的文件……"''', 'success':node_success_flag, 'variables':{"size_changer": str(size_changer)}})
        if (error is not None):
            sys.exit(1)
    # 激活网页
    try:
        Debug_Block_Start('canvas-node-_l8q8vz40')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if invoice_web is not None:
            visual.browser.activate(invoice_web)
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l8q8vz40', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l8q8vz40')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活网页', 'id':'canvas-node-_l8q8vz40', 'time':block_start_time, 'error': error, 'description':r'''将 invoice_web 网页切换到窗口的最前面''', 'success':node_success_flag, 'variables':{"invoice_web": str(invoice_web)}})
        if (error is not None):
            sys.exit(1)
    # 输入热键
    try:
        Debug_Block_Start('canvas-node-_ckc0n3q0')
        node_success_flag = True
        sleep(2)
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rpa.ui.win32.send_key(r"^{w}")
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_ckc0n3q0', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_ckc0n3q0')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_ckc0n3q0', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "^{w}"''', 'success':node_success_flag, 'variables':{}})
        if (error is not None):
            sys.exit(1)
    # 捕获异常和重试
    try:
        Debug_Block_Start('canvas-node-_l343br0h')
        node_success_flag = True
        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            # 捕获异常和重试
            try:
                Debug_Block_Start('canvas-node-_z3g7n1bn')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                try:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_8ign5uc0')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(os.path.basename(fp_excel_path).split('.')[0], mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_8ign5uc0', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_8ign5uc0')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_8ign5uc0', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(fp_excel_path).split('.')[0] 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    # 激活窗口
                    try:
                        Debug_Block_Start('canvas-node-_lmr7b4i1')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fp_win is not None: fp_win.activate()
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lmr7b4i1', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lmr7b4i1')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_lmr7b4i1', 'time':block_start_time, 'error': error, 'description':r'''激活 fp_win 窗口''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    # 输入热键
                    try:
                        Debug_Block_Start('canvas-node-_lmr7b4i2')
                        node_success_flag = True
                        sleep(2)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.ui.win32.send_key(r"!{F4}")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lmr7b4i2', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lmr7b4i2')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lmr7b4i2', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    # 捕获异常和重试
                    try:
                        Debug_Block_Start('canvas-node-_n97qo061')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        try:
                            # 获取窗口
                            try:
                                Debug_Block_Start('canvas-node-_5q6vqvm1')
                                node_success_flag = True
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                fp_win = visual.window.catch(os.path.basename(fpcy_excel_path)[13:19], mode="substr", process_name="", class_name="", timeout=5)
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_5q6vqvm1', error, False)
                            finally: 
                                rgv.set_values({"fp_win": fp_win})
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_5q6vqvm1')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_5q6vqvm1', 'time':block_start_time, 'error': error, 'description':r'''根据 os.path.basename(fpcy_excel_path)[13:19] 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                                if (error is not None):
                                    sys.exit(1)
                            # 激活窗口
                            try:
                                Debug_Block_Start('canvas-node-_filys6i5')
                                node_success_flag = True
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if fp_win is not None: fp_win.activate()
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_filys6i5', error, False)
                            finally: 
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_filys6i5')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_filys6i5', 'time':block_start_time, 'error': error, 'description':r'''激活 fp_win 窗口''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                                if (error is not None):
                                    sys.exit(1)
                            # 输入热键
                            try:
                                Debug_Block_Start('canvas-node-_uyzu88oo')
                                node_success_flag = True
                                sleep(2)
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                rpa.ui.win32.send_key(r"!{F4}")
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_uyzu88oo', error, False)
                            finally: 
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_uyzu88oo')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_uyzu88oo', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                                if (error is not None):
                                    sys.exit(1)
                            pass
                        except:
                            # 记录日志
                            try:
                                Debug_Block_Start('canvas-node-_l343br0q')
                                node_success_flag = True
                                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                logger.info(r''' ''')
                            except (SDKError, Exception) as e:
                                node_success_flag = False
                                error = '{0}'.format(e)
                                Debug_Block_Error('canvas-node-_l343br0q', error, False)
                            finally: 
                                if node_success_flag == True:
                                    Debug_Block_Success('canvas-node-_l343br0q')
                                    error = None
                                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_l343br0q', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                                if (error is not None):
                                    sys.exit(1)
                            pass
                        finally:
                            pass
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_n97qo061', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_n97qo061')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_n97qo061', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
                    pass
                except:
                    # 获取窗口
                    try:
                        Debug_Block_Start('canvas-node-_76m71oyk')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        fp_win = visual.window.catch(r"WPS", mode="substr", process_name="", class_name="", timeout=5)
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_76m71oyk', error, False)
                    finally: 
                        rgv.set_values({"fp_win": fp_win})
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_76m71oyk')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'获取窗口', 'id':'canvas-node-_76m71oyk', 'time':block_start_time, 'error': error, 'description':r'''根据 "WPS" 查找打开的窗口标题，将查找到的窗口对象赋值给 fp_win''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    # 激活窗口
                    try:
                        Debug_Block_Start('canvas-node-_lmr7b4i3')
                        node_success_flag = True
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if fp_win is not None: fp_win.activate()
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lmr7b4i3', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lmr7b4i3')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'激活窗口', 'id':'canvas-node-_lmr7b4i3', 'time':block_start_time, 'error': error, 'description':r'''激活 fp_win 窗口''', 'success':node_success_flag, 'variables':{"fp_win": str(fp_win)}})
                        if (error is not None):
                            sys.exit(1)
                    # 输入热键
                    try:
                        Debug_Block_Start('canvas-node-_lmr7b4i4')
                        node_success_flag = True
                        sleep(2)
                        block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        rpa.ui.win32.send_key(r"!{F4}")
                    except (SDKError, Exception) as e:
                        node_success_flag = False
                        error = '{0}'.format(e)
                        Debug_Block_Error('canvas-node-_lmr7b4i4', error, False)
                    finally: 
                        if node_success_flag == True:
                            Debug_Block_Success('canvas-node-_lmr7b4i4')
                            error = None
                        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'输入热键', 'id':'canvas-node-_lmr7b4i4', 'time':block_start_time, 'error': error, 'description':r'''执行快捷键 "!{F4}"''', 'success':node_success_flag, 'variables':{}})
                        if (error is not None):
                            sys.exit(1)
                    pass
                finally:
                    pass
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_z3g7n1bn', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_z3g7n1bn')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_z3g7n1bn', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})
            pass
        except:
            # 记录日志
            try:
                Debug_Block_Start('canvas-node-_l343br0p')
                node_success_flag = True
                block_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logger.info(r''' ''')
            except (SDKError, Exception) as e:
                node_success_flag = False
                error = '{0}'.format(e)
                Debug_Block_Error('canvas-node-_l343br0p', error, False)
            finally: 
                if node_success_flag == True:
                    Debug_Block_Success('canvas-node-_l343br0p')
                    error = None
                rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'记录日志', 'id':'canvas-node-_l343br0p', 'time':block_start_time, 'error': error, 'description':r'''记录日志''', 'success':node_success_flag, 'variables':{}})
                if (error is not None):
                    sys.exit(1)
            pass
        finally:
            pass
    except (SDKError, Exception) as e:
        node_success_flag = False
        error = '{0}'.format(e)
        Debug_Block_Error('canvas-node-_l343br0h', error, False)
    finally: 
        if node_success_flag == True:
            Debug_Block_Success('canvas-node-_l343br0h')
            error = None
        rpa_v33.agent.send('VisualDebug', 'DetailDebugLog', {'name':'捕获异常和重试', 'id':'canvas-node-_l343br0h', 'time':block_start_time, 'error': error, 'description':r'''执行并捕获异常 ''', 'success':node_success_flag, 'variables':{}})