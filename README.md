# 📊 RPA学生多智能体作业系统总控Skill

> "你的期末考试救星 + 私人财务 RPA 指导老师 —— 仅适用于阿里云 RPA"

`阿里云RPA` `RPA作业` `学生智能体` `期末救星` `框选教学` `ID风控` `有源码改作业` `无源码做作业` `AgentSkills` `技能包`

🎓 MIT License · Python 3.9+ · AgentSkills · ⭐ 已就绪

SOLO · Claude Code · Hermes · Codex


## About

**期末周了，你属于哪一种学生？**

| 你的情况 | 怎么破 |
|----------|--------|
| 🧑‍🎓 **抱大腿型** — 同学分享了源码工程，但里面全是他人的 UserID，直接交 = 0 分 + 风控拉黑 | 破障Agent 三秒清掉所有硬编码 ID，换成你的，干干净净 |
| 💔 **裸考型** — deadline 就在明天，没有源码、没有素材、不会框选、不知道从零怎么做 | 资产Agent 调模板，老师Agent 手把手教框选，从零出作业 |
| 🌟 **卷王型** — 你想做一份查重不过、ID 合规、框选精准的完美工程，但没人教你评分标准 | 老师Agent 输出验收标准 + 扣分点，精准拿满分 |
| 😰 **踩坑型** — 作业做完了，但不确定有没有别人 ID、路径对不对、能不能过风控 | 破障Agent 全盘扫描 + 风控检测，出一份安全报告 |
| 🤷 **迷茫型** — 不知道选哪个机器人来做作业，不知道哪个简单、哪个分高 | 资产Agent 列出 7 套模板的业务场景和难度，帮你选 |

**别管你是哪种。你的期末考试救星来了。**

这不是什么高高在上的技术框架。这是你的私人 RPA 指导老师，一个懂你期末有多难、知道阿里云 RPA 怎么考、帮你从零肝出完整作业的智能体团队。

有源码 → 帮你清掉别人的 ID，补上缺失的素材，教你这代码框选了啥。
没源码 → 从资产库调模板，手把手教你在页面上框哪儿、框多大、为什么框。
填 ID → 你亲手填你自己的，系统只注入不保存，安全合规不风控。
出作业 → 点几下，属于你一个人的期末作业就出来了。

**清码 · 补素材 · 教框选 · 填 ID · 出作业 · 一人搞定**


🎉 2026.07.19 里程碑 — Big-Data-and-Accounting-RPA-skills v1.0 正式发布！

历时数次迭代重构，最终定稿为 5 层层级架构 + 4 个 Skill 入口 + 22 个支撑文件的全功能系统。

📢 2026.07.19 更新 — 电子税务局 7 大机器人资产库全部入库！ 19 张 UI 截图 + 8 张业务数据表 + 7 套完整机器人代码分类索引，从发票查验到网银付款，资产全齐。

🗺️ 2026.07.19 — 双场景闭环正式上线！有源码场景（破障→资产→老师）和无源码场景（资产→老师→破障）已全部打通。👉 完整架构参见 README

🧑‍🏫 三大硬性强制规则已生效 — ID 零硬编码 · ID 自主提交 · 框选必交底

