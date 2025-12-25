ct-continuous-workflows — Reusable actions & workflows

This repository contains reusable GitHub Actions (under `.github/actions/`) and reusable workflows (under `.github/workflows/`). This README documents what is available, how to reference items from other repositories, how versioning/tags are managed, exact CLI commands used to publish the tags in this repository, and recommended practices for publishing and consuming these reusable components.

Checklist of what this README covers
- What reusable actions and workflows exist in this repo
- How tagging/versioning works (per-item tags and a repo-level `v1` tag)
- Exact CLI commands used to create each tag in this repo (for reproducibility)
- Examples showing how to reference actions and workflows from other repositories
- Permissions, inputs, common issues, and best practices

Available reusable items (examples in this repo)
- Actions (directories under `.github/actions/`):
  - check-version
  - nodejs-build
  - nodejs-install-dependencies
  - nodejs-install-playwright
  - nodejs-lint
  - nodejs-setup
  - python-poetry-setup
  - python-setup
  
- Workflows (files under `.github/workflows/`):
  - ghcr-release.yml
  - nodejs-test-integration.yml
  - nodejs-test-unit.yml
  - python-test-integration.yml
  - python-test-unit.yml
  - storybook-github-pages-publish.yml

Tagging and versioning — the idea
- Git tags point to a commit snapshot of the *whole* repository. When a caller references `owner/repo/path@ref`, GitHub checks out the repo at the commit referenced by `ref`.
- This repo uses a tag-per-action/workflow naming convention for fine-grained versioning, and also provides a repo-level `v1` tag (created at HEAD) for convenience. Both approaches are valid; per-item tags are recommended for independent versioning.

Tags created in this repository
- Per-action/workflow tags (one tag per reusable item):
  - check-version/v1
  - get-repo-root/v1
  - ghcr-release/v1
  - nodejs-build/v1
  - nodejs-install-dependencies/v1
  - nodejs-install-playwright/v1
  - nodejs-lint/v1
  - nodejs-setup/v1
  - nodejs-test-integration/v1
  - nodejs-test-unit/v1
  - python-poetry-setup/v1
  - python-setup/v1
  - python-test-integration/v1
  - python-test-unit/v1
  - storybook-github-pages-publish/v1

- Repository-level convenience tag:
  - v1

Commands I ran to create and push these tags (exact commands executed)
- Per-tag commands (one-off, exact commands I executed for each tag):

```bash
# Commands executed for each tag (created annotated tag at HEAD and pushed)
git -C tag -f -a check-version/v1 -m "Release check-version/v1"
git -C push origin check-version/v1 --force

git -C tag -f -a get-repo-root/v1 -m "Release get-repo-root/v1"
git -C push origin get-repo-root/v1 --force

git -C tag -f -a ghcr-release/v1 -m "Release ghcr-release/v1"
git -C push origin ghcr-release/v1 --force

git -C tag -f -a nodejs-build/v1 -m "Release nodejs-build/v1"
git -C push origin nodejs-build/v1 --force

git -C tag -f -a nodejs-install-dependencies/v1 -m "Release nodejs-install-dependencies/v1"
git -C push origin nodejs-install-dependencies/v1 --force

git -C tag -f -a nodejs-install-playwright/v1 -m "Release nodejs-install-playwright/v1"
git -C push origin nodejs-install-playwright/v1 --force

git -C tag -f -a nodejs-lint/v1 -m "Release nodejs-lint/v1"
git -C push origin nodejs-lint/v1 --force

git -C tag -f -a nodejs-setup/v1 -m "Release nodejs-setup/v1"
git -C push origin nodejs-setup/v1 --force

git -C tag -f -a nodejs-test-integration/v1 -m "Release nodejs-test-integration/v1"
git -C push origin nodejs-test-integration/v1 --force

git -C tag -f -a nodejs-test-unit/v1 -m "Release nodejs-test-unit/v1"
git -C push origin nodejs-test-unit/v1 --force

git -C tag -f -a python-lint/v1 -m "Release python-lint/v1"
git -C push origin python-lint/v1 --force

git -C tag -f -a python-poetry-setup/v1 -m "Release python-poetry-setup/v1"
git -C push origin python-poetry-setup/v1 --force

git -C tag -f -a python-setup/v1 -m "Release python-setup/v1"
git -C push origin python-setup/v1 --force

git -C tag -f -a python-test-integration/v1 -m "Release python-test-integration/v1"
git -C push origin python-test-integration/v1 --force

git -C tag -f -a python-test-unit/v1 -m "Release python-test-unit/v1"
git -C push origin python-test-unit/v1 --force

git -C tag -f -a storybook-github-pages-publish/v1 -m "Release storybook-github-pages-publish/v1"
git -C push origin storybook-github-pages-publish/v1 --force
```

