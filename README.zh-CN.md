# GitHub Notes

[English](README.md)

在 OctoSense 中使用 Rinx 文章编辑器编写 Markdown，保留可恢复的本地草稿，
并在保存到 GitHub 前审阅完整提交内容。不需要另建 OctoSense 云账户。
发布者：**ymote**；应用 ID：`org.octosense.samples.githubnotes`；版本：`0.1.0`。

**macOS 预览版。** 需要包含
[OctoSense #347](https://github.com/OctoSense-org/OctoSense/pull/347) 和
[App Hub #119](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/119)
的兼容运行时，以及 `MarkdownEditor`、`auth`、`github` 宿主服务。
通用 App Hub `card-host` 无法运行此编辑器。真实 GitHub 登录和仓库写入仍未验证；
本仓库存在不代表应用已获公共 App Hub 收录。

## 使用

1. 应用获收录后，通过兼容 OctoSense 的 App Hub 目录安装。提交内容仅为 `bundle/`。
2. 在 Source、Split、Preview 中编写和预览；窄窗口在 Source 和 Preview 之间切换。
   样式面板还提供富文本块编辑、撤销和重做。
3. 左上返回/文件图标打开 **Repository & file**。通过宿主弹层及外部浏览器连接 GitHub。
   宿主需要配置已启用 device flow 的 GitHub OAuth 客户端；凭据不能写入应用包。
4. 选择账户、仓库、分支和 Markdown 文件；**Use as new path** 指定新文件路径。
   公共仓库授权请求 `read:user` + `public_repo`；私有仓库请求范围更广的 `read:user` + `repo`。
5. 填写提交信息，返回笔记，点击纸飞机图标。在宿主弹层中审阅准确的目标和 Markdown
   后再批准。只有 GitHub 返回 commit SHA，应用才报告提交成功。

取消或保存失败会保留草稿。切换账户不会悄悄改变当前笔记的提交账户。
替换文件会保留一份旧草稿恢复副本。网络结果不确定时，请先检查 GitHub 再重试，
应用不会自动重发。断开连接不会删除本地草稿或已提交的内容。
详见[隐私说明](PRIVACY.zh-CN.md)。

## 验证发布版本

发布者签名版本包含 `publisher.json`、签名检查输出 `review/GATE.txt` /
`review/GATE.json`，以及发布记录 `review/RELEASE.json` 和问题记录
`review/QUESTIONS.json`。读取 `publisher.json` 中的公钥后，检查原样应用包：

```sh
HUB=hub # or the path to a compatible hub binary
APP_PUBLISHER_PUBLIC_KEY="$(python3 -c 'import json; print(json.load(open("publisher.json"))["public_key"])')"
"$HUB" check bundle --publisher-key "ymote=$APP_PUBLISHER_PUBLIC_KEY"
```

此命令只读取公钥，不会修改应用包。发布者签名证明来源，
App Hub 收录仍须由维护者独立决定。

## 无需 GitHub 账户的测试

将本仓库与兼容 OctoSense 仓库放在同一级目录，在 macOS 的 **OctoSense** 目录运行：

```sh
cargo build --locked --release -p octosense-shell \
  --features mobile-apps,acceptance-fixtures \
  --example connected-app-host --example connected-install
python3 tools/connected-e2e/notes.py --bundle ../octosense-github-notes/bundle
```

测试临时签名应用副本，经真实 Store 安装，并使用模拟 GitHub 传输层和内存凭据库，
验证原生编辑器、账户权限和精确审阅流程。不会使用 GitHub CLI 登录或写入真实仓库。
普通构建不启用测试特性，测试也拒绝未标记的用户配置目录。
[固定版本的测试指南](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/tools/connected-e2e/README.md)包含手动运行方法。
以上是复现命令；更新发布信息后的应用包尚未重跑原生测试。

## 开发新版本

请使用未签名的开发副本，不要修改已发布的签名包。使用兼容 App Hub 的 `hub`
工具，在开发副本中运行：

```sh
hub stamp bundle
hub check bundle --allow-unsigned
mkdir -p build
hub scan bundle --packet build/review-packet.json
```

对已签名包重新计算摘要会使原签名失效。发布后的修改必须升级版本、重新计算摘要，
由发布者运行 `hub sign-manifest` 重新签名，再使用上述公钥检查。
`--allow-unsigned` 不会信任未知签名。密钥和审核报告不得放入 `bundle/`。[审核回答](review/ANSWERS.md)和
[来源记录](review/PROVENANCE.json)独立于应用包。

## 证据与限制

两张商店截图保留真实原生截图的原始字节，内容为虚构笔记，并非效果图。
历史[安装测试记录](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/github-notes/evidence/rinx-writer-installed/receipt.json)及
[像素审阅](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/github-notes/evidence/rinx-writer-installed/manual-review.json)覆盖文件选择、
Unicode 编辑、取消、模拟新建/更新提交、冲突、不确定响应和离线重启。
[编辑器持续测试](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/tools/connected-e2e/evidence/notes-rinx-soak-20261006/README.md)
记录了恢复保护修复前的十分钟 36 轮测试，以及修复后的 12 轮回归。
这些历史记录保留原来源摘要；本仓库仅调整发布信息，因此应用摘要也发生变化，
不能把历史记录称为新摘要的重新执行证据。

编辑器文档上限为 512 KiB。不包含 Rinx 的 Matrix 发布、图片上传或远程图片加载。
应用不提供聊天、模型代理或 Glance 发布。三个[只读工具别名](bundle/tools.json)
标记为私有数据、仅前台、不可共享；没有写入或审批工具。
真实 GitHub、物理审批、代理工具转发及 Windows/Linux 界面仍未验证。
独立 OnePlus 测试不等于本应用的 Android 发布验收；商店仅声明 **macos**。

[支持](SUPPORT.md) · [隐私](PRIVACY.zh-CN.md) · [署名](NOTICE) · [Apache-2.0](LICENSE)
