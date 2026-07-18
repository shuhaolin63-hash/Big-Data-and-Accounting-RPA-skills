#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
流程图生成脚本
为 7 个机器人 + 双场景闭环生成 Mermaid 格式可视化流程图
输出到 REFERENCE/flowcharts/ 目录
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "REFERENCE", "flowcharts")


def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def write_mermaid(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 生成: {filename}")
    return path


def tax_login_flow():
    """电子税务局平台登录机器人"""
    content = """# 电子税务局平台登录机器人 - 作业流程图

> 业务流程：启动 → 打开登录页 → 输入凭证 → 认证 → 结束

```mermaid
graph TD
    Start([开始]) --> OpenBrowser[打开 Chrome 浏览器<br>访问电子税务局]
    OpenBrowser --> ClickLoginBtn[点击 "登录头像" 按钮]
    ClickLoginBtn --> SwitchToLogin[切换到登录表单页]
    SwitchToLogin --> InputUsername[填写 用户名输入框]
    InputUsername --> InputPassword[填写 密码输入框]
    InputPassword --> ClickSubmit[点击 "登录" 按钮]
    ClickSubmit --> VerifyLogin{登录成功?}
    VerifyLogin -->|是| SaveCookie[保存 Cookie / Token]
    VerifyLogin -->|失败重试| InputUsername
    SaveCookie --> End([结束])

    subgraph 框选要点
        ClickLoginBtn -->|框选| LoginBtn[定位: 登录头像按钮<br>class: loing alert_click_show]
        InputUsername -->|框选| UName[定位: 用户名输入框<br>name: acc]
        InputPassword -->|框选| Pwd[定位: 密码输入框<br>name: pwd]
        ClickSubmit -->|框选| SubmitBtn[定位: 登录按钮<br>id: login]
    end
```
"""
    return write_mermaid("01_电子税务局登录流程图.md", content)


def invoice_open_flow():
    """发票开具机器人"""
    content = """# 发票开具机器人 - 作业流程图

> 业务流程：启动 → 登录 → 读取数据 → 逐笔开票 → 退出

```mermaid
graph TD
    Start([开始]) --> CallStart[调用 START 子流程]
    CallStart --> OpenBrowser[打开 Chrome<br>访问电子税务局]
    OpenBrowser --> TaxLogin[登录电子税务局]
    TaxLogin --> OpenExcel[打开 发票开具业务数据表.xls]
    OpenExcel --> ReadData[读取 待开票数据]
    ReadData --> LoopData{还有未开发票?}

    LoopData -->|是| GetNext[取下一行数据]
    GetNext --> FillInvoice[填写发票信息<br>购货方/商品/金额/税率]
    FillInvoice --> SubmitInvoice[提交开具]
    SubmitInvoice --> CheckResult{开具成功?}
    CheckResult -->|是| LoopData
    CheckResult -->|否| Retry[重试或记录异常]
    Retry --> LoopData

    LoopData -->|否| Logout[退出电子税务局]
    Logout --> CallEnd[调用 END 子流程]
    CallEnd --> End([结束])

    subgraph 框选要点
        TaxLogin -->|框选| LoginArea[登录表单: 用户名/密码/登录按钮]
        FillInvoice -->|框选| InvoiceForm[开票表单: 发票类型/购货方/商品明细/金额/税率]
        SubmitInvoice -->|框选| SubmitBtn[提交按钮]
        Logout -->|框选| LogoutBtn[退出/安全退出按钮]
    end
```
"""
    return write_mermaid("02_发票开具机器人流程图.md", content)


def invoice_check_flow():
    """发票查验机器人"""
    content = """# 发票查验机器人 - 作业流程图

> 业务流程：启动 → 打开表格 → 逐条查验 → 记录结果

```mermaid
graph TD
    Start([开始]) --> CallStart[调用 START 子流程]
    CallStart --> OpenExcel[打开 发票查验业务数据表.xls]
    OpenExcel --> ReadData[读取待查验发票数据]
    ReadData --> OpenCheckPage[打开 发票查验平台]
    OpenCheckPage --> LoginCheck[登录查验系统]
    LoginCheck --> LoopData{还有未查验发票?}

    LoopData -->|是| GetNext[取下一张发票]
    GetNext --> InputInvoiceCode[输入 发票代码]
    InputInvoiceCode --> InputInvoiceNum[输入 发票号码]
    InputInvoiceNum --> InputCheckCode[输入 校验码]
    InputCheckCode --> InputAmount[输入 金额]
    InputAmount --> ClickCheck[点击 "查验" 按钮]
    ClickCheck --> GetResult[获取查验结果]
    GetResult --> WriteResult[将结果写回 Excel]
    WriteResult --> LoopData

    LoopData -->|否| CallEnd[调用 END 子流程]
    CallEnd --> End([结束])

    subgraph 框选要点
        InputInvoiceCode -->|框选| CodeField[发票代码输入框]
        InputInvoiceNum -->|框选| NumField[发票号码输入框]
        InputCheckCode -->|框选| CheckCodeField[校验码输入框]
        ClickCheck -->|框选| CheckBtn["查验" 按钮]
        GetResult -->|框选| ResultArea[查验结果区域]
    end
```
"""
    return write_mermaid("03_发票查验机器人流程图.md", content)


def invoice_certify_flow():
    """发票认证机器人"""
    content = """# 发票认证机器人 - 作业流程图

> 业务流程：启动 → 打开 Excel → 逐张认证 → 记录结果

```mermaid
graph TD
    Start([开始]) --> CallStart[调用 START 子流程]
    CallStart --> OpenExcel[打开 发票认证业务数据表.xls]
    OpenExcel --> ReadData[读取待认证发票数据]
    ReadData --> OpenCertifyPage[打开 发票认证平台]
    OpenCertifyPage --> LoginCertify[登录认证系统]
    LoginCertify --> LoopData{还有未认证发票?}

    LoopData -->|是| GetNext[取下一张发票]
    GetNext --> InputCertInfo[输入发票信息<br>代码/号码/金额/日期]
    InputCertInfo --> InputCertKey[输入认证密钥]
    InputCertKey --> ClickCertify[点击 "认证" 按钮]
    ClickCertify --> WaitResult[等待认证结果]
    WaitResult --> GetCertResult[获取认证结果]
    GetCertResult --> WriteResult[认证结果写回 Excel]
    WriteResult --> LoopData

    LoopData -->|否| CallEnd[调用 END 子流程]
    CallEnd --> End([结束])

    subgraph 框选要点
        InputCertInfo -->|框选| CertForm[认证信息输入表单]
        InputCertKey -->|框选| CertKeyField[认证密钥输入框]
        ClickCertify -->|框选| CertifyBtn["认证" 按钮]
        GetCertResult -->|框选| CertResultArea[认证结果区域]
    end
```
"""
    return write_mermaid("04_发票认证机器人流程图.md", content)


def bank_pay_flow():
    """网银付款机器人"""
    content = """# 网银付款机器人 - 作业流程图

> 业务流程：启动 → 登录网银 → 读取付款表 → 逐笔付款 → 查询 → 退出

```mermaid
graph TD
    Start([开始]) --> CallStart[调用 START 子流程]
    CallStart --> OpenExcel[打开 网银付款业务数据表.xls]
    OpenExcel --> ReadData[读取待付款数据]
    ReadData --> OpenBank[打开 工商银行网银]
    OpenBank --> LoginBank[登录企业网银]
    LoginBank --> LoopData{还有未付款项?}

    LoopData -->|是| GetNext[取下一笔付款]
    GetNext --> InputPayInfo[填写付款信息<br>收款人/账号/金额/用途]
    InputPayInfo --> InputBankKey[输入 U盾密码]
    InputBankKey --> ConfirmPay[确认付款]
    ConfirmPay --> CheckPayResult{付款成功?}
    CheckPayResult -->|是| RecordSuccess[记录成功]
    CheckPayResult -->|否| RecordFail[记录失败原因]
    RecordSuccess --> LoopData
    RecordFail --> LoopData

    LoopData -->|否| QueryPayInfo[查询付款信息汇总]
    QueryPayInfo --> LogoutBank[退出企业网银]
    LogoutBank --> CallEnd[调用 END 子流程]
    CallEnd --> End([结束])

    subgraph 框选要点
        LoginBank -->|框选| BankLoginForm[网银登录表单: 用户名/密码/验证码]
        InputPayInfo -->|框选| PayForm[付款信息填写区域]
        InputBankKey -->|框选| BankKeyField[U盾密码输入框]
        ConfirmPay -->|框选| ConfirmBtn[确认付款按钮]
        LogoutBank -->|框选| LogoutBtn[安全退出按钮]
    end
```
"""
    return write_mermaid("05_网银付款机器人流程图.md", content)


def bank_corp_pay_flow():
    """网银对公付款机器人"""
    content = """# 网银对公付款机器人（开发模板）- 作业流程图

> 业务流程：启动 → 登录网银 → 读取对公付款表 → 逐笔付款 → 查询 → 退出

```mermaid
graph TD
    Start([开始]) --> LoginBank[登录工行企业网银]
    LoginBank --> OpenExcel[打开 网银对公付款业务数据表.xls]
    OpenExcel --> ReadData[读取待付款数据]
    ReadData --> LoopData{还有未付款项?}

    LoopData -->|是| GetNext[取下一笔付款]
    GetNext --> InputPayInfo[填写付款信息<br>收款单位/开户行/账号/金额]
    InputPayInfo --> ConfirmPay[确认付款]
    ConfirmPay --> QueryResult[查询付款结果]
    QueryResult --> LoopData

    LoopData -->|否| QueryAll[查询所有付款信息]
    QueryAll --> Logout[退出工行网银]
    Logout --> End([结束])

    subgraph 框选要点
        LoginBank -->|框选| BankLogin[网银登录表单]
        InputPayInfo -->|框选| CorpPayForm[对公付款填写区域<br>收款单位/开户行/账号]
        ConfirmPay -->|框选| ConfirmBtn[确认付款按钮]
        Logout -->|框选| LogoutBtn[退出系统按钮]
    end
```
"""
    return write_mermaid("06_网银对公付款机器人流程图.md", content)


def bank_receive_flow():
    """网银收款查询机器人"""
    content = """# 网银收款查询机器人 - 作业流程图

> 业务流程：启动 → 登录网银 → 查询收款流水 → 核对 → 退出

```mermaid
graph TD
    Start([开始]) --> CallStart[调用 START 子流程]
    CallStart --> OpenExcel[打开 收款查询业务数据表.xls]
    OpenExcel --> ReadData[读取预期收款记录]
    ReadData --> OpenBank[打开 工商银行网银]
    OpenBank --> LoginBank[登录企业网银]
    LoginBank --> NavigateReceive[进入 收款查询页面]
    NavigateReceive --> SetQueryPeriod[设置查询时间范围]
    SetQueryPeriod --> ClickQuery[点击 "查询" 按钮]
    ClickQuery --> GetResults[获取收款流水结果]
    GetResults --> CompareData[逐条核对预期 vs 实际]

    CompareData --> LoopData{还有未核对的预期记录?}
    LoopData -->|是| MatchNext[取下一条预期记录]
    MatchNext --> FindMatch[在结果中查找匹配项]
    FindMatch --> RecordResult{找到匹配?}
    RecordResult -->|是| MarkMatched[标记: 已到账 ✓]
    RecordResult -->|否| MarkMissing[标记: 未到账 ✗]
    MarkMatched --> LoopData
    MarkMissing --> LoopData

    LoopData -->|否| WriteReport[生成核对报告]
    WriteReport --> LogoutBank[退出企业网银]
    LogoutBank --> CallEnd[调用 END 子流程]
    CallEnd --> End([结束])

    subgraph 框选要点
        LoginBank -->|框选| BankLogin[网银登录表单]
        NavigateReceive -->|框选| ReceiveMenu[收款查询菜单项]
        SetQueryPeriod -->|框选| DateRangePicker[日期范围选择器]
        ClickQuery -->|框选| QueryBtn["查询" 按钮]
        GetResults -->|框选| ResultTable[收款流水结果表格]
    end
```
"""
    return write_mermaid("07_网银收款查询机器人流程图.md", content)


def stock_price_flow():
    """股票实时价格采集机器人"""
    content = """# 股票实时价格采集机器人 - 作业流程图

> 业务流程：启动 → 读取股票清单 → 逐只查询 → 更新价格

```mermaid
graph TD
    Start([开始]) --> OpenExcel[打开 股票实时价格登记簿.xls]
    OpenExcel --> ReadData[读取股票清单<br>代码/名称/买入价]
    ReadData --> OpenBrowser[打开浏览器<br>访问股票行情网站]
    OpenBrowser --> LoopData{还有未查询的股票?}

    LoopData -->|是| GetNext[取下一只股票]
    GetNext --> SearchStock[搜索股票代码/名称]
    SearchStock --> GetPrice[获取实时价格]
    GetPrice --> ComparePrice{实时价 vs 买入价}
    ComparePrice -->|上涨| MarkUp[标记: ↑ 盈利]
    ComparePrice -->|下跌| MarkDown[标记: ↓ 亏损]
    MarkUp --> WritePrice[写回实时价格到 Excel]
    MarkDown --> WritePrice
    WritePrice --> LoopData

    LoopData -->|否| GenerateAdvice[根据盈亏生成操作建议]
    GenerateAdvice --> SaveExcel[保存 Excel]
    SaveExcel --> End([结束])

    subgraph 框选要点
        SearchStock -->|框选| StockSearchBox[股票搜索输入框]
        GetPrice -->|框选| PriceDisplayArea[实时价格显示区域]
    end
```
"""
    return write_mermaid("08_股票价格采集机器人流程图.md", content)


def dual_scenario_flow():
    """双场景闭环流程图"""
    content = """# 双场景完整作业闭环流程图

> 总控 Skill 根据用户需求自动路由到对应子智能体

## 场景A：有同学分享源码工程

```mermaid
graph LR
    UserA([用户: 有别人源码]) --> CrackAgent[🔧 破障Agent<br>清除他人Base64 ID]
    CrackAgent --> AssetAgent[📦 资产Agent<br>补齐缺失素材<br>替换本机路径]
    AssetAgent --> TeacherAgent[🧑‍🏫 老师Agent<br>讲解框选逻辑<br>输出对照表]
    TeacherAgent --> UserInputID[用户自主填写<br>UserID / TaskID]
    UserInputID --> Runtime[⚡ CORE_RUNTIME<br>动态注入个人ID]
    Runtime --> DoneA[✅ 生成专属合规作业<br>无风控 无查重]
```

## 场景B：无任何源码（从零做作业）

```mermaid
graph LR
    UserB([用户: 没有代码]) --> AssetAgentB[📦 资产Agent<br>调取标准模板<br>配套表格+图片]
    AssetAgentB --> TeacherAgentB[🧑‍🏫 老师Agent<br>逐步骤框选指导<br>位置+范围+功能]
    TeacherAgentB --> UserSelect[用户按照指导<br>完成页面框选]
    UserSelect --> UserInputIDB[用户强制提交<br>UserID / TaskID]
    UserInputIDB --> CrackAgentB[🔧 破障Agent<br>校验ID合法性<br>动态注入工程]
    CrackAgentB --> DoneB[✅ 输出可直接提交的<br>合规作业]
```

## 总控 Skill 自动路由逻辑

```mermaid
graph TD
    UserInput[用户输入需求] --> Controller{总控 Skill<br>判断意图}
    Controller -->|"有源码/别人分享"| A[破障Agent → 资产Agent → 老师Agent]
    Controller -->|"没有代码/从零"| B[资产Agent → 老师Agent → 破障Agent]
    Controller -->|"怎么框选"| C[老师Agent 单独教学]
    Controller -->|"清除ID"| D[破障Agent 单独清扫]
    Controller -->|"补素材/缺表格"| E[资产Agent 单独补齐]
    Controller -->|"检查作业"| F[破障Agent 校验 + 老师Agent 验收]
```
"""
    return write_mermaid("00_双场景闭环流程图.md", content)


def agents_architecture():
    """三大智能体架构图"""
    content = """# 三大智能体协作架构图

> 总控 Skill 统一调度，三大子智能体各司其职

```mermaid
graph TB
    MainSkill[📊 Big-Data-and-Accounting-RPA-skills<br>总控 Skill] --> Teacher[🧑‍🏫 老师教学智能体<br>rpa-teacher-agent]
    MainSkill --> Crack[🔧 破障修复智能体<br>rpa-crack-agent]
    MainSkill --> Asset[📦 模块资产智能体<br>rpa-module-asset-agent]

    Teacher --> Teach1[框选标准化教学]
    Teacher --> Teach2[考点讲解]
    Teacher --> Teach3[ID合规教育]
    Teacher --> Teach4[验收标准输出]

    Crack --> Crack1[清除Base64硬编码ID]
    Crack --> Crack2[ID合法性校验]
    Crack --> Crack3[风控合规检测]
    Crack --> Crack4[动态注入用户ID]

    Asset --> Asset1[资产库管理<br>7套机器人]
    Asset --> Asset2[模板生成<br>标准代码+表格+图片]
    Asset --> Asset3[路径适配<br>批量替换本机路径]
    Asset --> Asset4[素材补齐<br>自动检测缺失]

    subgraph 协作流程
        Crack -->|清理后代码| Teacher
        Asset -->|生成的模板| Teacher
        Crack -->|注入ID| Runtime[⚡ CORE_RUNTIME]
    end

    subgraph 用户工作区
        Runtime --> UserWS[USER_WORKSPACE<br>user_id_config.yaml]
        UserWS --> Homework[最终可提交作业]
    end
```

## 系统层级架构

```mermaid
graph LR
    L1[🥇 SKILL.md<br>全局总控入口] --> L2[🥇 ASSET/<br>作业资产库]
    L2 --> L3[🥈 REFERENCE/<br>参考文档]
    L3 --> L4[🥉 SCRIPTS/<br>核心脚本]
    L4 --> L5[4️⃣ AGENTS/<br>三大子智能体]
    L5 --> L6[5️⃣ USER_WORKSPACE/<br>用户工作区]
```
"""
    return write_mermaid("00_系统架构流程图.md", content)


def main():
    ensure_dir()
    print("🔄 生成可视化流程图...\n")

    paths = []
    paths.append(tax_login_flow())
    paths.append(invoice_open_flow())
    paths.append(invoice_check_flow())
    paths.append(invoice_certify_flow())
    paths.append(bank_pay_flow())
    paths.append(bank_corp_pay_flow())
    paths.append(bank_receive_flow())
    paths.append(stock_price_flow())
    paths.append(dual_scenario_flow())
    paths.append(agents_architecture())

    print(f"\n📊 共生成 {len(paths)} 个流程图文件")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print("\n💡 提示：这些 .md 文件中的 Mermaid 图表在 GitHub 上自动渲染")
    print("   也可以用支持 Mermaid 的 Markdown 编辑器（如 Typora）打开查看")
    return 0


if __name__ == "__main__":
    main()
