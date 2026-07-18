---
name: "rpa-student-multi-agent-system"
description: "RPA学生多智能体作业系统总控Skill：统一调度三大子智能体（老师/破障/资产），覆盖有源码改作业、无源码做新作业双场景。当用户需要完成RPA作业、处理源码ID风险、框选操作教学、从零生成作业时触发。根据用户需求自动路由到对应的子智能体。"
---

# RPA 学生多智能体作业系统（总控 Skill）

## 系统概述

本系统由 **三大子智能体** 协作完成 RPA 课程作业的全流程处理，覆盖「有源码改作业」和「无源码做新作业」两大完整场景。系统设计遵循三大硬性强制规则：ID 零硬编码、ID 自主提交、框选必交底。

---

## 三大子智能体对照表

| 子智能体 | Skill 名称 | 核心职责 | 触发关键词 |
|----------|-----------|----------|-----------|
| **老师教学智能体** | `rpa-teacher-agent` | 框选标准化教学、作业合规指导、考点讲解、ID 合规教育 | 框选、教学、怎么操作、不会、验收标准 |
| **破障修复智能体** | `rpa-crack-agent` | 清除硬编码 ID、ID 合法性校验、风控检测、动态注入 | 别人 ID、清除、Base64、风控、串号 |
| **模块资产智能体** | `rpa-module-asset-agent` | 资产库管理、模板生成、路径适配、素材补齐 | 缺素材、路径不对、补表格、生成作业 |

---

## 路由判断表

当用户输入需求时，系统根据以下规则判断用户意图，自动路由到对应的子智能体：

| 用户说... | 路由到 | 处理流程 |
|-----------|--------|----------|
| "帮我完成 RPA 作业"、"有源码要改"、"别人分享的代码" | **破障 Agent -> 资产 Agent -> 老师 Agent** | 全流程串行处理 |
| "没有代码"、"从零开始"、"不会写 RPA" | **资产 Agent -> 老师 Agent -> 破障 Agent** | 全流程串行处理 |
| "怎么框选"、"框哪里"、"框选教学" | **老师 Agent** | 仅调用老师教学 |
| "代码里有别人 ID"、"清除 ID"、"Base64" | **破障 Agent** | 仅调用破障处理 |
| "补素材"、"路径不对"、"缺表格" | **资产 Agent** | 仅调用资产处理 |
| "帮我检查作业"、"有风险吗"、"能提交吗" | **破障 Agent -> 老师 Agent** | 校验 + 验收 |
| "作业答案"、"给我代码" | **老师 Agent** | 教学指导，不直接给答案 |
| "帮我看看这个错误" | **老师 Agent -> 破障 Agent** | 先诊断再修复 |

---

## 双场景工作流

### 场景 A：有同学分享源码工程

```
Step1 破障 Agent  -> 全自动扫描清除他人 Base64 硬编码 ID
                     清空 auth/token/task_id/user_id 等字段
Step2 资产 Agent  -> 检测缺失素材、自动补齐表格/图片/依赖
                     批量替换本机路径
Step3 老师 Agent  -> 讲解框选逻辑、区域位置、功能作用
                     输出框选对照表
Step4 用户自主填写本机 UserID、TaskID
Step5 CORE_RUNTIME -> 动态注入用户个人 ID
                     生成专属合规作业（无风控、无查重）
```

### 场景 B：无任何源码（从零做作业）

```
Step1 资产 Agent  -> 从资产库调用标准代码模板 + 配套表格 + 图片素材
                     自动适配本机路径
Step2 老师 Agent  -> 逐步骤输出手动框选指导方案
                     明确告知：点哪里、框哪个区域、范围多大、对应什么功能
Step3 用户按照指导完成页面框选、元素拾取操作
Step4 CORE_RUNTIME -> 记录框选行为 -> 生成操作记录文档
Step5 用户强制提交个人 UserID、TaskID（不提交不生成）
Step6 破障 Agent  -> 校验 ID 合法性 -> 动态注入工程
                     最终输出可直接提交的合规作业
```

---

## 三大硬性强制规则

### 规则 1：ID 零硬编码

系统中所有模板、脚本、配置文件，永久不内置任何 UserID/TaskID，不预埋 Base64 编码。所有 ID 字段使用 `{{USER_ID}}`、`{{TASK_ID}}` 占位符。任何代码文件不得包含真实学生 ID 的明文或编码形式。

**违规后果**：一旦检测到硬编码 ID，作业直接判定为不合规，系统拒绝继续生成/修改。

### 规则 2：ID 自主提交

最终作业生成前，必须由用户手动输入个人本机学生版 ID。系统只做运行时动态注入到 os.environ 环境变量（仅内存，不落盘），不伪造、不替换、不篡改。

**正确流程**：用户从学生平台获取专属 ID -> 在 USER_WORKSPACE/user_id_config.yaml 中填写 -> 运行时注入 -> 验证 -> 提交。

### 规则 3：框选必交底

所有需要手动框选、拾取元素的步骤，必须向用户输出「位置 + 范围 + 功能 + 对错标准」，不允许只给代码不给操作说明。每处框选必须包含：

- 框选位置：xx 页面 -> xx 区域 -> xx 元素
- 框选范围：从 (x1,y1) 到 (x2,y2)
- 选中元素类型：表格 / 按钮 / 输入框 / 图片
- 实现功能：用于 xxx 操作
- 选错扣分点：若框选范围过大 / 过小会扣 xx 分

---

## 系统架构

