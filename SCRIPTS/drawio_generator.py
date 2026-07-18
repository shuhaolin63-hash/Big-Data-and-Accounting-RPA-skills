#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RPA 流程图生成器 (draw.io XML Engine)
基于 Next AI Draw.io 的 AI + draw.io 技术路线
自动生成标准 draw.io XML 流程图，可在 app.diagrams.net 中打开编辑
"""

import os
import json
import shutil
import argparse
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

ROBOTS = {
    "tax_login": {
        "name": "电子税务局平台登录机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开 Chrome 浏览器\n访问电子税务局", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("点击 '登录头像' 按钮", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 2),
            ("填写 用户名输入框", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 3),
            ("填写 密码输入框", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 4),
            ("点击 '登录' 按钮", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("登录成功?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 6),
            ("保存 Cookie\n/ Token", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 7),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 8),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7,0.3,"是"),(7,8),(6,3,0.7,"失败重试")],
    },
    "invoice_open": {
        "name": "发票开具机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("登录电子税务局", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("打开发票开具\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 2),
            ("读取待开票数据", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 3),
            ("还有未开发票?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("填写发票信息\n购货方/金额/税率", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("提交开具", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 6),
            ("开具成功?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 7),
            ("退出电子税务局", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 8),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 9),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,4,0.3,"是"),(7,8,0.7,"否"),(4,8,0.7,"否"),(8,9)],
    },
    "invoice_check": {
        "name": "发票查验机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开发票查验\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("读取待查验\n发票数据", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 2),
            ("登录发票查验平台", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 3),
            ("还有未查验发票?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("输入发票信息\n代码/号码/校验码", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("点击 '查验' 按钮", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 6),
            ("获取查验结果\n写回Excel", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 7),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 8),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,4),(4,8,0.7,"否")],
    },
    "invoice_certify": {
        "name": "发票认证机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开发票认证\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("读取待认证\n发票数据", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 2),
            ("登录发票认证平台", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 3),
            ("还有未认证发票?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("输入发票信息\n+ 认证密钥", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 5),
            ("点击 '认证' 按钮", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 6),
            ("获取认证结果\n写回Excel", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 7),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 8),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,4),(4,8,0.7,"否")],
    },
    "bank_pay": {
        "name": "网银付款机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开网银付款\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("读取待付款数据", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 2),
            ("登录工行企业网银", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 3),
            ("还有未付款项?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("填写付款信息\n+ U盾密码", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 5),
            ("确认付款", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 6),
            ("付款成功?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 7),
            ("查询付款信息", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 8),
            ("退出企业网银", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 9),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 10),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,4,0.3,"是"),(7,8,0.7,"否"),(4,8,0.7,"否"),(8,9),(9,10)],
    },
    "bank_corp_pay": {
        "name": "网银对公付款机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("登录工行企业网银", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("打开对公付款\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 2),
            ("读取待付款数据", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 3),
            ("还有未付款项?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("填写对公付款信息\n收款单位/金额", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("确认付款", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 6),
            ("查询付款结果", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 7),
            ("退出工行网银", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 8),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 9),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,4),(4,8,0.7,"否"),(8,9)],
    },
    "bank_receive": {
        "name": "网银收款查询机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开收款查询\n业务数据表.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("读取预期收款记录", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 2),
            ("登录工行企业网银", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 3),
            ("进入收款查询页面", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 4),
            ("点击 '查询' 按钮", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("还有未核对的\n预期记录?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 6),
            ("核对匹配项\n已到账✓/未到账✗", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 7),
            ("生成核对报告", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 8),
            ("退出企业网银", "rounded=1;fillColor=#ffe6cc;strokeColor=#d79b00;", 9),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 10),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7,0.3,"是"),(7,6),(6,8,0.7,"否"),(8,9),(9,10)],
    },
    "stock_price": {
        "name": "股票实时价格采集机器人",
        "nodes": [
            ("开始", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 0),
            ("打开股票实时价格\n登记簿.xls", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 1),
            ("读取股票清单\n代码/名称/买入价", "rounded=1;fillColor=#fff2cc;strokeColor=#d6b656;", 2),
            ("打开行情网站", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 3),
            ("还有未查询股票?", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 4),
            ("搜索股票代码", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 5),
            ("获取实时价格", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 6),
            ("盈亏判断\n↑盈利 / ↓亏损", "rhombus=1;fillColor=#f8cecc;strokeColor=#b85450;", 7),
            ("写回实时价格\n到Excel", "rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;", 8),
            ("生成操作建议", "rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;", 9),
            ("结束", "ellipse;fillColor=#d5e8d4;strokeColor=#82b366;", 10),
        ],
        "edges": [(0,1),(1,2),(2,3),(3,4),(4,5,0.3,"是"),(5,6),(6,7),(7,8,0.3,"↑盈利"),(7,8,0.7,"↓亏损"),(8,4),(4,9,0.7,"否"),(9,10)],
    },
}


def generate_drawio_xml(robot_key):
    """生成标准 draw.io mxGraphModel XML"""
    robot = ROBOTS.get(robot_key)
    if not robot:
        return None

    xml_lines = []
    xml_lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    xml_lines.append('<mxfile host="Big-Data-and-Accounting-RPA-skills" version="1.0">')
    safe_name = escape(robot["name"])
    xml_lines.append(f'  <diagram id="rpa-flowchart-{robot_key}" name="{safe_name}">')
    xml_lines.append('    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1">')
    xml_lines.append('      <root>')
    xml_lines.append('        <mxCell id="0"/>')
    xml_lines.append('        <mxCell id="1" parent="0"/>')

    # Layout: vertical flow, nodes spaced 120px apart
    start_x, start_y = 80, 40
    box_w, box_h = 200, 60
    rhombus_w, rhombus_h = 160, 80

    for i, (label, style, order) in enumerate(robot["nodes"]):
        cell_id = str(i + 2)
        y_pos = start_y + i * 120
        
        if "rhombus" in style:
            w, h = rhombus_w, rhombus_h
        elif "ellipse" in style:
            w, h = 120, 60
        else:
            w, h = box_w, box_h

        escaped_label = escape(label)
        escaped_style = escape(style)
        xml_lines.append(f'        <mxCell id="{cell_id}" value="{escaped_label}" style="{escaped_style}" vertex="1" parent="1">')
        xml_lines.append(f'          <mxGeometry x="{start_x}" y="{y_pos}" width="{w}" height="{h}" as="geometry"/>')
        xml_lines.append(f'        </mxCell>')

    # Generate edges
    for edge_info in robot["edges"]:
        if len(edge_info) == 2:
            src_idx, tgt_idx = edge_info
            src_id = str(src_idx + 2)
            tgt_id = str(tgt_idx + 2)
            label = ""
        else:
            src_idx, tgt_idx, exit_y, label = edge_info
            src_id = str(src_idx + 2)
            tgt_id = str(tgt_idx + 2)

        edge_id = f"e{src_idx}_{tgt_idx}"
        src_pos = src_idx
        tgt_pos = tgt_idx

        # Calculate edge direction
        is_loopback = src_pos > tgt_pos
        if is_loopback:
            # Loopback: exit from left side
            exit_x, exit_y_val = "0", "0.5"
            entry_x, entry_y_val = "0.5", "0"
            style = f"edgeStyle=orthogonalEdgeStyle;exitX={exit_x};exitY={exit_y_val};entryX={entry_x};entryY={entry_y_val};endArrow=classic;curved=1;"
        else:
            exit_x, exit_y_val = "0.5", "1"
            entry_x, entry_y_val = "0.5", "0"
            style = f"edgeStyle=orthogonalEdgeStyle;exitX={exit_x};exitY={exit_y_val};entryX={entry_x};entryY={entry_y_val};endArrow=classic;"

        edge_value = escape(label) if label else ""
        xml_lines.append(f'        <mxCell id="{edge_id}" value="{edge_value}" style="{style}" edge="1" parent="1" source="{src_id}" target="{tgt_id}">')
        xml_lines.append(f'          <mxGeometry relative="1" as="geometry"/>')
        xml_lines.append(f'        </mxCell>')

    xml_lines.append('      </root>')
    xml_lines.append('    </mxGraphModel>')
    xml_lines.append('  </diagram>')
    xml_lines.append('</mxfile>')

    return "\n".join(xml_lines)


def generate_all_drawio(output_dir):
    """为所有机器人生成 drawio 文件"""
    os.makedirs(output_dir, exist_ok=True)
    generated = []
    for key, robot in ROBOTS.items():
        xml = generate_drawio_xml(key)
        if xml:
            filename = f"{key}.drawio"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(xml)
            generated.append((filename, robot["name"]))
            print(f"  ✅ {filename} ({robot['name']})")
    return generated


def generate_svg_preview(output_dir):
    """生成纯SVG流程图预览（不含draw.io依赖）"""
    os.makedirs(output_dir, exist_ok=True)

    robot_svg_info = {
        "tax_login": ("电子税务局平台登录机器人", [
            "【开始】→ 【打开Chrome】→ 【点击登录头像】→",
            "【填写用户名】→ 【填写密码】→ 【点击登录】→",
            "┌→ 【登录成功?】 ──是──→ 【保存Cookie】→ 【结束】",
            "└──失败重试──→ 【填写用户名】（循环）",
        ]),
        "invoice_open": ("发票开具机器人", [
            "【开始】→ 【登录税务局】→ 【打开Excel】→ 【读取数据】→",
            "┌→ 【还有未开发票?】 ──是──→ 【填写发票信息】→ 【提交开具】",
            "│                                      ↓",
            "│                               【开具成功?】 ──否──→ 【重试】",
            "│                                      ↓是",
            "└──────────────────────────←──────────┘",
            "【退出税务局】→ 【结束】",
        ]),
        "invoice_check": ("发票查验机器人", [
            "【开始】→ 【打开Excel】→ 【读取数据】→ 【登录查验平台】→",
            "┌→ 【还有未查验发票?】 ──是──→ 【输入发票信息】→",
            "│                                      ↓",
            "│                               【查验】→ 【写回Excel】",
            "│                                      ↓",
            "└──────────────────────←──────────┘",
            "【结束】",
        ]),
        "invoice_certify": ("发票认证机器人", [
            "【开始】→ 【打开Excel】→ 【读取数据】→ 【登录认证平台】→",
            "┌→ 【还有未认证发票?】 ──是──→ 【输入信息+密钥】→",
            "│                                      ↓",
            "│                               【认证】→ 【写回结果】",
            "│                                      ↓",
            "└──────────────────────←──────────┘",
            "【结束】",
        ]),
        "bank_pay": ("网银付款机器人", [
            "【开始】→ 【打开Excel】→ 【读取数据】→ 【登录网银】→",
            "┌→ 【还有未付款?】 ──是──→ 【付款信息+U盾密码】→",
            "│                                      ↓",
            "│                        ┌→ 【确认付款】",
            "│                        │     ↓",
            "│                        │【付款成功?】 ──否──→ 【查询付款信息】",
            "│                        │     ↓是              ↓",
            "└──────────────────────←─┘           【退出网银】→ 【结束】",
        ]),
        "bank_corp_pay": ("网银对公付款机器人", [
            "【开始】→ 【登录网银】→ 【打开Excel】→ 【读取数据】→",
            "┌→ 【还有未付款?】 ──是──→ 【填写对公付款信息】→",
            "│                                      ↓",
            "│                               【确认付款】→ 【查询结果】",
            "│                                      ↓",
            "└──────────────────────←──────────┘",
            "【退出网银】→ 【结束】",
        ]),
        "bank_receive": ("网银收款查询机器人", [
            "【开始】→ 【打开Excel】→ 【读取数据】→ 【登录网银】→",
            "【进入收款查询】→ 【查询】→",
            "┌→ 【还有未核对记录?】 ──是──→ 【核对匹配项】",
            "│                                      ↓",
            "└──────────────────────←──────────┘",
            "【生成核对报告】→ 【退出网银】→ 【结束】",
        ]),
        "stock_price": ("股票价格采集机器人", [
            "【开始】→ 【打开Excel】→ 【读取股票清单】→ 【打开行情网站】→",
            "┌→ 【还有未查询股票?】 ──是──→ 【搜索股票代码】→",
            "│                                      ↓",
            "│                               【获取实时价格】",
            "│                                      ↓",
            "│                               【盈亏判断↑/↓】→ 【写回Excel】",
            "│                                      ↓",
            "└──────────────────────←──────────┘",
            "【生成操作建议】→ 【结束】",
        ]),
    }

    for key, (name, lines) in robot_svg_info.items():
        svg_lines = []
        svg_lines.append('<?xml version="1.0" encoding="UTF-8"?>')
        svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{30 * len(lines) + 60}" viewBox="0 0 900 {30 * len(lines) + 60}">')
        svg_lines.append(f'  <rect width="900" height="{30 * len(lines) + 60}" fill="#f8f9fa" rx="8"/>')
        svg_lines.append(f'  <text x="20" y="30" font-family="Microsoft YaHei, SimSun, sans-serif" font-size="16" font-weight="bold" fill="#333">{name} - 流程图预览</text>')

        for i, line in enumerate(lines):
            y = 60 + i * 24
            svg_lines.append(f'  <text x="20" y="{y}" font-family="Consolas, monospace" font-size="13" fill="#444">{escape(line)}</text>')

        svg_lines.append('</svg>')
        filepath = os.path.join(output_dir, f"{key}_preview.svg")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(svg_lines))
        print(f"  ✅ {key}_preview.svg")

    return True


def main():
    parser = argparse.ArgumentParser(description="RPA 流程图生成器 (draw.io XML Engine)")
    parser.add_argument("-r", "--robot", choices=list(ROBOTS.keys()) + ["all"], default="all",
                        help="要生成的机器人流程图")
    parser.add_argument("-o", "--output", default=None,
                        help="输出文件路径（不含扩展名）")
    parser.add_argument("-f", "--format", choices=["drawio", "svg", "both"], default="both",
                        help="输出格式")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_base = os.path.join(base_dir, "REFERENCE", "flowcharts", "drawio")

    if args.robot == "all":
        print("🔄 为所有8个RPA机器人生成流程图...\n")
        generated = generate_all_drawio(output_base)
        if args.format in ("svg", "both"):
            print("\n🔄 生成SVG预览...")
            generate_svg_preview(output_base)
        print(f"\n✅ 共生成 {len(generated)} 个 .drawio 文件")
        print(f"📁 输出目录: {output_base}")
        print("\n💡 提示：.drawio 文件可用 draw.io 在线打开: https://app.diagrams.net")
    else:
        print(f"🔄 生成 {ROBOTS[args.robot]['name']} 流程图...")
        xml = generate_drawio_xml(args.robot)
        if xml:
            out = args.output or args.robot
            drawio_path = os.path.join(output_base, f"{out}.drawio")
            os.makedirs(output_base, exist_ok=True)
            with open(drawio_path, 'w', encoding='utf-8') as f:
                f.write(xml)
            print(f"  ✅ {out}.drawio")
            print(f"📁 {drawio_path}")

    # Generate index.json for robot list
    index = {k: {"name": v["name"], "nodes": len(v["nodes"]), "edges": len(v["edges"])}
             for k, v in ROBOTS.items()}
    index_path = os.path.join(base_dir, "AGENTS", "agent_module_asset", "robot_flowchart_index.json")
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 流程图索引已更新: robot_flowchart_index.json")


if __name__ == "__main__":
    main()