Asset Base: `f:\RPA(1)\` · Skills: `.trae/skills/` · 项目根目录: `Big-Data-and-Accounting-RPA-skills/` · 引擎: SOLO AI Agent


## 🆕 这次版本有什么？

### 1️⃣ 三大智能体协作，覆盖双场景闭环

| 智能体 | 代号 | 核心职责 |
|-------|------|---------|
| 🧑‍🏫 **老师教学智能体** | `rpa-teacher-agent` | 框选标准化教学、作业合规指导、考点讲解、ID合规教育 |
| 🔧 **破障修复智能体** | `rpa-crack-agent` | 清除硬编码ID、ID合法性校验、风控检测、动态注入 |
| 📦 **模块资产智能体** | `rpa-module-asset-agent` | 资产库管理、模板生成、路径适配、素材补齐 |

三大智能体串成一条流水线，一条龙出作业。

### 2️⃣ 支持两大作业场景

| 场景 | 流程 | 适合谁 |
|------|------|--------|
| **🧬 有源码改作业** | 破障清ID → 资产补素材 → 老师讲框选 → 用户填ID → 注入生成 | 有同学分享工程的 |
| **🆕 无源码做新作业** | 资产调模板 → 老师教框选 → 用户框选+填ID → 破障校验 → 出作业 | 零基础、自己一个人做的 |

### 3️⃣ 支持多宿主调用

| 宿主 | 调用方式 |
|------|---------|
| 🟣 **SOLO（默认）** | Skill name 调用，三大子Agent 自动路由 |
| 🟠 **Claude Code** | slash command 兼容 |
| 🔵 **Hermes Agent** | 一键调用 |
| ⚫ **Codex** | skill name 直接路由 |


## 🚀 三大硬性强制规则

### 🔒 ID 零硬编码
系统中所有模板、脚本、配置，永久不内置任何 UserID / TaskID，不预埋 Base64 编码。所有 ID 字段使用 `{{USER_ID}}`、`{{TASK_ID}}` 占位符。杜绝泄露与串号。

### ✍️ ID 自主提交
最终作业生成前，**必须由用户手动输入**个人本机学生版 ID。系统只做运行时动态注入，不伪造、不替换、不篡改官方身份。不提交，不出作业。

### 📐 框选必交底
所有需要手动框选、拾取元素的步骤，必须向用户输出「位置 + 范围 + 功能 + 对错标准」。绝不允许只给代码不给操作说明。


## 📦 支持的作业资产库

资产库根目录：`f:\RPA(1)\`

| 资产编号 | 机器人名称 | 场景 |
|---------|-----------|------|
| 📄 AST-001 | 电子税务局平台登录机器人 | 税务系统登录 |
| 📄 AST-002 | 发票开具机器人 | 数电票批量开具 |
| 📄 AST-003 | 发票查验机器人 | 发票真伪查验 |
| 📄 AST-004 | 发票认证机器人 | 进项发票认证 |
| 📄 AST-005 | 网银付款机器人 | 企业网银付款 |
| 📄 AST-006 | 网银对公付款机器人（开发模板） | 对公材料款付款 |
| 📄 AST-007 | 网银收款查询机器人 | 收款流水查询 |

配套：**8 张业务数据表**（.xls）+ **19 张 UI 截图**（.png）+ **7 套完整代码 + 控件选择器**


## ⚡ 一键安装（安装技能）

### 这是什么？

Big-Data-and-Accounting-RPA-skills 是一套 **Agent Skills**（智能体技能包），不是普通的 Python 库或插件。安装＝把这套技能注册到你的 AI 宿主的 skills 目录中，让宿主认识并能够调用它们。它遵循 AgentSkills 开放标准，适用于以下 **AI 编程宿主**：

| 宿主 | 支持情况 | 说明 |
|------|---------|------|
| 🟣 **SOLO（Trae）** | ✅ 原生支持 | Skill name 直接调用，三大子 Agent 自动路由 |
| 🟠 **Claude Code** | ✅ 兼容 | slash command 调用 |
| 🔵 **Hermes Agent** | ✅ 兼容 | 一键 `/dot-skill` 调用 |
| ⚫ **Codex** | ✅ 兼容 | skill name 路由 |

### 各宿主安装命令

打开 **CMD 终端**（Win+R → 输入 `cmd` → 回车），根据你使用的宿主执行对应的安装命令：

#### 🟣 SOLO / Trae CN（默认宿主）

```cmd
:: 技能文件已放在 .trae/skills/ 目录下，SOLO 自动识别加载
:: 无需手动执行安装命令，直接在对话中描述需求即可使用
```

#### 🟠 Claude Code

```cmd
:: 注册总控 Skill
skills register f:\RPA(1)\.trae\skills\Big-Data-and-Accounting-RPA-skills\SKILL.md

:: 注册老师教学智能体
skills register f:\RPA(1)\.trae\skills\rpa-teacher-agent\SKILL.md

:: 注册破障修复智能体
skills register f:\RPA(1)\.trae\skills\rpa-crack-agent\SKILL.md

