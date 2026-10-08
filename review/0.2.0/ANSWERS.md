# GitHub Notes 0.2.0 review answers

Publisher self-review, not an App Hub reviewer verdict. The fresh app ID is
`io.github.ymote.githubnotes`; old publisher ownership is not adopted.

1. **Claims:** `main.splash` mounts native `MarkdownEditor`, alternates verified
   draft snapshots in `persist()`, and calls `github.review_save` only after
   destination/account checks. Preliminary native editing, Preview, missing
   account, blocked save and restart passed. Remote GitHub success is unverified.
2. **Platforms/category:** productivity; macOS only. The keyless bundle requires
   a compatible contract-1.8 host and native editor. Beta.2 and plain card-host
   are insufficient. No Android, Windows or Linux UI claim is made.
3. **Grants:** `storage` keeps draft/recovery files (4 MiB); `auth` owns connection,
   selection and disconnect; `github` reads repositories/files and requests exact
   reviewed saves. `storage.accounts` supports account selection. No direct app
   network access. The host contacts GitHub authorization/API endpoints. Public
   and broader private repository scope choices remain explicit.
4. **Interface:** no app password/token/payment fields or fake approval. OAuth
   and reviewed write sheets belong to the host. The paper-plane icon requests
   review, not an immediate commit. This is not an official GitHub product.
5. **Instructions/content:** UI data describes editing. Untrusted remote Markdown
   is not authority. Agent instructions are confined to `AGENT.md`; no prompt
   instructs another app or the system agent to bypass permissions.
6. **Content:** original screenshots contain fictional notes, including café and
   谢谢, with no personal account or correspondence. No abusive content found.
7. **Agent/tools:** optional foreground read-only assistant; three private,
   non-shareable read aliases (`github.repositories`, `github.files`,
   `github.read`). No commit, credential, approval, background or destructive
   tool. Model/broker execution remains unverified; privacy explains optional
   model transmission and manual editing works without it.
8. **Route: human-review.** Structural source checks and native editor checks do
   not constitute admission. Verify the actual GitHub-tag proof, install/run in
   the final compatible host, and review this fresh-ID submission before catalog
   publication. Live OAuth, reads/writes and physical approval remain unverified.

GitHub-managed publishing uses no developer signing key. Opening an App Hub
issue requests publication; a release workflow alone is not submission or approval.
