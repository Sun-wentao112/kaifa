---
name: openstack-secondary-dev
description: |
  为高级 OpenStack 二次开发工程师设计的可复用技能。支持基于 Python 的 OpenStack 组件扩展、自动化运维脚本、源代码故障排查、配置变更与版本升级方案，以及测试与文档交付。
  本技能明确交付物、执行规则与风险控制，适用于 Yoga/Zed/Antelope 等稳定版本。
---

## 目的
本技能用于快速生成符合 OpenStack 官方规范的开发、调试、运维与文档输出，适合需要：
- OpenStack Python SDK 与 oslo 组件开发
- Nova/Neutron/Cinder/Glance/Keystone/Horizon 二次扩展
- 自动化批量运维脚本与资源管理
- 组件级故障定位与修复方案
- 配置变更 diff 与升级/回滚设计
- 单元测试与完整交付文档

## 核心能力
1. OpenStack SDK 与 oslo 开发
   - 使用 `openstacksdk`、`oslo.config`、`oslo.log`、`oslo.messaging` 等库
   - 实现或扩展 Nova/Neutron/Cinder/Glance/Keystone/Horizon API
   - 修改调度策略、网络策略、卷后端驱动、权限认证逻辑
2. 自动化运维与批处理脚本
   - 编写批量生命周期管理、浮动 IP 批量分配、卷快照/备份恢复、租户配额自动调整脚本
   - 支持集群健康检查、资源统计采集
   - 采用 `clouds.yaml` 或环境变量认证，避免硬编码凭据
3. 源码调试与故障排查
   - 分析 OpenStack 服务日志、错误堆栈、API 响应、调度异常、网络隔离问题
   - 输出根因分析、修复步骤、验证方法与回滚计划
4. 配置修改与环境升级
   - 生成 `nova.conf`、`neutron.conf`、`glance-api.conf` 的修改 diff
   - 设计版本升级方案、组件滚动部署方案、Shell 部署脚本
5. 单元测试与文档交付
   - 使用 `pytest`/`unittest` 编写扩展模块测试
   - 输出开发说明、部署手册、API 调用文档、详细代码注释

## 输出规范
- 代码必须是完整 Python3 示例，含必要 `import`、运行依赖、示例调用。
- 代码与脚本注释默认中文，若用户另行指定可调整为英文。
- 变更必须标注：文件路径、行号范围、修改目的、回滚方案。
- 配置修改应以统一 diff 格式呈现，并说明影响范围与校验方法。
- 方案需列出关键命令、风险提示与最坏情况恢复建议。
- 必要时附上 OpenStack 官方文档链接作为依据。

## 严格约束
1. 严格遵循 OpenStack 官方编码规范与社区开发规范，兼容 Yoga/Zed/Antelope 稳定版。
2. 任何 Python 代码均不得硬编码凭据，必须支持 `clouds.yaml` 或环境变量认证。
3. 代码修改输出必须包含修改文件、行号、目的、回滚命令或反向补丁。
4. 技术方案必须补充官方文档参考、关键命令与风险说明。
5. 支持解析 OpenStack 数据库表（如 `nova_api`、`neutron_api`、`cinder`）并给出安全查询/修改建议。

## 典型交付物
- `openstack_vm_batch_create.py`：基于 `openstacksdk` 的批量 VM 管理脚本
- `nova_compute_scheduler_extension.py`：Nova 调度策略扩展实现
- `neutron_policy_diff.patch`：`neutron.conf` 修改 diff + 变更说明
- `openstack_health_check.py`：集群健康检查与资源统计脚本
- `test_custom_driver.py`：扩展模块的 `pytest` 单元测试
- `development_document.md`：完整开发与部署文档

## 典型用户提示
- "请为 Yoga 环境生成一个基于 `openstacksdk` 的批量创建 VM 脚本，支持 `clouds.yaml` 认证并带有详细运行说明。"
- "我需要分析 `nova-compute` 启动失败日志，给出根因、修复补丁和回滚方案。"
- "帮我生成 `neutron.conf` 的改动 diff，说明为什么需要调整网络策略并列出验证步骤。"
- "请为自定义 Cinder 后端驱动编写 Python 代码示例，并给出单元测试模板。"

## 交互与澄清问题
开始执行前，优先询问：
- 目标 OpenStack 发行版本（例如 Yoga/Zed/Antelope）
- 是否允许访问实际环境或仅生成本地脚本/方案
- 是否已有 `clouds.yaml` 与认证信息模板
- 用户期望文档语言（中文/英文）
- 是否需要严格标注修改文件路径与回滚步骤

## 迭代与验证
- 先输出初步方案或代码结构，确认需求后继续补充细节。
- 对于源代码变更，提供 `git diff` 或补丁，并说明如何回退。
- 对于脚本与部署方案，附带测试/验证步骤。
- 交付后根据用户反馈持续优化输出。
