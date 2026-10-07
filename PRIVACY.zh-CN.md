# GitHub Notes 隐私说明

[English](PRIVACY.md) · 适用于 0.1.0 · 2026-10-06

发布者：**ymote**。本文说明本仓库代码及所需 OctoSense 宿主服务的行为；
真实 GitHub 登录和写入仍待验收。应用没有发布者运营的后端或统计端点，
也不会创建 OctoSense 云账户。

## 本机数据

应用保存 Markdown、所选账户的不透明连接句柄、仓库所有者和名称、分支、文件路径、
blob SHA、提交信息及未保存状态。`draft-a.json` 与 `draft-b.json` 交替写入并校验；
`recovery.json` 保存上次替换的草稿。重启或断开连接后仍保留草稿。
使用期间还会显示仓库/文件列表和账户标签。清单申请 4 MiB 应用存储额度和
账户选择能力（`storage.accounts: true`）；编辑器文档上限为 512 KiB。

草稿是宿主应用私有数据目录中的普通 JSON，应用没有为其另行加密。
备份和文件访问由操作系统及 OctoSense 配置决定。账户标识、授权范围和所选句柄等
连接元数据属于独立的宿主数据。提供商令牌保存在宿主凭据库中（受支持 macOS 上为
Keychain），脚本只获得句柄，不获得令牌。这是代码权限边界，并不保证受入侵的宿主
或设备无法访问数据。

## 发送给 GitHub 的数据

连接、浏览、加载或明确批准保存时，应用调用宿主 GitHub 服务，没有直接网络权限。
宿主通过 `github.com` 完成 OAuth 设备授权和令牌交换，通过 `api.github.com`
读取身份、仓库/文件列表、文件以及提交。GitHub 会收到必要的授权及请求元数据。
批准保存后发送选定仓库、分支、路径、准确的 Markdown、提交信息及适用的原文件 SHA。
提交身份由 GitHub 根据账户处理。公共仓库内容及历史可能公开；私有仓库可见性遵循
GitHub 权限。

**Connect public repositories** 请求 `read:user` 和 `public_repo`；
**Connect private repositories** 则请求 `read:user` 和 `repo`。
这些 OAuth 范围比单个笔记更广，宿主弹层会在授权前解释。应用发起的每次写入均通过
宿主精确审阅弹层。选择账户或编辑草稿不会自动提交。响应失败可能导致远端结果未知，
请先检查 GitHub，再决定是否重新批准。

## 代理与其他接收方

应用没有模型调用、聊天代理、后台调度、统计端点或向发布者上传数据的逻辑。
三个宿主只读别名提供仓库列表、文件元数据和笔记读取；均为 `private_data: true`、
`shareable: false`、`background: false`，没有凭据、写入或审批工具。
访问仍受宿主应用和账户授权限制。模拟提供商测试没有证明代理转发执行路径。

远程 Markdown 图片保留为文本，编辑器不会加载其像素。外部授权浏览器受 GitHub
和浏览器政策约束。OctoSense 的其他功能及用户安装的集成可能另有数据行为，
本文仅覆盖本应用与上述连接服务。

## 断开、删除与支持

**Disconnect selected account** 撤销本应用的本地连接句柄，并请求宿主删除对应凭据。
它不会撤销 GitHub 端 OAuth 应用授权，也不会删除本地草稿、仓库文件或提交历史。
提供商侧撤权需在 GitHub 的已授权 OAuth 应用设置中操作。
应用目前没有“清除全部”按钮；删除草稿需先关闭应用，再使用宿主的数据清除功能或
删除本应用的私有数据目录。宿主连接数据、备份和远端历史需分别处理；不保证安全擦除。

[支持 issue](https://github.com/ymote/octosense-github-notes/issues)是公开的。
请勿上传令牌、OAuth 代码、私有笔记、仓库内容、原始配置或日志。
请用虚构内容复现并对截图脱敏。主动发到 issue 的内容会由 GitHub 处理，且对读者可见。

依据：[应用](bundle/main.splash)、[清单](bundle/manifest.json)、[工具](bundle/tools.json)，
以及固定宿主版本的 [OAuth 流程](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/authorize.rs)、
[连接存储](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/store.rs)、
[GitHub API](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/api.rs)和
[审阅服务](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/host_api.rs)。