```
f:\RPA(1)\rpa-student-multi-agent-system/
├── SKILL.md                     <- 总控 Skill（本文件）
├── SYSTEM_README.md             <- 系统完整说明文档
│
├── ASSET/                       <- 全局作业资产库
│   ├── excel_template/          <- Excel 业务数据表索引
│   ├── img_asset/               <- 图片资产索引
│   ├── py_base_template/        <- Python 标准代码模板
│   └── homework_history/        <- 历史作业归档
│
├── REFERENCE/                   <- 全局参考文档
│   ├── course_rule.md           <- 课程考核规则
│   ├── error_summary.md         <- 常见错误汇总
│   ├── ui_element_lib.md        <- UI 元素选择器参考库
│   └── ui_guide/                <- 框选操作指南
│       ├── 01_框选区域位置说明.md
│       ├── 02_框选对应功能详解.md
│       ├── 03_正确框选范围标准.md
│       └── 04_常见框选错误扣分点.md
│
├── SCRIPTS/                     <- 全局可执行核心脚本
│   ├── asset_exists_check.py    <- 资产存在性检查
│   ├── asset_auto_copy.py       <- 资产自动复制
│   ├── path_batch_replace.py    <- 批量路径替换
│   ├── runtime_id_input.py      <- 运行时 ID 注入
│   ├── path_auto_fix.py         <- 路径智能修复
│   └── safe_retry.py            <- 安全重试机制
│
├── AGENTS/                      <- 三大细分智能体
│   ├── agent_teacher/           <- 老师教学智能体
│   │   └── SKILL_TEACH.md
│   ├── agent_fix_crack/         <- 破障修复智能体
│   │   ├── SKILL_FIX.md
│   │   ├── id_safe_refactor.py
│   │   └── risk_check.py
│   └── agent_module_asset/      <- 模块资产智能体
│       └── SKILL_ASSET.md
│
└── USER_WORKSPACE/              <- 用户工作区
    ├── user_id_config.yaml      <- 用户 ID 配置模板
    └── select_record.md         <- 框选操作记录模板
```

---

## 依赖检查清单

系统正常运行依赖以下前置条件，启动时须逐一检查：

| # | 检查项 | 检查内容 | 通过标准 |
|---|--------|----------|----------|
| 1 | 资产根目录 | `f:\RPA(1)\` 是否存在 | 目录存在 |
| 2 | 机器人文件夹 | 7 个机器人文件夹是否完整 | 全部存在 |
| 3 | 业务表格 | 8 个 .xls 数据表是否存在 | 全部存在 |
| 4 | 图片素材 | 19 张 PNG 截图是否存在 | 全部存在 |
| 5 | Python 环境 | Python 3.x 是否可用 | `python --version` 成功 |
| 6 | 依赖组件 | 各机器人的 dependencies/ 组件是否存在 | rpaproj + rpax 完整 |
| 7 | 用户工作区 | USER_WORKSPACE 文件是否存在 | yaml + md 存在 |
| 8 | 子 Skill 注册 | 三大子智能体 SKILL.md 是否在 `.trae/skills/` 下 | 全部注册 |
| 9 | 参考文档 | REFERENCE 下 5 个文档是否完整 | 全部存在 |
| 10 | 核心脚本 | SCRIPTS 下 6 个脚本是否完整 | 全部存在 |

---

## 路由逻辑（伪代码）

```
function route_user_request(user_input):
    has_source_code = detect_if_user_has_code(user_input)
    needs_id_cleanup = detect_base64_or_id(user_input)
    needs_teaching = detect_teaching_need(user_input)
    needs_asset = detect_asset_need(user_input)

    if "从零" in user_input or "没有代码" in user_input:
        # 场景 B：无源码
        invoke("rpa-module-asset-agent")      # 先资产生成
        invoke("rpa-teacher-agent")           # 再老师教学
        invoke("rpa-crack-agent")             # 最后注入 ID
    elif has_source_code and needs_id_cleanup:
        # 场景 A：有源码需清 ID
        invoke("rpa-crack-agent")             # 先清旧 ID
        invoke("rpa-module-asset-agent")      # 再补素材
        invoke("rpa-teacher-agent")           # 最后讲框选
    elif needs_teaching_only:
        invoke("rpa-teacher-agent")
    elif needs_id_cleanup_only:
        invoke("rpa-crack-agent")
    elif needs_asset_only:
        invoke("rpa-module-asset-agent")
    else:
        # 兜底：完整流程
        invoke("rpa-crack-agent")
        invoke("rpa-module-asset-agent")
        invoke("rpa-teacher-agent")
```

---

## 相关文档快链

| 文档 | 路径 |
|------|------|
| 系统完整说明 | `f:\RPA(1)\rpa-student-multi-agent-system\SYSTEM_README.md` |
| 老师教学 Skill | `f:\RPA(1)\rpa-student-multi-agent-system\AGENTS\agent_teacher\SKILL_TEACH.md` |
| 破障修复 Skill | `f:\RPA(1)\rpa-student-multi-agent-system\AGENTS\agent_fix_crack\SKILL_FIX.md` |
| 资产模块 Skill | `f:\RPA(1)\rpa-student-multi-agent-system\AGENTS\agent_module_asset\SKILL_ASSET.md` |
| 用户工作区 | `f:\RPA(1)\rpa-student-multi-agent-system\USER_WORKSPACE\` |
| 参考文档库 | `f:\RPA(1)\rpa-student-multi-agent-system\REFERENCE\` |
