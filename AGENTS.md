# GitHub Notes maintenance

This repository contains one contained App Hub app. Only `bundle/` is shipped.
Read README.md, PRIVACY.md and review/ANSWERS.md before changing its permissions
or publishing claims. Keep English and Chinese user documentation aligned.

- Preserve app ID `org.octosense.samples.githubnotes`; released versions are immutable.
- Use the matching OctoSense connected-services host. Generic card-host lacks MarkdownEditor.
- Keep OAuth tokens and provider configuration in the host; never add secret fields to the app.
- GitHub writes require the exact host review; never substitute a script approval bypass.
- Changes to any bundle file require stamping and a new publisher signature for release.
- Use isolated synthetic profiles for tests; do not use a developer's GitHub/Matrix profile.
- Do not claim live OAuth, remote commits, physical approval or untested platforms from fixtures.
- Keep keys, local state, raw logs and scan packets outside bundle and Git.
- Preserve source-bound historical evidence; new bytes need new execution evidence.
- Follow App Hub's publishing instructions. Catalog/index/artifacts are maintainer-owned.

Existing user authorization applies to publication; keys and final release actions
belong to the designated publisher. Documentation and tests do not constitute
App Hub admission or a reviewer verdict.