:: 注册模块资产智能体
skills register f:\RPA(1)\.trae\skills\rpa-module-asset-agent\SKILL.md
```

#### 🔵 Hermes Agent

```cmd
:: Hermes 一键安装技能
hermes skill install f:\RPA(1)\.trae\skills\Big-Data-and-Accounting-RPA-skills\SKILL.md
hermes skill install f:\RPA(1)\.trae\skills\rpa-teacher-agent\SKILL.md
hermes skill install f:\RPA(1)\.trae\skills\rpa-crack-agent\SKILL.md
hermes skill install f:\RPA(1)\.trae\skills\rpa-module-asset-agent\SKILL.md
```

#### ⚫ Codex

```cmd
:: Codex 注册技能
codex skill add f:\RPA(1)\.trae\skills\Big-Data-and-Accounting-RPA-skills\SKILL.md
codex skill add f:\RPA(1)\.trae\skills\rpa-teacher-agent\SKILL.md
codex skill add f:\RPA(1)\.trae\skills\rpa-crack-agent\SKILL.md
codex skill add f:\RPA(1)\.trae\skills\rpa-module-asset-agent\SKILL.md
```

> 💡 4 条命令执行完毕后，**4 个技能全部安装完成**。无需额外配置，关闭 CMD 即可进入你的 AI 宿主开始使用。

### 安装后怎么用？

技能装好了，在宿主里直接描述你的需求，总控 Skill 会自动判断走哪个流程：

| 你说... | 系统会... |
|------|------|
| "帮我完成 RPA 作业" | 启动总控 Skill 自动判断场景，路由到对应子智能体 |
| "有别人分享的源码，帮我改" | **破障Agent → 资产Agent → 老师Agent** 全流程 |
| "没有代码，从零做一个发票机器人" | **资产Agent → 老师Agent → 破障Agent** 全流程 |
| "框选操作怎么弄" | 单独调用 **老师Agent** 教学 |
| "帮我把代码里的别人 ID 清了" | 单独调用 **破障Agent** 清扫 |
| "缺表格和图片，帮我补上" | 单独调用 **资产Agent** 补齐 |
| "帮我检查作业能不能提交" | **破障Agent 校验 + 老师Agent 验收** |

### 依赖项

系统正常运行需要以下前置环境：

| 依赖 | 版本要求 | 说明 |
|------|---------|------|
| 🐍 **Python** | 3.9+ | 核心脚本运行环境（ID清洗/风控/路径替换等） |
| 📦 **Pillow** | 任意 | 图片尺寸读取（`pip install Pillow`） |
| 📂 **资产根目录** | — | `f:\RPA(1)\` 必须存在，内含 7 套机器人 + 8 张表格 + 19 张截图 |
| 🧠 **AI 宿主** | — | SOLO / Claude Code / Hermes / Codex 任一 |
| 🪟 **操作系统** | Windows | 资产库路径基于 Windows 文件系统 |

> ⚠️ 如缺少 Pillow，资产检查脚本会跳过图片尺寸检测，不影响核心功能。


## 🚀 使用

在装了本系统的 Host 中直接描述你的场景 —— 总控 Skill 会自动判断路由：

### 场景一：你有同学分享的源码

```
你：帮我完成 RPA 作业，有别人分享的源码
↓
总控路由 → 破障Agent → 资产Agent → 老师Agent
  Step1  自动清除源码中的他人 UserID / TaskID / Base64 编码
  Step2  检测缺失素材，自动补齐表格/图片，替换本机路径
  Step3  讲解原有代码框选逻辑，输出框选对照表
  Step4  等待你自主填写本机 UserID、TaskID
  Step5  动态注入，生成专属合规作业
```

### 场景二：你没有任何源码，从零开始

```
你：没有代码，从零做一个发票查验机器人
↓
总控路由 → 资产Agent → 老师Agent → 破障Agent
  Step1  从资产库调用标准代码模板 + 配套表格 + 图片素材
  Step2  逐步骤输出框选指导：点哪里、框哪个区域、范围多大
  Step3  你按照指导完成页面框选和元素拾取
  Step4  提交你的个人 UserID、TaskID
  Step5  校验合法性，动态注入，输出可直接提交的作业
```

### 单独调用某个子智能体

```
你：帮我把这个代码里的别人 ID 清了          → 破障Agent
你：框选操作怎么弄？                        → 老师Agent
你：缺表格和图片，帮我补上                  → 资产Agent
你：帮我检查作业能不能提交                  → 破障Agent + 老师Agent
```


## 🎛️ 管理命令

| 命令 | 说明 |
|------|------|
| 描述你的RPA作业需求 | 总控入口，自动路由到对应子智能体 |
| 调用老师教学智能体 | 框选教学、考点讲解、验收标准 |
| 调用破障修复智能体 | 清除硬编码ID、风控校验 |
| 调用模块资产智能体 | 模板生成、素材补齐、路径修复 |


## ✨ 效果示例

### 🧑‍🏫 teacher — 框选教学场景

```
用户            ❯ 框选操作怎么弄？我不知道从哪里开始

