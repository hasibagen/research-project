# Changelog

All notable changes to **research-project** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project adheres
to [Semantic Versioning](https://semver.org/).

## [1.0.0] · 2026-10-21

### Added
- **The skill itself** — a two-layer skill for LLM coding agents that keeps a
  research project's plans, code, data, results and delivery material in a fixed,
  self-describing, checkable shape:
  - **action layer** — 7 modules, one per job (`organize` · `project` · `plan` ·
    `code` · `run` · `interpret` · `release`)
  - **structure layer** — 6 areas, one per kind of object (`project` ·
    `documents` · `code` · `data` · `results` · `delivery`)
- **21 templates and schemas** (`assets/templates/`), including a project
  scaffold (`AGENTS.md` · `README.md` · `docs-readme.md` · `gitignore`).
- **A synthetic end-to-end demo** (`assets/demo/`) — Snakemake → provenance
  records → de-duplicated import → RO-Crate export → `roc-validator`
  validation → question-page back-fill — plus a fault drill that kills a real
  subprocess mid-import and recovers.
- **Four helper scripts** — a 5 MB file gate for Git/jj (`check_repo_files.py`),
  a read-only plan/dependency/evidence checker (`check_plans.py`), a project
  scaffold generator (`create_project_template.py`) and a run-record adapter
  (`research_records.py`).
- **41 tests** covering the templates, the record contract and the plan checker.
- **Bilingual documentation** — `README.md` (English) and `README.zh.md` (中文),
  both with mermaid architecture diagrams, the authoritative directory trees and
  a scope table.
- **CI** (GitHub Actions): the template and contract test suite on Python
  3.10 / 3.12.

### Notes
- This is a **fully de-identified public release**. Every project, plan, config
  and script name, absolute path, session id and run identifier is replaced with
  a synthetic placeholder; the numbers, counts and metrics in the worked examples
  are illustrative rather than measurements; and the private archives and
  snapshots are excluded. The rules, the templates, the scripts and the tests are
  complete and unmodified in substance.
- `rocrate` is an optional dependency: the RO-Crate export tests skip themselves
  when it is not installed. CI installs it so the export path is exercised.
