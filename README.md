# GitHub Notes

[简体中文](README.zh-CN.md)

Write Markdown in OctoSense with the Rinx article writer, keep recoverable local
drafts, and review an exact GitHub commit before saving it. No separate OctoSense
cloud account is needed. Publisher: **ymote**. App ID:
`org.octosense.samples.githubnotes`, version `0.1.0`.

**macOS Apple Silicon preview.** Install [OctoSense desktop-v0.1.0-beta.2](https://github.com/OctoSense-org/OctoSense/releases/tag/desktop-v0.1.0-beta.2),
which includes the connected services and native Markdown editor. This app's
signed `0.1.0` bundle is available in the official App Hub catalog (first admission:
[sequence 7, App Hub #125](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/125)). Generic `card-host` cannot run this editor.
Live GitHub authorization and repository writes remain unverified.

## Use

1. In OctoSense, open **App Hub → Search**, search **GitHub Notes**, then choose
   **Get → Install → Open** after reviewing the requested permissions.
   This repository's signed `bundle/` is the same application artifact.
2. Write locally using Source, Split or Preview; narrow windows alternate Source
   and Preview. The palette also offers the rich block editor and undo/redo.
3. The back/file icon opens **Repository & file**. Connect GitHub through the host
   sheet and external browser. A host-configured GitHub OAuth client with device
   flow enabled is required; follow the [versioned host setup guide](https://github.com/OctoSense-org/OctoSense/blob/desktop-v0.1.0-beta.2/crates/oauth-service/README.md).
   Never put provider credentials in the bundle.
4. Choose the account, repository, branch and Markdown file. **Use as new path**
   selects a new destination. Public access requests `read:user` + `public_repo`;
   private access requests the broader `read:user` + `repo` scopes.
5. Set the commit message, return to the note, and use the paper-plane icon.
   Review the exact destination and Markdown in the host sheet before approving.
   A commit is reported only after GitHub returns a commit SHA.

Cancelled or failed saves retain the draft. Switching accounts does not silently
retarget an open note. Replacing a note keeps one previous recovery copy. If a
save has an uncertain network outcome, check GitHub before trying again; the app
does not automatically retry. Disconnecting retains local drafts and existing
GitHub commits. See [Privacy](PRIVACY.md).

## Verify a release

A publisher-signed release includes `publisher.json` and the signed check output
in `review/GATE.txt` / `review/GATE.json`, with release and question records in
`review/RELEASE.json` / `review/QUESTIONS.json`. Read the public key from
`publisher.json`, then verify the unchanged bundle:

```sh
HUB=hub # or the path to a compatible hub binary
APP_PUBLISHER_PUBLIC_KEY="$(python3 -c 'import json; print(json.load(open("publisher.json"))["public_key"])')"
"$HUB" check bundle --publisher-key "ymote=$APP_PUBLISHER_PUBLIC_KEY"
```

The command reads only the public key and does not modify the bundle. A publisher signature identifies its source; App Hub catalog
admission remains a separate maintainer decision.

## Test without a GitHub account

With this repository and a compatible OctoSense checkout as siblings, run from
the **OctoSense** directory on macOS:

```sh
cargo build --locked --release -p octosense-shell \
  --features mobile-apps,acceptance-fixtures \
  --example connected-app-host --example connected-install
python3 tools/connected-e2e/notes.py --bundle ../octosense-github-notes/bundle
```

The test signs a temporary copy, installs through the real Store, and exercises
the native editor, account gates and exact host review using a synthetic GitHub
transport and in-memory vault. It does not use your GitHub CLI login or write a
real repository. The fixture feature is disabled in ordinary builds and refuses
unmarked profiles. See the [pinned acceptance guide](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/tools/connected-e2e/README.md)
for manual fixture launch and evidence handling. These commands are reproduction
instructions; the repackaged listing has not been rerun through the native suite.

## Develop a new version

Use an unsigned development copy, not the published signed artifact. Build `hub`
from the App Hub revision required by the runtime, then check that copy:

```sh
hub stamp bundle
hub check bundle --allow-unsigned
mkdir -p build
hub scan bundle --packet build/review-packet.json
```

Stamping a signed artifact invalidates its signature. After changing a release,
the publisher must use a new version, stamp, re-sign with `hub sign-manifest`,
and run the publisher-key check above. `--allow-unsigned` does not trust an
unknown signature. Keys and review packets stay out of `bundle/`. [Review answers](review/ANSWERS.md) and [source provenance](review/PROVENANCE.json)
are separate from the app.

## Evidence and limits

The two listing images are unchanged original native captures with fictional
notes; they are not mockups. Historical [installed acceptance](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/github-notes/evidence/rinx-writer-installed/receipt.json)
and [visual review](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/github-notes/evidence/rinx-writer-installed/manual-review.json)
cover repository/file selection, Unicode editing, cancellation, synthetic
existing/new commits, conflicts, uncertain responses and offline restart.
The [writer soak](https://github.com/OctoSense-org/OctoSense/blob/26b9fe9fa51ef3c1fe6f833743144a2e12cf54e3/tools/connected-e2e/evidence/notes-rinx-soak-20261006/README.md)
records 36 cycles over ten minutes before the failed-load recovery guard and a
12-cycle regression afterward. These records retain their original source
hashes; this repository changes listing metadata and consequently the digest.
They are not new execution evidence for that new digest.

The editor has a 512 KiB document limit. Rinx Matrix publication, image upload and
remote image fetching are not included. This app has no in-app Chat, direct model
calls or Glance publication. OctoSense offers an optional, separately consented
**Ask GitHub Notes** agent because the bundle declares tools. If used, your
questions, conversation context and permitted tool results may be sent to the
host-configured model; see [Privacy](PRIVACY.md). This shell-agent path remains
unverified here. Its three private-data read aliases in [tools.json](bundle/tools.json)
are foreground-only and non-shareable; there is no exported write/approval tool.
Live GitHub, physical host approval, brokered tool execution and Windows/Linux UI
remain unverified. A separate OnePlus test does not establish an Android release
claim for this bundle; the listing declares **macos only**.

[Support](SUPPORT.md) · [Privacy](PRIVACY.md) · [Attribution](NOTICE) ·
[Apache-2.0](LICENSE)
