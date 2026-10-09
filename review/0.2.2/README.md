# GitHub Notes 0.2.2 candidate

0.2.2 rewrites the GitHub part of **Repository & file**. The editor, read tools,
permissions and persisted-draft format are unchanged.

## What changed

[0.2.1](00-before-0.2.1.png) had three equal buttons ("Connect public
repositories", "Connect private repositories (broader access)" and "Disconnect
selected account", even with nothing connected). Its status sat in a small line
at the bottom, and after connecting it kept saying "No GitHub connection",
because it never reloaded its account list.

- [One **Connect GitHub**](01-connect.png) action, with a plain-language choice
  of what the app can reach. **Public repositories** is the default and requests
  `read:user` + `public_repo`. [**Public and private
  repositories**](02-private-access.png) requests `read:user` + `repo`.
- [The host sheet](03-host-code.png) shows the one-time code; it comes from
  OctoSense ([#416](https://github.com/OctoSense-org/OctoSense/pull/416)).
- After approval, [an account card](04-connected.png) names the account and
  its access, and the repositories load at once. With public-only access, the
  list offers **Include private repositories**.
- [**Disconnect** asks first](05-confirm-disconnect.png) and says the note stays.
  [**Use another account**](06-another-account.png) lists the other connected
  accounts and can add one.
- A failed sign-in shows [**Not connected**](07-declined.png), with the reason
  in plain words and **Try again**. [A cancelled one](08-cancelled.png) says
  nothing was connected.
- The branch, path and commit fields draw a dark caret, since the theme's caret
  is white and was invisible on them. Every control on the screen shares one
  type scale, and [a wide window](09-wide-connected.png) keeps a 720 px column.

The script calls the same nine host methods as 0.1.0 and requests the same two
scope sets. [The contract test](../../tests/test_release_contract.py) now checks
those, where it used to pin the script's bytes. `tools.json` stays
byte-identical to 0.1.0.

## Evidence

`hub`, built from App Hub `655114c` (the tag workflow's pin), stamped the bundle.
Its [source gate](GATE.txt) passes with the expected unsigned-development
warning, and the [review questions](QUESTIONS.json) are unchanged from 0.2.1.
The four source-contract tests pass.

The final `main.splash` ran on a Linux build host under headless Weston, in
OctoSense's `connected-app-host` from #416 with its signed-out synthetic GitHub
(`--provider-fixture=github-sign-in`). The sign-in service, sheet and connection
store were real; only github.com was a fixture. That host installs only the
historical sample id, so the test copy carried
`org.octosense.samples.githubnotes`, as the sheet in 03 shows.

- Scripted runs passed: approve, disconnect confirm and cancel, the
  another-account panel, disconnect, decline, cancel, and a 1200×820 window.
  The images above come from them.
- OctoSense's `tools/connected-e2e/notes_signin.py` passed three runs in a row
  with this script.
- `tools/check-connected-oauth.py` passed: the real sheet, missing
  registration, Close, the local draft kept, and switching between two accounts.
- `tools/connected-e2e/notes.py` passed its first five checks: signed install,
  Unicode edit and restart, empty repository and pagination, refusing a
  dirty-note replacement, and exact host review and cancel. It then stops at
  **Approve & Save**, because remote input cannot activate the native approval.
  The 0.2.1 script stops at the same place on that host.

## Release and admission

The [v0.2.2 tag workflow](https://github.com/ymote/octosense-github-notes/actions/runs/37900013646)
released `e3f1e811` with pack sha256
`08061d70c4650298ead15ef7fb6b1d10702996fd5063195433ffa8f8e4349ff5`. Native
publisher unpack/verify and the gate passed on the downloaded pack against
catalog 14, and an independent review approved the candidate. The
[publication run](https://github.com/OctoSense-org/OctoSense-App-Hub/actions/runs/37902582113)
admitted it as public catalog 15
([App Hub `18cd41d`](https://github.com/OctoSense-org/OctoSense-App-Hub/commit/18cd41d)),
after a dry run had signed and verified the same payload. The public catalog
passes native `catalog-verify`, and its 0.2.2 pack equals the release asset.

## Not verified

Live GitHub OAuth, remote commits, physical approval, and installation or update
of 0.2.2 in a packaged macOS host from the public catalog.
