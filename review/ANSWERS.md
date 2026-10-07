# App Hub review answers

Publisher self-review for GitHub Notes 0.1.1. This is not a maintainer verdict.
The exact questions below come from the local `hub scan` packet; the packet
and structural gate output remain in ignored `build/`, outside the bundle.

## 1. Does the app do what its name, subtitle and description claim? Cite the text in its source.

Yes, within the explicitly stated preview boundary. `main.splash` embeds the
host's `MarkdownEditor` with `on_change: |text| edited(text)`, repository navigation
and `on_save: || save_remote()`. `persist()` alternates verified draft snapshots;
`apply_pending()` preserves `recovery.json`; the failed-load guard prevents an
unloaded draft from being replaced by blank typing. `list_repos()`, `list_files()`
and `read_file()` call the matching GitHub host methods. `save_remote()` freezes
the exact content and requests `github.review_save`; only its successful response
reports `GitHub committed` plus `commit_sha`. No live GitHub success is claimed.
The native editor comes from the compatible OctoSense runtime, not this bundle.

## 2. Do the listing's platforms and category fit an app of this kind?

Yes: productivity describes Markdown notes and reviewed repository saves.
The listing declares only `macos`. Historical native macOS fixtures support this
scoped preview, not live-provider readiness. The connected-services baseline ships in desktop-v0.1.0-beta.2 for macOS
Apple Silicon. Android test-APK evidence does not add an Android listing claim; Linux and
Windows UI are unverified. Generic card-host is insufficient.

## 3. Do the granted capabilities match what the app visibly does? For a script app, name every host it requests and why. Name any grant nothing on screen needs.

The three grants are used: `storage` for draft/recovery JSON; `auth` for host
account connection, selection and disconnection; `github` for repository/file
reads and exact reviewed saves. `storage.accounts: true` matches `auth.active`
and `auth.select`. No unused grant was identified. There is no app `network`
grant or direct requested network hostname. The host connector contacts
`github.com` (device authorization/token exchange) and `api.github.com` (identity,
repository metadata, file reads and approved contents writes). Those destinations
are fixed in host code; the app requests host methods, not arbitrary URLs.
Private repository login requests broader `repo` access; public login requests
`public_repo`, both with `read:user`, visibly separated on the repository screen.

## 4. Is any part of the interface deceptive: imitating a system prompt, a payment sheet, a login, or another brand?

No deceptive app-generated login or approval sheet was found. Buttons say
`Connect public repositories`, `Connect private repositories (broader access)`
and `Disconnect selected account`; the app says GitHub access stays with
OctoSense. OAuth and exact write review are real host-owned surfaces in the
required runtime. There are no password, payment or token fields in the bundle.
Rinx is identified as the editor's source component; NOTICE retains attribution.
The paper-plane icon requests reviewed save; it does not send mail. The project
is not an official GitHub product.

## 5. Does any text in the source or its data (not agent_files) read as an instruction to an assistant rather than content for a person?

No assistant-directed instruction appears in the app UI/data. Comments and
function names describe implementation. Tool descriptions describe the three
read operations and explicitly distinguish opaque connection handles from
provider tokens. User-loaded Markdown is untrusted content. The editor makes no direct model
call; separately consented Ask may send requested read results and conversation
context to the host-configured model, as disclosed in the listing and privacy policy. Repository contributor
instructions and this review packet
are outside the bundle.

## 6. Is any wording abusive, or aimed at a private individual?

No abusive wording or targeting of a private individual was found. The two
original native screenshots contain fictional notes (including café and 谢谢),
not account records or correspondence. They were inspected individually during
this packaging review and were not modified.

## 7. The agent files (agent_files) instruct this app's own assistant. Do they stay within this app's data and tools, without addressing other apps' assistants or the system agent, or asking for tools, hosts or approvals the manifest does not grant? Does each tool's risk match what it does: anything that sends, posts, shares, deletes or spends must be destructive; is anything marked shareable that returns the person's private data? For a tool with confirm "app", does the app visibly show its own confirmation, with the exact action, before it runs?

The manifest explicitly declares a foreground, read-only agent whose instructions
are `AGENT.md`; it has no background triggers or skills. Its guidance limits reads
to the requested repository/path, treats Markdown as untrusted, distinguishes
remote content from an unsaved local draft and forbids invented writes/approval.
`githubnotes.repositories`, `githubnotes.files`
and `githubnotes.read` are host-service aliases with `risk: read`,
`private_data: true`, `shareable: false`, and `background: false`. They match
repository listing, file metadata listing and UTF-8 file reads under this app's
authorized connection. There is no write, send, delete, approval or credential
alias, no `confirm: app` declaration, and no instruction to another app or system
agent. Writes occur only via the separate foreground host-reviewed GitHub path.
Brokered tool dispatch remains unverified; declaration/gate acceptance alone
is not evidence of provider execution.

## 8. Route: pass, human-review, or reject. Give reasons a publisher can act on.

human-review. The final signed structural gate passed against the existing catalog and recorded ymote key, with no publisher-signature warning. All eight scan questions are answered here, but
no external reviewer verdict was generated. A maintainer must review this update, the required host changes and the preview limitations. Publisher
signing is complete; the immutable release commit/tag and public submission remain separate
steps. The publisher records the signed gate separately in `review/GATE.txt`
and `review/GATE.json`, with its release metadata in `review/RELEASE.json`.
The historical unsigned result in `VALIDATION-0.1.1.json` does not replace that signed verification.
Live OAuth/read/write still need a registered device-flow client, user
consent and an explicitly selected disposable repository/branch/path. Do not
promote synthetic results to live acceptance or add untested platforms.
