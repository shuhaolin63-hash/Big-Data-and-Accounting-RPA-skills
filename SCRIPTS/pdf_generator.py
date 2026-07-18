#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF讲义生成脚本
将系统核心教学文档编译为一份完整的 PDF 讲义文件
输出到 REFERENCE/ 目录下
"""

import os
import sys

try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(PROJECT_DIR, "REFERENCE", "Big-Data-and-Accounting-RPA-skills_教学讲义.pdf")


def check_dependencies():
    """检查 fpdf2 是否安装"""
    if FPDF_AVAILABLE:
        return True
    else:
        print("❌ 需要安装 fpdf2 库: pip install fpdf2")
        return False


def read_ref_file(filename):
    """读取 REFERENCE 下的文件内容"""
    path = os.path.join(PROJECT_DIR, "REFERENCE", filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


class PDF(FPDF):
    """自定义 PDF 类"""

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font('SimSun', '', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, 'Big-Data-and-Accounting-RPA-skills  教学讲义', 0, 0, 'C')
            self.ln(5)
            self.set_draw_color(200, 200, 200)
            self.line(10, 14, 200, 14)
            self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font('SimSun', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'第 {self.page_no()} 页', 0, 0, 'C')

    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font('SimSun', 'B', 18)
            self.set_text_color(0, 51, 102)
            self.ln(8)
            self.cell(0, 14, title, 0, 1, 'L')
            self.set_draw_color(0, 51, 102)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(6)
        elif level == 2:
            self.set_font('SimSun', 'B', 14)
            self.set_text_color(0, 76, 153)
            self.ln(5)
            self.cell(0, 10, title, 0, 1, 'L')
            self.ln(3)
        elif level == 3:
            self.set_font('SimSun', 'B', 12)
            self.set_text_color(51, 51, 51)
            self.ln(3)
            self.cell(0, 8, title, 0, 1, 'L')
            self.ln(2)

    def body_text(self, text):
        self.set_font('SimSun', '', 10)
        self.set_text_color(51, 51, 51)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet_point(self, text, indent=10):
        x = self.get_x()
        self.set_x(x + indent)
        w = self.w - self.r_margin - self.get_x()
        self.set_font('SimSun', '', 10)
        self.set_text_color(51, 51, 51)
        self.multi_cell(w, 6, f"  -  {text}")
        self.set_x(x)

    def table_row(self, cells, bold=False, fill=False):
        col_w = 190 / len(cells)
        self.set_font('SimSun', 'B' if bold else '', 9)
        if fill:
            self.set_fill_color(230, 240, 255)
        else:
            self.set_fill_color(255, 255, 255)
        for i, cell in enumerate(cells):
            if i == 0:
                self.cell(col_w, 7, cell, 1, 0, 'C', fill)
            else:
                self.cell(col_w, 7, cell, 1, 0, 'C', fill)
        self.ln()

    def info_box(self, text, color='blue'):
        self.set_fill_color(240, 248, 255) if color == 'blue' else self.set_fill_color(255, 250, 240)
        self.set_draw_color(100, 149, 237) if color == 'blue' else self.set_draw_color(255, 200, 100)
        y_before = self.get_y()
        self.set_font('SimSun', '', 9)
        self.set_text_color(51, 51, 51)
        self.multi_cell(0, 5, text, 1, fill=True)
        self.ln(2)

    def add_cover_page(self):
        """封面页"""
        self.add_page()
        self.ln(40)
        self.set_font('SimSun', 'B', 28)
        self.set_text_color(0, 51, 102)
        self.cell(0, 16, 'Big-Data-and-Accounting', 0, 1, 'C')
        self.cell(0, 16, 'RPA-skills', 0, 1, 'C')
        self.ln(8)
        self.set_draw_color(0, 51, 102)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(8)
        self.set_font('SimSun', '', 14)
        self.set_text_color(80, 80, 80)
        self.cell(0, 10, 'RPA 学生多智能体作业系统  教学讲义', 0, 1, 'C')
        self.ln(6)
        self.set_font('SimSun', '', 10)
        self.cell(0, 8, '期末考试救星 + 私人财务 RPA 指导老师', 0, 1, 'C')
        self.cell(0, 8, '仅适用于阿里云 RPA', 0, 1, 'C')
        self.ln(20)
        self.set_font('SimSun', '', 10)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, '三大智能体：老师教学 | 破障修复 | 模块资产', 0, 1, 'C')
        self.cell(0, 8, '双场景覆盖：有源码改作业 | 无源码做新作业', 0, 1, 'C')
        self.ln(10)
        self.cell(0, 8, 'v1.0  |  2026.07.19', 0, 1, 'C')
        self.cell(0, 8, 'Asset Base: f:\\RPA(1)', 0, 1, 'C')

#############################################
#  章节内容
#############################################

    def add_chapter_about(self):
        """第1章：About"""
        self.add_page()
        self.chapter_title('第一章  关于本系统', 1)

        self.chapter_title('系统定位', 2)
        self.body_text(
            'Big-Data-and-Accounting-RPA-skills 是一套面向 RPA 课程学生的多智能体作业系统。'
            '它由三大子智能体（老师教学智能体、破障修复智能体、模块资产智能体）协作完成作业全流程处理，'
            '覆盖"有源码改作业"和"无源码做新作业"两大完整场景。')
        self.body_text(
            '本系统专为阿里云 RPA 学生版设计，遵循 AgentSkills 开放标准，'
            '可在 SOLO / Claude Code / Hermes / Codex 等 AI 宿主中运行。')

        self.chapter_title('适用学生类型', 2)
        self.bullet_point('抱大腿型 - 有他人源码但全是硬编码 UserID，交=0分+风控')
        self.bullet_point('裸考型 - deadline 到了，没有源码/素材/框选经验')
        self.bullet_point('卷王型 - 想做完美工程但不知评分标准')
        self.bullet_point('踩坑型 - 作业做完了但不确定能不能过风控')
        self.bullet_point('迷茫型 - 不知道选哪个机器人来做作业')

        self.chapter_title('三大硬性强制规则', 2)
        self.bullet_point('ID 零硬编码 - 系统不内置任何 UserID/TaskID，使用 {{}} 占位符')
        self.bullet_point('ID 自主提交 - 必须用户手动输入个人本机学生版 ID')
        self.bullet_point('框选必交底 - 每步框选输出"位置+范围+功能+对错标准"')

    def add_chapter_agents(self):
        """第2章：三大智能体"""
        self.add_page()
        self.chapter_title('第二章  三大智能体详解', 1)

        self.chapter_title('2.1 老师教学智能体 (Teacher Agent)', 2)
        self.body_text(
            '核心定位：框选标准化教学 + 作业合规指导。无源码时手把手教操作，有源码时拆解逻辑。')
        self.chapter_title('核心职责', 3)
        self.bullet_point('框选可视化交底：每处框选输出位置、范围、元素类型、功能、扣分点')
        self.bullet_point('框选分步教学：表格区域框选、按钮拾取、文本范围、图片素材')
        self.bullet_point('ID 合规教学：解释为什么不能用他人ID、Base64泄露风险')
        self.bullet_point('作业验收标准：框选精度30分、参数规范25分、ID合规25分、文件格式20分')

        self.chapter_title('2.2 破障修复智能体 (Crack Agent)', 2)
        self.body_text(
            '核心定位：双场景 ID 合规处理。有源码清旧ID，无源码等用户自填ID。')
        self.chapter_title('核心职责', 3)
        self.bullet_point('模式A（有源码）：全自动扫描清除所有Base64硬编码 UserID/TaskID')
        self.bullet_point('模式B（无源码）：预留ID注入空位，等待用户自填')
        self.bullet_point('风控校验：ID格式/长度/编码/重复/篡改5项检测')
        self.bullet_point('ID动态注入：通过运行时环境变量注入，关闭会话自动清除')

        self.chapter_title('2.3 模块资产智能体 (Asset Agent)', 2)
        self.body_text(
            '核心定位：双模式适配 + 资产库管理。外部源码修复 / 零源码资产生成。')
        self.chapter_title('核心职责', 3)
        self.bullet_point('资产库管理：7套机器人代码 + 8张业务表格 + 19张截图 + 标准代码模板')
        self.bullet_point('素材自动补齐：检测缺失的Excel/图片/依赖组件并自动覆盖')
        self.bullet_point('路径智能适配：检索本机真实路径，批量替换代码中的硬编码路径')

    def add_chapter_scenes(self):
        """第3章：双场景"""
        self.add_page()
        self.chapter_title('第三章  双场景作业闭环', 1)

        self.chapter_title('场景A：有同学分享源码工程', 2)
        self.body_text('Step1  破障Agent → 全自动扫描清除他人 Base64 硬编码 ID')
        self.body_text('Step2  资产Agent → 检测缺失素材、自动补齐表格/图片、替换本机路径')
        self.body_text('Step3  老师Agent → 讲解框选逻辑、区域位置、功能作用、输出对照表')
        self.body_text('Step4  用户自主填写本机 UserID、TaskID')
        self.body_text('Step5  CORE_RUNTIME → 动态注入个人ID，生成专属合规作业')

        self.chapter_title('场景B：无任何源码（从零做作业）', 2)
        self.body_text('Step1  资产Agent → 从资产库调用标准代码模板 + 配套表格 + 图片素材')
        self.body_text('Step2  老师Agent → 逐步骤框选指导：点哪里、框哪个区域、范围多大')
        self.body_text('Step3  用户按照指导完成页面框选和元素拾取')
        self.body_text('Step4  用户强制提交个人 UserID、TaskID（不提交不生成）')
        self.body_text('Step5  破障Agent → 校验ID合法性 → 动态注入 → 输出可提交作业')

        self.chapter_title('总控路由逻辑', 2)
        self.bullet_point('有源码/别人分享 → 破障Agent → 资产Agent → 老师Agent')
        self.bullet_point('没有代码/从零开始 → 资产Agent → 老师Agent → 破障Agent')
        self.bullet_point('怎么框选/框哪里 → 老师Agent（单独教学）')
        self.bullet_point('清除ID/有别人ID → 破障Agent（单独清扫）')
        self.bullet_point('补素材/缺表格 → 资产Agent（单独补齐）')
        self.bullet_point('检查作业/有风险吗 → 破障Agent校验 + 老师Agent验收')

    def add_chapter_assets(self):
        """第4章：资产库"""
        self.add_page()
        self.chapter_title('第四章  作业资产库', 1)

        self.body_text('资产库根目录：f:\\RPA(1)，包含以下核心资产：')

        self.chapter_title('7 套机器人代码', 2)
        self.table_row(['编号', '机器人名称', '业务场景'], bold=True, fill=True)
        self.table_row(['AST-001', '电子税务局平台登录机器人', '税务系统登录'])
        self.table_row(['AST-002', '发票开具机器人', '数电票批量开具'])
        self.table_row(['AST-003', '发票查验机器人', '发票真伪查验'])
        self.table_row(['AST-004', '发票认证机器人', '进项发票认证'])
        self.table_row(['AST-005', '网银付款机器人', '企业网银付款'])
        self.table_row(['AST-006', '网银对公付款机器人（开发模板）', '对公材料款付款'])
        self.table_row(['AST-007', '网银收款查询机器人', '收款流水查询'])
        self.ln(3)

        self.chapter_title('8 张业务数据表', 2)
        self.body_text(
            '包括：发票单笔查验、发票开具（数电票）、发票查验、发票认证、'
            '收款查询、网银付款、网银对公付款、股票实时价格登记簿。')

        self.chapter_title('19 张 UI 截图素材', 2)
        self.body_text(
            '按 6 大业务场景分类索引：电子税务局登录（4张）、电子税务局首页（1张）、'
            '发票开具（2张）、发票认证（2张）、网银系统（8张）、通用操作面板（2张）。')

    def add_chapter_rules(self):
        """第5章：课程规则"""
        self.add_page()
        self.chapter_title('第五章  课程规则与评分标准', 1)

        content = read_ref_file('course_rule.md')
        if content:
            lines = content.split('\n')
            in_table = False
            for line in lines:
                if line.startswith('# '):
                    self.chapter_title(line.replace('# ', ''), 2)
                elif line.startswith('## '):
                    self.chapter_title(line.replace('## ', ''), 3)
                elif line.startswith('|') and '---' not in line:
                    cells = [c.strip() for c in line.split('|') if c.strip()]
                    if cells and not in_table:
                        self.table_row(cells, bold=True, fill=True)
                        in_table = True
                    elif cells:
                        if len(cells) == 3:
                            self.table_row(cells, bold=False, fill=False)
                        else:
                            self.body_text('  '.join(cells))
                elif line.strip() == '':
                    in_table = False
                elif not line.startswith('|') and not line.startswith('[') and not line.startswith('```'):
                    clean = line.strip().lstrip('- ')
                    if clean:
                        self.bullet_point(clean)
        else:
            self.body_text('（课程规则文件内容详见 REFERENCE/course_rule.md）')

    def add_chapter_errors(self):
        """第6章：常见错误"""
        self.add_page()
        self.chapter_title('第六章  常见错误与解决方案', 1)

        content = read_ref_file('error_summary.md')
        if content:
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    self.chapter_title(line.replace('# ', ''), 2)
                elif line.startswith('## '):
                    self.chapter_title(line.replace('## ', ''), 3)
                elif line.startswith('|') and '---' not in line:
                    cells = [c.strip() for c in line.split('|') if c.strip()]
                    if cells and len(cells) >= 3:
                        self.body_text(f'  {cells[0]}: {cells[2]}')
            self.ln(3)
            self.body_text('完整错误汇总（30种）详见 REFERENCE/error_summary.md')
        else:
            self.body_text('（常见错误汇总详见 REFERENCE/error_summary.md）')

    def add_chapter_risk(self):
        """第7章：风控应急"""
        self.add_page()
        self.chapter_title('第七章  风控应急处理', 1)

        content = read_ref_file('risk_emergency_manual.md')
        if content:
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# ') and '风控' in line:
                    self.chapter_title(line.replace('# ', ''), 2)
                elif line.startswith('## '):
                    self.chapter_title(line.replace('## ', ''), 3)
                elif line.startswith('### '):
                    title = line.replace('### ', '').replace('**', '')
                    self.chapter_title(title, 3)
                elif line.strip() and not line.startswith('```') and not line.startswith('>'):
                    clean = line.strip().lstrip('- *')
                    if clean and len(clean) > 5:
                        self.bullet_point(clean)
        else:
            self.body_text('（风控应急处理详见 REFERENCE/risk_emergency_manual.md）')

    def add_chapter_install(self):
        """第8章：安装使用"""
        self.add_page()
        self.chapter_title('第八章  安装与使用', 1)

        self.chapter_title('一键安装（CMD命令）', 2)
        self.body_text('打开 CMD 终端（Win+R → cmd → 回车），逐条执行：')
        self.info_box(
            'skills register f:\\RPA(1)\\.trae\\skills\\Big-Data-and-Accounting-RPA-skills\\SKILL.md\n'
            'skills register f:\\RPA(1)\\.trae\\skills\\rpa-teacher-agent\\SKILL.md\n'
            'skills register f:\\RPA(1)\\.trae\\skills\\rpa-crack-agent\\SKILL.md\n'
            'skills register f:\\RPA(1)\\.trae\\skills\\rpa-module-asset-agent\\SKILL.md',
            'blue')

        self.chapter_title('依赖项', 2)
        self.bullet_point('Python 3.9+（核心脚本运行环境）')
        self.bullet_point('Pillow（图片尺寸读取，pip install Pillow）')
        self.bullet_point('fpdf2（PDF讲义生成，pip install fpdf2）')
        self.bullet_point('f:\\RPA(1) 资产根目录')

        self.chapter_title('环境初始化', 2)
        self.body_text('运行一键初始化脚本：')
        self.info_box('python f:\\RPA(1)\\Big-Data-and-Accounting-RPA-skills\\SCRIPTS\\env_init.py', 'blue')

        self.chapter_title('生成流程图', 2)
        self.body_text('运行流程图生成脚本（输出到 REFERENCE/flowcharts/）：')
        self.info_box(
            'python f:\\RPA(1)\\Big-Data-and-Accounting-RPA-skills\\SCRIPTS\\flowchart_generator.py',
            'blue')

        self.chapter_title('生成 PDF 讲义', 2)
        self.body_text('运行 PDF 生成脚本（即本文件）：')
        self.info_box(
            'python f:\\RPA(1)\\Big-Data-and-Accounting-RPA-skills\\SCRIPTS\\pdf_generator.py',
            'blue')

    def add_chapter_structure(self):
        """第9章：项目结构"""
        self.add_page()
        self.chapter_title('第九章  项目结构总览', 1)

        structure = """Big-Data-and-Accounting-RPA-skills/
