# uiao-impl — moved to WhalerMike/uiao

> **This repository has moved.** All `uiao-impl` content now lives under
> [`impl/`](https://github.com/WhalerMike/uiao/tree/main/impl) in the
> consolidated monorepo [`WhalerMike/uiao`](https://github.com/WhalerMike/uiao).
>
> The move happened on 2026-04-17. Full history was preserved via
> `git subtree`. No content was lost — only the URL changed.

## Where to go

| Old location | New location |
|---|---|
| `uiao-impl/` repo root | [`uiao/impl/`](https://github.com/WhalerMike/uiao/tree/main/impl) |
| `uiao-impl/src/uiao_impl/` | [`uiao/impl/src/uiao_impl/`](https://github.com/WhalerMike/uiao/tree/main/impl/src/uiao_impl) |
| `uiao-impl/tests/` | [`uiao/impl/tests/`](https://github.com/WhalerMike/uiao/tree/main/impl/tests) |
| `uiao-impl/scripts/` | [`uiao/impl/scripts/`](https://github.com/WhalerMike/uiao/tree/main/impl/scripts) |
| `uiao-impl/pyproject.toml` | [`uiao/impl/pyproject.toml`](https://github.com/WhalerMike/uiao/blob/main/impl/pyproject.toml) |
| Releases (`v0.2.1`+, signed, SBOM-attached) | [`uiao/releases`](https://github.com/WhalerMike/uiao/releases) |
| Issue tracker | [`uiao/issues`](https://github.com/WhalerMike/uiao/issues) |

## Install (from the monorepo)

```bash
pip install git+https://github.com/WhalerMike/uiao.git@v0.2.1#subdirectory=impl
```

## CLI

```bash
uiao --help
uiao substrate walk
uiao substrate drift
```

## Why consolidated

Four repositories (`uiao-core`, `uiao-docs`, `uiao-gos`, `uiao-impl`)
were merged into a single governance substrate with schema-anchored
canon, drift detection, and unified CI. See
**[ADR-028](https://github.com/WhalerMike/uiao/blob/main/core/canon/adr/adr-028-monorepo-consolidation-gos-integration.md)**
in the new repo for the authoritative rationale.

## This repo is now read-only

No new commits will land here. File issues and open PRs against
[`WhalerMike/uiao`](https://github.com/WhalerMike/uiao).