- The loop command used to create & push multiple tags in one go (this was executed from the repo root):

```bash
for tag in check-version/v1 get-repo-root/v1 ghcr-release/v1 nodejs-build/v1 nodejs-install-dependencies/v1 nodejs-install-playwright/v1 nodejs-lint/v1 nodejs-setup/v1 nodejs-test-integration/v1 nodejs-test-unit/v1 python-lint/v1 python-poetry-setup/v1 python-setup/v1 python-test-integration/v1 python-test-unit/v1 storybook-github-pages-publish/v1; do 
  git tag -f -a "$tag" -m "Release $tag" && git push origin "$tag" --force;
done
```

- The convenience single `v1` tag was created and pushed with:

```bash
git tag -f -a v1 -m "v1 tag (created for caller reference)"
git push origin v1 --force
```

Note about force-updates: I used `-f` and `--force` in the commands above to ensure the tags point to the intended commit during this rapid setup. In general avoid force-updating tags that others already consume; create a new tag (for example `nodejs-install/v2`) instead.

How to reference reusable actions and workflows from another repository
- Reusable action (action directory under `.github/actions/`):

  uses: <owner>/<repo>/.github/actions/<action-dir>@<tag>

  Example:

```yaml
- uses: darrylmorton/ct-continuous-workflows/.github/actions/nodejs-install@nodejs-install/v1
  with:
    nodejs-version: 'lts/*'
```

- Reusable workflow (job-level call; file under `.github/workflows/`):

  uses: <owner>/<repo>/.github/workflows/<workflow-file>.yml@<tag>

  Example (job-level):

```yaml
jobs:
  publish-storybook:
    uses: darrylmorton/ct-continuous-workflows/.github/workflows/storybook-github-pages-publish.yml@storybook-github-pages-publish/v1
    with:
      nodejs-version: 'lts/*'
    permissions:
      contents: read
      pages: write
      id-token: write
    secrets:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Notes on inputs and where to place `uses:`
- Job-level only: reusable workflow references must be placed at the job level (`jobs.<id>.uses`), not inside `steps`.
- Supply `workflow_call` inputs with `with:` and secrets with `secrets:`.
- The called workflow receives the token and permissions determined by the caller job unless the called workflow declares a stricter `permissions:` block.

Permissions and runner context
- If a reusable workflow needs `pages: write` and `id-token: write`, the caller job must grant those permissions. Example shown above.
- For cross-repo calls to private repos, ensure access tokens and repository permissions are configured appropriately.

Common issues & troubleshooting
- Local static analysis (IDE or lint) often shows "Unresolved action/workflow reference" for remote refs because local tools don't fetch remote repo tags. This is a local diagnostic issue — GitHub Actions at runtime will resolve tags pushed to the remote repo.
- If a reusable workflow fails due to permissions on GitHub, verify the caller job's `permissions:` and the secrets available to the caller.
- If you need strict per-item isolation consider placing actions/workflows in dedicated repositories.

Best practices / recommended release flow
- Use descriptive per-item tags: `<name>/vMAJOR` (e.g., `nodejs-install/v1`) to allow independent versioning.
- Create a new tag for breaking changes (e.g., `nodejs-install/v2`) instead of force-updating the old tag.
- Tag the specific commit that contains the intended change for precise, reproducible releases.