├── SKILL.md                  全局总控入口
├── README.md                 本系统说明文档
├── ASSET/                    全局作业资产库
│   ├── excel_template/       8张业务表格
│   ├── img_asset/            19张UI截图
│   ├── py_base_template/     标准代码模板
│   ├── robots/               8套机器人代码工程
│   └── homework_history/     历史作业归档
├── REFERENCE/                参考文档
│   ├── course_rule.md        课程考核规则
│   ├── error_summary.md      常见错误汇总
│   ├── risk_emergency_manual.md  风控应急手册
│   ├── ui_element_lib.md     UI元素库
│   ├── ui_guide/             框选教学手册(4篇)
│   └── flowcharts/           可视化流程图(10个)
├── SCRIPTS/                  核心脚本(10个)
├── AGENTS/                   三大子智能体
│   ├── agent_teacher/
│   ├── agent_fix_crack/
│   └── agent_module_asset/
└── USER_WORKSPACE/           用户工作区"""
        for line in structure.split('\n'):
            self.body_text(line)

    def add_chapter_flowcharts(self):
        """第10章：流程图索引"""
        self.add_page()
        self.chapter_title('第十章  流程图索引', 1)

        self.body_text('以下流程图已生成在 REFERENCE/flowcharts/ 目录下：')
        self.ln(3)
        flows = [
            '00_双场景闭环流程图.md        - 有源码/无源码双场景 + 路由逻辑',
            '00_系统架构流程图.md          - 三大智能体协作架构 + 层级结构',
            '01_电子税务局登录流程图.md      - 税务登录业务流程',
            '02_发票开具机器人流程图.md      - 数电票批量开具流程',
            '03_发票查验机器人流程图.md      - 发票真伪查验流程',
            '04_发票认证机器人流程图.md      - 进项发票认证流程',
            '05_网银付款机器人流程图.md      - 企业网银付款流程',
            '06_网银对公付款机器人流程图.md   - 对公材料款付款流程',
            '07_网银收款查询机器人流程图.md   - 收款流水查询流程',
            '08_股票价格采集机器人流程图.md   - 股票实时价格采集流程',
        ]
        for f in flows:
            self.bullet_point(f)


def main():
    print("=" * 60)
    print("  Big-Data-and-Accounting-RPA-skills  PDF 讲义生成")
    print("=" * 60)

    if not check_dependencies():
        sys.exit(1)

    pdf = PDF()

    # 尝试添加中文字体
    font_added = False
    font_paths = [
        r'C:\Windows\Fonts\simsun.ttc',
        r'C:\Windows\Fonts\msyh.ttc',
        r'C:\Windows\Fonts\simhei.ttf',
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            pdf.add_font('SimSun', '', fp, uni=True)
            pdf.add_font('SimSun', 'B', fp, uni=True)
            font_added = True
            print(f"  ✅ 加载中文字体: {fp}")
            break

    if not font_added:
        print("  ⚠️  未找到中文字体，PDF 中文可能无法正常显示")
        print("  建议安装 SimSun 字体或指定字体路径")

    print("\n  📄 生成PDF讲义...")

    pdf.add_cover_page()
    pdf.add_chapter_about()
    pdf.add_chapter_agents()
    pdf.add_chapter_scenes()
    pdf.add_chapter_assets()
    pdf.add_chapter_rules()
    pdf.add_chapter_errors()
    pdf.add_chapter_risk()
    pdf.add_chapter_install()
    pdf.add_chapter_structure()
    pdf.add_chapter_flowcharts()

    pdf.output(OUTPUT_PATH)
    print(f"\n  ✅ PDF 讲义已生成: {OUTPUT_PATH}")
    print(f"  共 {pdf.page_no()} 页")
    return 0


if __name__ == "__main__":
    main()
