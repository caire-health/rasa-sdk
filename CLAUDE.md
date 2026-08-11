# caire-health/rasa-sdk fork

## Dependency changes — mandatory rule

**Whenever `pyproject.toml` is changed, always regenerate `poetry.lock` in the same commit:**

```bash
poetry lock
```

Never open a PR with a `pyproject.toml` change without the updated `poetry.lock`.

## Repo context

- This is a fork of `rasahq/rasa-sdk` (the action server framework — separate from the full rasa ML framework)
- Python `>3.10, <3.13`
- `caire-services/services/rasa-actions` depends on this repo via git source on `main` branch
- After merging any change here, run `poetry lock` in `caire-services/services/rasa-actions/` to pick up the new `resolved_reference`

## Version

- Keep `version` in `pyproject.toml` as a stable semver (e.g. `3.12.0`) — never leave it as a pre-release suffix like `.dev2`
- A pre-release version causes `poetry lock` in dependents to fail with `[BUG] rasa-sdk (x.y.z.devN) is not satisfied`
