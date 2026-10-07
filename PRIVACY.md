# GitHub Notes privacy

[简体中文](PRIVACY.zh-CN.md) · Applies to version 0.1.0 · 2026-10-06

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

**Connect public repositories** requests `read:user` and `public_repo`.
**Connect private repositories** instead requests `read:user` and `repo`.
These OAuth scopes grant broader provider access than a single selected note;
the host sheet explains them before consent. Every app-initiated write goes
through the host's exact review sheet. Selecting an account or typing a draft
does not itself commit a file. A failed response can leave a remote outcome
unknown; check GitHub before another approved attempt.

## Agents and other recipients

There is no model call, chat agent, background scheduler, telemetry endpoint or
publisher data upload in this app. It declares three host-backed read aliases
for repositories, file metadata and note content. All are `private_data: true`,
`shareable: false` and `background: false`; no credential, commit or approval tool
is exposed. Access remains subject to host app/account authorization. No
brokered-agent execution was proven by the provider fixture tests.

Remote Markdown images are retained as text and are not fetched by this editor.
Opening the external authorization browser is subject to GitHub and browser
policies. The broader OctoSense shell and user-installed integrations may have
their own data practices; this document covers this app and the named connector.

## Disconnect, deletion and support

**Disconnect selected account** revokes this app's local handle and asks the host
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
