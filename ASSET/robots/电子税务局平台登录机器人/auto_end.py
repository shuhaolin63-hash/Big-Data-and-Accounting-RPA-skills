"""
RPA中的判分扩展包
"""
import os
import sys
import shutil
import time
import traceback
import base64
from tkinter import *
import tkinter.filedialog
import win32api
import win32con
import requests
import json
from datetime import datetime
import zipfile
from requests.adapters import HTTPAdapter

rs = requests.Session()
rs.mount('http://', HTTPAdapter(max_retries=1))
timeout = 90


def minimize_win():
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)


class App:
    def __init__(self, *args, **kwargs):
        self.filename = os.path.dirname(__file__)
        self.rzfile = os.path.join(self.filename, 'rzgc.variable.json')
        self.rzgc_json = self.read_json()
        self.assess_id = self.rzgc_json.get('assess_id')
        self.utask_id = self.rzgc_json.get('utask_id')
        self.exam_paper_record_id = self.rzgc_json.get('exam_paper_record_id')
        if not (self.assess_id or self.exam_paper_record_id):
            return

        self.host = self.rzgc_json.get('host')
        self.host = self.host if self.host.startswith('http://') else 'http://' + self.host
        self.username = base64.b64decode(self.rzgc_json.get('auth')[0].encode('utf8')).decode('utf8')

        # self.headers = {'Authorization': 'JWT ' + self.rzgc_json.get('token')}

        self.rpa_data = kwargs.get('rpa_data')
        self.run_state = kwargs.get('run_state')
        self.bus_excel = kwargs.get('bus_excel')
        self.ask_file = kwargs.get('ask_file')
        self.err_html = 'C:/RPADATA/error.html'

        res = self.eval_score()
        self.show(res)

    def show(self, res):
        """
        :param res: 测评响应json
        :return:
        """
        bg = '#ffffff'
        fg = '#000'
        fg_title = '#37185b'
        w = 500
        h = 320
        text_title = res.get('title') or '遇到问题了'
        text_main = '        ' + res.get('text') or '测评服务遇到问题了，请稍后再试！'
        img_qx_ok = 'iVBORw0KGgoAAAANSUhEUgAAAFoAAAAdCAMAAAAdK4vkAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAqUExURQAAADgYXDcYWzcYW2dPgot5oI18oqqdur61ysK4zdPM2+Ld5/Du8////6dUqQcAAAADdFJOUwBWzIRFsJcAAAAJcEhZcwAAFxEAABcRAcom8z8AAAEhSURBVEhL7ZbRkoMgDEVRWCiE/P/v7g2hLbWhT/DmGcdmHD25IEx17jj9Bs4D5l4v53BbMgun68UGbvWFmToyB4pEKCnqJRALTgWnxMETv5DLX5jqhLu9DyWiQwgovc9iqL4k9FRqu1UgfjcfmKUWH9RyFg/ljF6wNeEwDlyVGBamehgqCAnap1qHBJ6h8xD/k1+pc9JatKou8KQ2sdpG3ok5z8IvtaStfxqyp8bxmTpOZgNM1JhAJqwHgrG1GNSX1PprYKox7vZErU1TsNLWpW4TEhg+FBzrstQATxBjc0BRMo6FqWtkrI+aYski4b5lKsv+HEi9hYGpxkvsS4r5obE0NTZR6yHAKXVfoAaz1Au41Rd2/u1u/FjY+IlzM+LcP/igJBsriNbMAAAAAElFTkSuQmCC'
        img_qx_run_err = 'iVBORw0KGgoAAAANSUhEUgAAAFcAAAAeCAIAAADW/RWfAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAEXRFWHRTb2Z0d2FyZQBTbmlwYXN0ZV0Xzt0AAAOySURBVFiF7ZkxaBNRGMd/LRYHU4UOl6lYpARsEcmg3tJarFOoHh2yhk62urwizWIgZPCmdGgGhxSEo4MORZosAcFBWzzq0tAhCMcpigaNi0KUVhzicK85k6bV5sQDkx8Z3nv37t3//fN9773jemq1Gh3PMbe4s4Nlsbvrn5h/SCDA6Gi9tufC3busrPgjyEfm57l1C+gFWFzsRAuApSUePUK6sL7usxofefIE6cL79z5L8ZFyGelCJ28Tvb1IFzqergvg1QVNY2MDTZPlYhHLkr9SCSFa3CIEa2uHjSkEL17IMQ9CVdnYQNc9SG/AmwvT0wSDpNMYBvk8N29i28TjxGJ8/Ah/MOf9ZDK8fMnsbHO7rrsWr6wQDBKNui3F4m+MO5Rjv+9yEEJw6hSxGMmknGowCFCpAHz/zps35POEwxgGa2ukUpw4Ie+1LADbJhJBCG7coK+veXynD/DjB8vLAKbJzAyaxp07PHhAJiM7qCrJZPsTgZ5arUY4zLdvR761UGB42K2aJorCp08oCsPDcoZ1idks+TyAEExMMD3tFupoGgsLLC7Knoc/bj+rqyQSR57FyAi5nIdYyGZZWGB9HVVle5upKWybmZnmbpub0o4/oVqVobQfZxDDANynCMH16yQSbG4eTXwjHlwAAgGiUYDBQUyTclmq5Behqsr8PEtLUqiicPx469GGhjh9uvksX48ph2fPuHzZTZZKhXjcowV4deHrVwoFGQsDA4TDbtBalkzjS5f48oVksiGe69MolVhelhmuKLx92zDnuqfQsHw4K0UmgxDcv09fX5vpsMffi4VSif5+4nGZ6vVYmJjg6VPm5gBUlXSaarVFjqgq4+O8enXgszIZdzkEDANdJ5FoaGwXby58+MDz51y5wvY2588zMEA6LS9ZFpUKuRy7u67QuTmqVYpFDKN5Bbl2jUCgeVtVFIpFWW65Ojr/gYMTem3h4bxw8SKArjM5yc4O794xOkoohGlimoRCjI1x7hyvX8PeOUdRiERk6P66w+s60SiFQsPuoKr097vVSIRQiFCI1VUqFba22Nri82ficdnergV4ioUzZ8hmYe9fMs0WfRxlhsGFC27+O+2aRirF7CyPHxOJcO+evOo44mDb0jInlZzziG0zNoZhUC7z8CGplAxAD7Hg4bzwfzAyQi7XfZuC7julQ9cF6Lrg0AswOOi3DP8YGkK6MDnprxI/uXoV6YIQxGI+q/GF27eZmkKeFxw66gvdyZOcPVuv9XS/1gI/ARwybRqW2UgPAAAAAElFTkSuQmCC'
        img_qx_ass_err = 'iVBORw0KGgoAAAANSUhEUgAAAFYAAAAeCAIAAAA5P36hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAEXRFWHRTb2Z0d2FyZQBTbmlwYXN0ZV0Xzt0AAAMSSURBVFiF7Zk/SDphGMc/Sn8Io5b+0BJFLRUYhsMRVM4RHELubg4OLrUkhAg3WYNEhNutZhA23BbUktISNEVYkRAkbZGELf6GO7o8r0yNLn76weG995737nme9/s+751nK5fLtDYdevP+nkKBVshIZyejowwMqEcdAKenbGzw9GSlW7+P2832NiMjtvLdHaLI66vVHlmB08nBgZ1MpkXjBy4veX62c3NjtSOWcntrp6fHai8spVy2W+2C9bRT8FMpEEUUBUEw9ssy19ef/mRZs5EkzV6SUBStLQgcHxMKmZxSzyoKoti877by1haJRN3jRJFIBIfjU4NCgfV1slm9JxTC48HrNVoKApLE0RHxOKDlxe9HUbi4IBzWzCQJl4tolFiM4WHjRc7O8PvrjgJIJjtqG5mSTpNO685NT9PdTamELOv96imfr2Lg9bXeVv3OZjk6wuPB5WJ+vsJschKfj1RKS8TICH4/CwsAgsDmJolExe0aolEVqKgR5nIkEgQC7O9ruo1EjJ5JEouLRl18RnV4sszUFMDbG729Jup7T1O9JJONpqB6eg0Ui2QyLC3R2fmV2fk5MzM4HKRSnJ+bLK5ikUgEr5ehIYDlZa3/p1TQeApUDg85OdHW8DuyzMNDxZyEw7y8VJiJIoEA0agmCsOQ6vAODymV6OsjkTCvQdWl55s0XgtUursJBgkGjf2plN4WRVZXcTiMZoVCHTfyerVymE4TCFSUSVFkbY2trUbiBypelhugVGJ310QFH/H7eXtDlk1UYEBRmJzUD2MxYjGAXE7Xv4rPV7EMi8VGA4BmU1BTBYrC1RUDAyZmBhWoz+nr66TTtdf5x+KnqqAJmkuBYXIMhELk8+zvMztrFEu1ClZWSKW+W9v+hAq+syNEIsTjCAJdXTVU0N9vsqC+4E+oIBz+7j6czWoPM19geGTMZmvoS+V9GnK5ZrbG5jbF/4Bksv2m2H5ZbqcAsDM+brUPljIxYWdurnX/PnQ66euzMzbG3h6Dg1a78+u43ezsADb9m2I+z+NjC35Qs7U/q/4D1JFUih2MKQsAAAAASUVORK5CYII='
        img_icon = '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'
        img_bg = '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'

        # 响应code：200成功，201失败(不打开网页)，201失败(运行类，打开解决方案)，202失败(数据类，打开错误详情)
        res_code = res.get('code')
        fg_title2 = 'green' if res_code == 200 else 'red'  # 标题字体颜色
        if res_code > 201 and os.path.isfile(self.err_html):
            img_qx = img_qx_run_err if res_code == 202 else img_qx_ass_err  # 按钮图片-我知道了
            command = self.open_html  # 打开网页并退出
        else:
            command = self.end  # 按钮图片-查看详情
            img_qx = img_qx_ok  # 不打开网页直接退出

        root = Tk()
        self.root = root
        pimg_icon = PhotoImage(data=img_icon)
        root.iconphoto(False, pimg_icon)
        root.overrideredirect(True)
        root.geometry(
            '{}x{}+{}+{}'.format(w, h, (root.winfo_screenwidth() - w) // 2, (root.winfo_screenheight() - h) // 2))
        root.resizable(False, False)
        root.attributes('-topmost', True)
        root.after(0, lambda: root.focus_force())

        # label添加背景图
        pimg = PhotoImage(data=img_bg)
        bgi = Label(root, image=pimg)
        bgi.place(x=-2, y=-2)

        # logo标题：融智机器人
        title = Label(root, text='融智机器人', fg=fg_title, font=('微软雅黑', 13)).place(x=43, y=13)

        # 右上角关闭
        root.protocol("WM_DELETE_WINDOW", self.end)
        qb = Button(text='×', font=('微软雅黑', 15), fg=fg_title, border=0, command=self.end).place(x=455, y=5)

        # 居中标题：用户验证
        title = Label(root, text=text_title, bg=bg, fg=fg_title2, font=('微软雅黑', 13, ''), ).place(x=166, y=78)

        # hi
        hi = Label(root, text=self.username + '，您好！', bg=bg, font=('微软雅黑', 11, '')).place(x=44, y=116)
        text2 = Text(root, font=('微软雅黑', 11), fg=fg, bg=bg, width=47, height=6, bd=0, padx=0, pady=3, spacing2=10,
                     selectbackground=fg, selectforeground=bg)
        text2.insert(0.0, text_main)
        text2['state'] = DISABLED
        text2.place(x=47, y=147)
        # 遮盖背景机器人用
        text3 = Text(root, font=('微软雅黑', 11), fg=fg, bg=bg, width=47, height=2, bd=0, padx=0, pady=3, spacing2=10,
                     selectbackground=fg, selectforeground=bg)
        text3['state'] = DISABLED
        text3.place(x=47, y=270)

        # 我知道了
        pimg_qx = PhotoImage(data=img_qx)
        b2 = Button(root, image=pimg_qx, border=0, bg=bg, command=command, text='我知道了来打击开发商的').place(x=205, y=273)

        root.mainloop()

    # 保存json
    def save_json(self):
        base_d = base64.b64encode(json.dumps(self.rzgc_json).encode('utf8')).decode('utf8')
        with open(self.rzfile, 'w') as f:
            f.write(base_d)

    # 提交平台判分
    def eval_score(self):
        # 清除上次的报错文件
        if os.path.isfile(self.err_html):
            os.remove(self.err_html)

        text_log = self.text_log()
        url = self.host + '/api/practice/utask/rpa/'
        down_data = self.rzgc_json.get('down_data')
        data = {'text_log': text_log, 'assess_id': self.assess_id, 'down_data': down_data, 'utask_id': self.utask_id}
        if self.exam_paper_record_id:
            start_time = self.rzgc_json.get('start_time')
            data.update({'start_time': start_time, 'exam_paper_record_id': self.exam_paper_record_id})
        files = {}
        excel_file = self.select_excel()
        if excel_file:
            files.update(excel_file)

        headers = {'Authorization': 'JWT ' + self.rzgc_json.get('token')}
        # rs.get(url=url, headers=headers, data={'down_data': down_data}, files=files, timeout=timeout)
        response = rs.post(url=url, headers=headers, data=data, files=files, timeout=timeout)
        self.res = response.json()

        html = self.res.get('html')
        if self.res.get('code') not in (200, 201) and html:
            with open(self.err_html, 'wb') as f:
                f.write(html.encode())

        if self.rzgc_json.get('task_type') == '9268cb7b0d1f49a88183486363a83b73' and not self.exam_paper_record_id:  # 上传机器人文件包
            self.up_zip()

        self.rzgc_json.update({'assess_id': '', 'utask_id': ''})
        self.save_json()
        return self.res

    def up_zip(self):
        robot_file = shutil.make_archive(self.filename, 'zip', self.filename)
        url = self.host + "/api/file/upload/"
        with open(robot_file, 'rb') as f:
            headers = {'Authorization': 'JWT ' + self.rzgc_json.get('token')}
            file = {'file': (os.path.basename(robot_file), f.read())}
            # dt = time.localtime()
            # path = 'ive/{}/{:02d}/{:02d}/{}.zip'.format(dt.tm_year, dt.tm_mon, dt.tm_mday, int(time.time()))
            # data = {'is_download': '1', 'type': 'oss', 'suffix': 'zip', 'path': path, 'name': self.filename}
            data = {'type': 'oss'}
            response = rs.post(url=url, headers=headers, files=file, timeout=timeout, data=data)
            ufile_id = response.json().get('data').get('file_id')
            if ufile_id:
                utask_id = self.rzgc_json.get('utask_id')
                classes = self.rzgc_json.get('classes')
                url = '{}/api/practice/utask/{}/'.format(self.host, utask_id)
                data = {'ufile_id': ufile_id}
                # rs.get(url=url, headers=headers, params=data, timeout=timeout)
                rs.patch(url=url, headers=headers, cookies={'classes': classes}, data=data, timeout=timeout)
        os.remove(robot_file)

    # 取消
    def end(self):
        self.root.destroy()
        sys.exit()

    def open_html(self):
        import webbrowser
        webbrowser.open(self.err_html, new=0)
        self.end()

    # 获取日志内容
    def text_log(self):
        try:
            path = os.path.expanduser('~')
            path_log = r'{}\AppData\Roaming\AlibabaCloudRPA\log\debug.log'.format(path)
            # path_log = r'c:\\RPADATA\debug.log'

            if os.path.exists(path_log):
                with open(path_log, 'rb') as f:
                    text_all = f.read().decode('utf8')
                text = text_all.split('开始调试')[-1]
                return text
            else:
                return ''
        except Exception as e:
            return ''

    # 查找表格
    def select_excel(self):
        res = {}
        if self.bus_excel:
            for i in self.bus_excel:
                file = r'C:\RPADATA\{}'.format(i)
                if not os.path.isfile(file) and self.ask_file:
                    t = Tk()
                    t.withdraw()
                    file = tkinter.filedialog.askopenfilename()
                    t.destroy()
                if os.path.isfile(file):
                    with open(file, 'rb') as f:
                        mtime = os.path.getmtime(file)
                        t = datetime(*time.localtime(mtime)[:6])
                        res[i] = (os.path.basename(file), f.read(), t)
        return res

    # 读取内置信息
    def read_json(self):
        if os.path.exists(self.rzfile):
            with open(self.rzfile, 'rb') as f:
                str_base = base64.b64decode(f.read().decode('utf8')).decode('utf8')
                return json.loads(str_base)
        return {}


def start(*args, **kwargs):
    try:
        minimize_win()
        App(*args, **kwargs)
        return
    except Exception:
        assert False, traceback.format_exc()
    finally:
        rs.close()
