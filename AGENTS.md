# GitHub Notes maintenance

This repository contains one contained App Hub app. Only `bundle/` is shipped.
Read README.md, PRIVACY.md and review/ANSWERS.md before changing its permissions
or publishing claims. Keep English and Chinese user documentation aligned.

- Use app ID `io.github.ymote.githubnotes` for 0.2.x; released versions are immutable.
  Historical `org.octosense.samples.githubnotes` releases remain separate; never overwrite or silently migrate them.
- Use the matching OctoSense connected-services host. Generic card-host lacks MarkdownEditor.
- Keep OAuth tokens and provider configuration in the host; never add secret fields to the app.
- GitHub writes require the exact host review; never substitute a script approval bypass.
- Changes to any editable bundle file require stamping and a new version/tag. The generated GitHub workflow attests and packs it; never restamp sealed release artifacts. No developer signing key is required.
- Use isolated synthetic profiles for tests; do not use a developer's GitHub/Matrix profile.
- Do not claim live OAuth, remote commits, physical approval or untested platforms from fixtures.
- Keep keys, local state, raw logs and scan packets outside bundle and Git.
- Preserve source-bound historical evidence; new bytes need new execution evidence.
- Follow App Hub's publishing instructions. Catalog/index/artifacts are maintainer-owned.

Existing user authorization applies to publication and submission. The tag workflow uses
GitHub-managed identity; an App Hub issue requests publication and an administrator separately approves admission. Documentation and tests do not constitute
App Hub admission or a reviewer verdict.