teacher-agent   ❯ 好的，我们从第一步开始。
                  📌 框选操作 第1步：登录页面
                  
                  页面位置：电子税务局登录页 → 中央表单 → 用户名输入框
                  框选范围：从 (400, 350) 到 (600, 390)
                  元素类型：Chrome input（name="acc"）
                  功能用途：输入登录账号
                  
                  ✅ 正确框选：得 30 分
                  ❌ 框选偏移 > 10px：扣 10 分
                  ❌ 选成密码框：扣 15 分
```

### 🔧 crack — 破障清除ID场景

```
用户            ❯ 帮我看看这个源码里有没有别人的 ID

crack-agent     ❯ 正在扫描工程目录...
                  ⚠️ 发现风险！
                  
                  文件：rzgc.variable.json
                  字段：auth（Base64 编码）→ 解码后含他人用户名和手机号
                  字段：token → JWT 格式，含他人 UserID
                  字段：task_id → 32 位 hex，他人作业标识
                  
                  ✅ 已自动清除所有 7 个敏感字段
                  ✅ 替换为 PLACEHOLDER
                  ✅ 已输出清洗报告
                  
                  请继续 → 由老师Agent讲解框选逻辑
```

### 📦 asset — 从零做作业场景

```
用户            ❯ 我想做一个发票开具机器人，没有代码

module-asset    ❯ 好的，从资产库调取「发票开具机器人」模板：
                  已复制标准代码模板  → ✓
                  已复制业务数据表    → ✓ 发票开具业务(数电票)数据表.xls
                  已复制参考图片素材  → ✓ 2 张截图
                  已适配本机路径      → ✓
                  
                  工程已生成到：USER_WORKSPACE/current_homework/
                  现在交给老师Agent进行框选指导 →
```


## 🔧 功能特性

### 🧱 系统层级架构

```
Skill.md > ASSET > REFERENCE > SCRIPTS > AGENTS > USER_WORKSPACE
```

| 层级 | 内容 | 职责 |
|------|------|------|
| 🥇 **SKILL.md** | 全局总控入口 | 最高优先级，统一调度所有子智能体 |
| 🥇 **ASSET/** | 作业资产库 | 表格、图片、代码模板、历史作业 |
| 🥈 **REFERENCE/** | 参考文档 | 课程规则、报错汇总、UI元素库、框选教学手册 |
| 🥉 **SCRIPTS/** | 核心脚本 | 资产检测、自动复制、路径修复、ID注入、安全重试 |
| 4️⃣ **AGENTS/** | 三大子智能体 | 各自 SKILL 文档 + 破障脚本工具 |
| 5️⃣ **USER_WORKSPACE/** | 用户工作区 | ID 配置、框选记录、最终作业 |

### 🧬 双场景自动路由逻辑

```
用户输入 → 总控SKILL判断意图 →
  ├─ "有源码/别人分享的" → 破障Agent(清ID) → 资产Agent(补素材) → 老师Agent(讲框选)
  ├─ "没有代码/从零开始" → 资产Agent(调模板) → 老师Agent(教框选) → 破障Agent(校验)
  ├─ "怎么框选/框哪里"   → 老师Agent(仅教学)
  ├─ "清除ID/有别人ID"   → 破障Agent(仅清除)
  ├─ "补素材/缺表格"     → 资产Agent(仅补齐)
  └─ "检查作业/有风险吗" → 破障Agent(校验) → 老师Agent(验收)
