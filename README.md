# GitHub Notes

[简体中文](README.zh-CN.md)

Write Markdown with the native Rinx article editor in OctoSense, retain local
drafts across restart, and review an exact GitHub commit before saving.
Publisher: **ymote**. New app ID: `io.github.ymote.githubnotes`, version `0.2.1`.

This is a **macOS development preview candidate**. It requires a compatible
OctoSense host with contract 1.8.0 / `publisher-github-v1` support and the native
Markdown editor. `desktop-v0.1.0-beta.2` cannot install this keyless release;
generic `card-host` cannot render its editor. Version 0.2.0 passed real signed installation, editing and restart in the
compatible packaged host at `5e1a8414`; the official compatible release remains pending. Live GitHub authorization and remote commits are unverified.

## Install and use

Publication is requested through an issue on
[OctoSense App Hub](https://github.com/OctoSense-org/OctoSense-App-Hub/issues).
A GitHub tag produces verifiable release assets; it does **not** automatically
submit or admit the app. Until administrators publish this new ID in the
catalog, it is not available through the official App Hub search.

After admission, use **App Hub → Search → GitHub Notes → Get → Install → Open**
in a compatible host. Review the app ID and permissions before installing.

1. Write locally in Source, Split or Preview. Narrow windows switch Source and
   Preview; the palette offers the rich block editor and undo/redo.
2. The file icon opens **Repository & file**. Connect GitHub through the host
   sheet and external browser. The host operator must configure a GitHub OAuth
   client with device flow enabled; no token or secret belongs in this bundle.
3. Select an account, repository, branch and Markdown file. **Use as new path**
   chooses a new destination. Public access requests `read:user` + `public_repo`;
   private access requests broader `read:user` + `repo` scopes.
4. Set a commit message and use the paper-plane icon. Review the exact target
   and Markdown in the host sheet. Only a returned commit SHA counts as saved.

Cancelled or failed saves retain the draft. Account switches never silently
retarget a note. Replacing a note keeps one recovery copy. An uncertain network
response needs checking on GitHub before another approved attempt.

## GitHub-managed publishing

No separate developer signing key or repository signing secret is required.
The reviewed [tag workflow](.github/workflows/publish-app.yml) prepares the
canonical manifest, obtains a GitHub Actions attestation, verifies it, and
publishes `app.bundle.pack.json`, `octosense-app-manifest.json` and
`release-receipt.json`. Each update needs a new version and immutable tag.

Verify downloaded assets with a compatible Hub CLI:

```sh
hub publisher-unpack app.bundle.pack.json --out verified-bundle
hub publisher-verify verified-bundle
```

Never stamp the verified bundle. For editable source only:

```sh
hub stamp bundle
hub check bundle --allow-unsigned
mkdir -p build
hub scan bundle --packet build/review-packet.json
python3 -m unittest discover -s tests -v
```

Open or update the [submission issue](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/158) with the successful workflow, release, screenshots and
[review answers](review/0.2.0/ANSWERS.md) to the submission issue. Hub review and
administrator catalog approval are separate from GitHub artifact publication.

## Evidence and limits

The editor, three private read aliases and account/review logic are retained
from the earlier app. New source/native evidence is recorded under
[review/0.2.0](review/0.2.0/README.md). Original screenshots contain only fictional
notes. Preliminary editor checks do not prove current-shell signed installation,
live OAuth, remote writes, physical approval or model execution.

The optional **Ask GitHub Notes** agent needs separate consent and may send
questions, conversation context and permitted repository reads to the
host-configured model. It is foreground-only, read-only and non-shareable.
It cannot edit the draft, approve or commit. There is no in-app chat, direct
model call, Glance publication, Matrix publication or image upload. Documents
are limited to 512 KiB. Only macOS is listed; other platforms remain unverified.
See [Privacy](PRIVACY.md), [Support](SUPPORT.md) and [Attribution](NOTICE).

## Historical app

The old `org.octosense.samples.githubnotes` 0.1.0/0.1.1 releases, signatures,
`publisher.json` and dated `review/` records remain historical and unchanged.
They are not the identity or verification evidence for this fresh app. There
is no automatic transfer of drafts, account handles or publisher ownership.
Old App Hub [#121](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/121)
and [#131](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/131) describe
those old releases, not this submission.
