# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-04-20
### Added
- Initial release of `dictionary-parser`.
- CLI interface using Typer.
- Accepts local files or URL for input.
- Filters words by starting letter(s) or range (e.g., `a`, `a-c`, `a,f,g`).
- Exports to JSON or CSV.
- Supports output into multiple files or a single file.
- Global index, per-letter index, and length metadata.
- Word case transformation: lower, upper, or no change.
- Automated tests with Pytest.
- CI pipeline using GitHub Actions.

## [0.2.0] - 2025-04-21
### Added
- Updated documentation to reflect changes in Github Actions, Badges, etc.
- Added missing __main__ file
- Switch to Poetry Core for build system

## [0.2.1] - 2025-04-21
- Updated README to match latest release version

## [0.3.0] - 2025-04-23
### Added
- Added support for sorting words in the output files.
- Added support for adding metadata to the output files.
---

