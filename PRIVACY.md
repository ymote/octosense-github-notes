# GitHub Notes privacy

[简体中文](PRIVACY.zh-CN.md) · Applies to version 0.2.x · 2026-10-08

Publisher: **ymote**. This describes the code in this repository and its required
OctoSense host services; live GitHub authorization/write acceptance is still
pending. GitHub Notes has no publisher-operated backend or analytics endpoint,
and does not create an OctoSense cloud account.

## Data on your device

The app keeps Markdown, the selected account's opaque connection handle,
repository owner/name, branch, file path, blob SHA, commit message and unsaved
state. `draft-a.json` and `draft-b.json` alternate verified local snapshots;
`recovery.json` holds the previous replaced draft. Drafts persist across restart
and disconnect. Repository/file lists and account labels are also displayed
while the app is open. The manifest requests a 4 MiB app storage allowance and
account selection (`storage.accounts: true`). The editor accepts documents up
to 512 KiB.

Draft files are ordinary local JSON in the host's private app-data jail, not
app-encrypted files. Device backups and local filesystem access follow your OS
and OctoSense configuration. OAuth connection metadata (account identity,
scopes and selected handle) is separate host data. Provider tokens stay in the
host credential vault (macOS Keychain on the supported platform); scripts receive
handles, never tokens. This is a code boundary, not a guarantee that a compromised
host or device cannot access data.

## Data sent to GitHub

Only connecting, browsing, loading or explicitly approving a save uses the host
GitHub connector. The app has no direct network grant. The host uses
`github.com` for OAuth device authorization and token exchange and `api.github.com`
for identity, repository/file listing, file reading and commits. GitHub receives
the necessary authorization and request metadata. An approved save sends the
chosen repository/branch/path, exact Markdown, commit message and existing blob
SHA where applicable. Your GitHub account's commit identity is used by GitHub.
Public repository content and commit history can be publicly visible; private
repository visibility follows GitHub permissions.

**Connect GitHub** with **Public repositories** chosen requests `read:user` and
`public_repo`. With **Public and private repositories** chosen, or through
**Include private repositories**, it instead requests `read:user` and `repo`.
These OAuth scopes grant broader provider access than a single selected note;
the host sheet explains them before consent. Every app-initiated write goes
through the host's exact review sheet. Selecting an account or typing a draft
does not itself commit a file. A failed response can leave a remote outcome
unknown; check GitHub before another approved attempt.

## Agents and other recipients

The app has no in-app Chat interface, direct model calls, background scheduler,
telemetry endpoint or publisher data upload. The OctoSense shell separately
reads the explicit foreground `agent` declaration, `AGENT.md` and
private read tools in this bundle and offers **Ask GitHub Notes**. That optional
host-provided agent requires separate consent; installing the app or connecting
GitHub does not grant that consent. You can decline it or turn it off in
OctoSense's Assistant settings and still edit notes manually.

If you use the shell agent, your questions, conversation context and permitted
tool results may be sent to the model/provider configured in OctoSense. This can
include repository names, file metadata, note contents and Markdown you include
in the conversation. That content may leave your device and is subject to the
configured provider's data practices; it is not sent to a publisher-operated
model service. Review the host's agent disclosure and provider settings before
using Ask with private information.

The bundle declares three host-backed read aliases for repositories, file
metadata and note content. All are `private_data: true`, `shareable: false` and
`background: false`; no credential, commit or approval tool is exposed. Access
remains subject to host agent, app and account authorization. The shell's Ask
surface and brokered tool execution were not validated by this app's provider
fixture tests; this disclosure describes the host code, not a live-model test.

Remote Markdown images are retained as text and are not fetched by this editor.
Opening the external authorization browser is subject to GitHub and browser
policies. The broader OctoSense shell and user-installed integrations may have
their own data practices; this document covers this app and the named connector.

## Disconnect, deletion and support

**Disconnect**, once confirmed, revokes this app's local handle and asks the host
to delete its stored credential. It does not revoke the OAuth application's grant
on GitHub, erase local drafts, or delete repository files or commit history. For
provider-side revocation, use GitHub's authorized OAuth applications settings.
The app currently has no in-app erase-all action; to remove local drafts, close
it and use your host's app-data removal controls or remove its private app-data
directory. Host connection data, backups and provider history must be managed
separately; secure erasure is not promised.

[Support issues](https://github.com/ymote/octosense-github-notes/issues) are public.
Do not attach tokens, OAuth codes, private notes, repository contents or raw
profiles/logs. Use fictional reproductions and redacted screenshots. Anything
you voluntarily post there is processed by GitHub and visible to issue readers.

Source: [app](bundle/main.splash), [manifest](bundle/manifest.json),
[tools](bundle/tools.json), pinned host
[OAuth flow](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/authorize.rs),
[connection store](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/store.rs),
[GitHub API](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/api.rs) and
[review service](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/crates/oauth-service/src/host_api.rs).

The optional shell agent is defined by the versioned host's
[agent discovery](https://github.com/OctoSense-org/OctoSense/blob/4109d59db899525c7caa2229cd4117d62bc720d5/crates/shell/src/apps.rs),
[consent and peer preparation](https://github.com/OctoSense-org/OctoSense/blob/4109d59db899525c7caa2229cd4117d62bc720d5/crates/shell/src/agents.rs)
and [Ask conversation](https://github.com/OctoSense-org/OctoSense/blob/4109d59db899525c7caa2229cd4117d62bc720d5/crates/shell/src/app_chat/mod.rs).
