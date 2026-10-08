# GitHub Notes

[English](README.md)

在 OctoSense 中使用原生 Rinx 文章编辑器编写 Markdown，重启后保留本地草稿，
并在保存到 GitHub 前审阅准确的提交内容。发布者：**ymote**。
新应用 ID：`io.github.ymote.githubnotes`，版本：`0.2.1`。

这是 **macOS 开发预览候选版**。需要支持 contract 1.8.0／`publisher-github-v1`
及原生 Markdown 编辑器的兼容 OctoSense 宿主。`desktop-v0.1.0-beta.2`
无法安装此无独立密钥版本，通用 `card-host` 不能渲染此编辑器。
0.2.0 → 0.2.1 已在 `5e1a8414` 兼容打包宿主中通过真实签名安装、更新、编辑及重启检查；
官方兼容发行版仍待发布。真实 GitHub 授权及远程提交尚未验证。

## 安装与使用

请通过 [OctoSense App Hub 的 issue](https://github.com/OctoSense-org/OctoSense-App-Hub/issues)
申请发布。GitHub 标签产生可验证的发布文件，**不会**自动提交审核或收录。
管理员将此新 ID 发布到目录前，官方 App Hub 搜索中还没有此新应用。

收录后，在兼容宿主中依次选择 **App Hub → Search → GitHub Notes → Get → Install → Open**。
安装前检查应用 ID 和权限。

1. 在 Source、Split、Preview 中编辑；窄窗口切换 Source 和 Preview。
   样式面板还提供富文本块编辑及撤销、重做。
2. 文件图标打开 **Repository & file**。通过宿主弹层和外部浏览器连接 GitHub。
   宿主运营者需配置启用 device flow 的 GitHub OAuth 客户端；应用包不能包含令牌或密钥。
3. 选择账户、仓库、分支及 Markdown 文件；**Use as new path** 指定新目标。
   公共仓库请求 `read:user` + `public_repo`；私有仓库请求更广的 `read:user` + `repo`。
4. 填写提交信息后点击纸飞机图标，在宿主弹层审阅准确目标和 Markdown。
   仅在返回 commit SHA 后才算保存成功。

取消或失败会保留草稿。切换账户不会悄悄改变笔记目标；替换笔记保留一份恢复副本。
网络结果不确定时，先检查 GitHub，再决定是否重新批准发送。

## GitHub 管理的发布流程

无需额外生成开发者签名密钥，也无需仓库签名 secret。
经审阅的[标签工作流](.github/workflows/publish-app.yml)准备规范清单、获取 GitHub Actions
证明、验证证明，并发布 `app.bundle.pack.json`、`octosense-app-manifest.json`
及 `release-receipt.json`。每次更新都需新版本及不可变标签。

用兼容 Hub CLI 验证下载的文件：

```sh
hub publisher-unpack app.bundle.pack.json --out verified-bundle
hub publisher-verify verified-bundle
```

不要重新计算已验证包的摘要。仅对可编辑源代码运行：

```sh
hub stamp bundle
hub check bundle --allow-unsigned
mkdir -p build
hub scan bundle --packet build/review-packet.json
python3 -m unittest discover -s tests -v
```

在[提交 issue](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/158) 中补充成功工作流、发布文件、截图及[审核回答](review/0.2.0/ANSWERS.md)补充到申请 issue。
Hub 审核与管理员目录批准独立于 GitHub 发布文件。

## 证据与限制

编辑器、三个私有读取别名及账户／审阅逻辑沿用旧应用。
新的源代码及原生证据记录在 [review/0.2.0](review/0.2.0/README.md)和[已验证的 0.2.1 更新](review/0.2.1/README.md)。
原始截图仅含虚构笔记。初步编辑器检查不能证明当前 Shell 的签名安装、
真实 OAuth、远程写入、物理审批或模型执行。

可选 **Ask GitHub Notes** 代理需单独授权，可能将问题、对话上下文及获准读取的仓库
数据发送到宿主配置的模型。它仅前台、只读、不可共享，不能修改草稿、审批或提交。
不包含应用内聊天、直接模型调用、Glance 发布、Matrix 发布或图片上传。
文档上限为 512 KiB；仅声明 macOS，其他平台未验证。
参见[隐私](PRIVACY.zh-CN.md)、[支持](SUPPORT.md)及[署名](NOTICE)。

## 历史应用

旧 `org.octosense.samples.githubnotes` 的 0.1.0／0.1.1 发布、签名、`publisher.json`
及有日期的 `review/` 记录保持不变，仅作为历史资料。
它们不代表此新应用的身份或验证证据；不会自动迁移草稿、账户句柄或发布者所有权。
旧 App Hub [#121](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/121)
及 [#131](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/131)
描述旧版本，不是本次申请。
