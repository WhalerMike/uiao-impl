# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | ✅        |

## Reporting a Vulnerability

If you discover a security vulnerability, please do not open a public GitHub issue.
Instead, please report it via GitHub's private vulnerability reporting feature:

[Report a Vulnerability](https://github.com/WhalerMike/uiao-impl/security/advisories/new)

You can expect an initial response within 72 hours and a resolution timeline within
14 days for critical issues.

## AI Agent Governance

This section defines the governance policy for AI coding agents operating in this repository.

### Permitted Actions

- Reading source files and consuming uiao-core canon at runtime via `--canon-path`.
- Creating or updating files in `src/`, `tests/`, `scripts/`, and `adapters/` as part of CI/CD.
- Opening pull requests that include only auto-generated artifacts or dependency updates.

### Prohibited Actions

- Committing secrets, credentials, API keys, or PII directly into any file.
- Modifying `pyproject.toml` dependencies without a human-reviewed pull request.
- Disabling or bypassing branch protection rules or required status checks.
- Exfiltrating repository contents to unapproved external endpoints.
- Self-modifying workflow files (`.github/workflows/`) without explicit human approval.
- Hardcoding `--canon-path` values pointing outside the standard uiao-core sibling layout.

### Human-in-the-Loop Requirements

The following changes always require a human reviewer:

- Changes to `pyproject.toml` (dependency surface).
- Changes to `.github/workflows/` (CI/CD pipeline).
- Changes to `SECURITY.md`, `CLAUDE.md`, or `README.md`.
- Any change that modifies GitHub Actions permissions or secrets.

## Compliance

This governance policy aligns with NIST SP 800-53 Rev 5 (SI-7, AU-2),
NIST SP 800-218 (SSDF), and CISA Secure-by-Design Principles.
