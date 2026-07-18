---
name: "Big-Data-and-Accounting-RPA-skills"
description: "RPA学生多智能体作业系统总控Skill：统一调度三大子智能体（老师/破障/资产），覆盖有源码改作业、无源码做新作业双场景。当用户需要完成RPA作业、处理源码ID风险、框选操作教学、从零生成作业时触发。根据用户需求自动路由到对应的子智能体。"
---

# RPA 学生多智能体作业系统 (总控Skill)

## 系统概述

本系统由 **三大子智能体** 协作完成RPA课程作业的全流程处理，覆盖「有源码改作业」和「无源码做新作业」两大完整场景。

---

## 三大子智能体

| 子智能体 | Skill名称 | 核心职责 |
|----------|-----------|----------|
| **老师教学智能体** | `rpa-teacher-agent` | 框选标准化教学、作业合规指导、考点讲解、ID合规教育 |
| **破障修复智能体** | `rpa-crack-agent` | 清除硬编码ID、ID合法性校验、风控检测、动态注入 |
| **模块资产智能体** | `rpa-module-asset-agent` | 资产库管理、模板生成、路径适配、素材补齐 |

---

## 触发入口

当用户提出以下需求时，由本总控Skill判断用户意图，自动路由到对应的子智能体：

### 路由判断表

| 用户说... | 路由到 | 说明 |
|-----------|--------|------|
| "帮我完成RPA作业"、"有源码要改"、"别人分享的代码" | **破障Agent → 资产Agent → 老师Agent** | 全流程串行处理 |
| "没有代码"、"从零开始"、"不会写RPA" | **资产Agent → 老师Agent → 破障Agent** | 全流程串行处理 |
| "怎么框选"、"框哪里"、"框选教学" | **老师Agent** | 仅调用老师教学 |
| "代码里有别人ID"、"清除ID"、"Base64" | **破障Agent** | 仅调用破障处理 |
| "补素材"、"路径不对"、"缺表格" | **资产Agent** | 仅调用资产处理 |
| "帮我检查作业"、"有风险吗"、"能提交吗" | **破障Agent → 老师Agent** | 校验+验收 |

---

## 路由逻辑（伪代码）

```
function route_user_request(user_input):
    has_source_code = detect_if_user_has_code(user_input)
    needs_id_cleanup = detect_base64_or_id(user_input)
    needs_teaching = detect_teaching_need(user_input)
    needs_asset = detect_asset_need(user_input)
    
    if "从零" in user_input or "没有代码" in user_input:
        # 场景B：无源码
        invoke("rpa-module-asset-agent")      # 先资产生成
        invoke("rpa-teacher-agent")           # 再老师教学
        invoke("rpa-crack-agent")             # 最后注入ID
    elif has_source_code and needs_id_cleanup:
        # 场景A：有源码需清ID
        invoke("rpa-crack-agent")             # 先清旧ID
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

## 双场景完整工作流

### 场景A：有同学分享源码工程

```
Step1 破障Agent → 全自动扫描清除他人Base64硬编码ID
                   清空auth/token/task_id/user_id等字段
Step2 资产Agent → 检测缺失素材、自动补齐表格/图片/依赖
                   批量替换本机路径
Step3 老师Agent → 讲解框选逻辑、区域位置、功能作用
                   输出框选对照表
Step4 用户自主填写本机UserID、TaskID
Step5 CORE_RUNTIME → 动态注入用户个人ID
                   生成专属合规作业（无风控、无查重）
```

### 场景B：无任何源码（从零做作业）

```
Step1 资产Agent → 从资产库调用标准代码模板+配套表格+图片素材
                   自动适配本机路径
Step2 老师Agent → 逐步骤输出手动框选指导方案
                   明确告知：点哪里、框哪个区域、范围多大、对应什么功能
Step3 用户按照指导完成页面框选、元素拾取操作
Step4 CORE_RUNTIME → 记录框选行为 → 生成操作记录文档
Step5 用户强制提交个人UserID、TaskID（不提交不生成）
Step6 破障Agent → 校验ID合法性 → 动态注入工程
                   最终输出可直接提交的合规作业
```

---

## 三大硬性强制规则

### 规则1：ID零硬编码
系统中所有模板、脚本、配置文件，永久不内置任何UserID/TaskID，不预埋Base64编码。所有ID字段使用 `{{USER_ID}}`、`{{TASK_ID}}` 占位符。

### 规则2：ID自主提交
最终作业生成前，必须由用户手动输入个人本机学生版ID。系统只做运行时动态注入，不伪造、不替换、不篡改。

### 规则3：框选必交底
所有需要手动框选、拾取元素的步骤，必须向用户输出「位置 + 范围 + 功能 + 对错标准」，不允许只给代码不给操作说明。

---

## 相关文档

| 文档 | 路径 |
|------|------|
| 全局总控Skill | `Big-Data-and-Accounting-RPA-skills/SKILL.md` |
| 系统完整文档 | `Big-Data-and-Accounting-RPA-skills/README.md` |
| 资产库（表格/图片/代码模板） | `Big-Data-and-Accounting-RPA-skills/ASSET/` |
| 参考文档（课程规则/错误/框选指南） | `Big-Data-and-Accounting-RPA-skills/REFERENCE/` |
| 核心脚本（ID注入/路径修复/安全重试） | `Big-Data-and-Accounting-RPA-skills/SCRIPTS/` |
| 老师教学智能体 | `Big-Data-and-Accounting-RPA-skills/AGENTS/agent_teacher/` |
| 破障修复智能体 | `Big-Data-and-Accounting-RPA-skills/AGENTS/agent_fix_crack/` |
| 模块资产智能体 | `Big-Data-and-Accounting-RPA-skills/AGENTS/agent_module_asset/` |
| 用户工作区 | `Big-Data-and-Accounting-RPA-skills/USER_WORKSPACE/` |

---

## 依赖检查

系统正常运行依赖以下前置条件：

- [ ] `f:\RPA(1)\` 资产根目录存在
- [ ] 7个机器人文件夹完整
- [ ] 8个业务表格文件存在
- [ ] Python 3.x 可用（pip install Pillow 如需要图片处理）