```

### 🔬 源码 ID 清洗管线

```
扫描 .py → 匹配 Base64 / UUID / 32位hex
扫描 .json → 检测 auth/token/task_id/user_id/assess_id/utask_id/loginer
扫描 .variable.json → 清空 defaultValue 中的默认 ID
扫描 .flow.json → 检测 URL 路径中的硬编码参数
替换 → PLACEHOLDER → 输出清洗报告
```

### 🕰️ 框选可视化教学手册

4 篇完整教学文档，覆盖框选全流程：

| 手册 | 内容 |
|------|------|
| 01_框选区域位置说明.md | 每个元素在哪页、什么位置、怎么框 |
| 02_框选对应功能详解.md | 框了这个元素，程序会做什么 |
| 03_正确框选范围标准.md | 框多大才算对、不同元素的标准 |
| 04_常见框选错误扣分点.md | 8种常见错误、扣多少分、怎么修正 |


## 📂 项目结构

```
Big-Data-and-Accounting-RPA-skills/
├── SKILL.md                                   # 全局总技能入口（最高优先级）
├── README.md                                  # 本文件
│
├── ASSET/                                     # 第1层：全局作业资产库
│   ├── excel_template/README.md               # 8个业务表格索引
│   ├── img_asset/README.md                    # 19张图片分类索引
│   ├── py_base_template/
│   │   └── standard_workflow.py               # 空白标准代码模板（426行）
│   └── homework_history/                      # 历史作业归档
│
├── REFERENCE/                                 # 第2层：全局参考文档
│   ├── course_rule.md                         # 考核规则 + 评分标准
│   ├── error_summary.md                       # 30种常见报错汇总
│   ├── ui_element_lib.md                      # UI元素选择器库
│   └── ui_guide/                              # 框选可视化教学手册
│       ├── 01_框选区域位置说明.md
│       ├── 02_框选对应功能详解.md
│       ├── 03_正确框选范围标准.md
│       └── 04_常见框选错误扣分点.md
│
├── SCRIPTS/                                   # 第3层：全局核心脚本
│   ├── asset_exists_check.py                  # 资产缺失检测
│   ├── asset_auto_copy.py                     # 素材自动复制
│   ├── path_batch_replace.py                  # 批量路径替换
│   ├── runtime_id_input.py                    # 用户ID动态注入
│   ├── path_auto_fix.py                       # 本机路径适配
│   └── safe_retry.py                          # 安全重试机制
│
├── AGENTS/                                    # 第4层：三大细分智能体
│   ├── agent_teacher/SKILL_TEACH.md           # 老师教学
│   ├── agent_fix_crack/
│   │   ├── SKILL_FIX.md                       # 破障修复
│   │   ├── id_safe_refactor.py                # Base64 ID清洗
│   │   └── risk_check.py                      # 风控合规检测
│   └── agent_module_asset/SKILL_ASSET.md      # 模块资产
│
└── USER_WORKSPACE/                            # 用户独立工作区
    ├── user_id_config.yaml                    # 用户自填ID（零硬编码）
    ├── select_record.md                       # 框选操作记录（防查重）
    └── current_homework/                      # 最终可提交的作业
```


## ⚠️ 注意事项

**原材料质量决定作业质量。** 不同场景的关键资源不一样：

| 场景 | 信源优先级（高 → 低） |
|------|----------------------|
| 🧬 有源码改作业 | 他人源码工程 › 配套数据表 › 控件选择器 |
| 🆕 无源码做作业 | 资产库标准模板 › 业务数据表 › UI截图参考 |

**有源码场景：** 务必先让破障Agent扫描清除他人ID，否则直接提交=0分+风控。

**无源码场景：** 框选操作的精度直接影响作业评分。框偏10px扣5分，框偏20px扣15分——建议逐步骤核对框选教学手册。

**ID自主提交：** 系统全程不保存你的ID。关闭会话后ID即清除，无残留、无泄露。

目前是 v1.0 正式版本，如有问题请直接反馈！


## 📄 核心资产清单

| 类型 | 数量 | 说明 |
|------|------|------|
| 🤖 机器人代码资产 | 7 套 | 电子税务 + 发票 + 网银全套 |
| 📊 业务数据表 | 8 张 | 每种机器人配套输入数据 |
| 🖼️ UI截图素材 | 19 张 | 6 大业务场景分类索引 |
| 📝 教学文档 | 4 篇 | 框选位置/功能/标准/扣分全面覆盖 |
| 🔧 **风控应急手册** | `REFERENCE/risk_emergency_manual.md` | 风控等级判定、应急处理步骤、账号解封流程 |
| 🐍 **环境初始化脚本** | `SCRIPTS/env_init.py` | 一键检测 Python/Pillow/资产/目录，自动安装依赖 |
| 📋 SKILL文档 | 4 个 | 总控 + 三大子智能体 |
| 📚 参考文档 | 4 篇 | 课程规则/报错汇总/UI元素库/风控应急手册 |


Asset Base: `f:\RPA(1)\` · Skills: `.trae/skills/` · 引擎: SOLO AI Agent · License: MIT
