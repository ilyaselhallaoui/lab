# 10 Week Challenge — Python for DevOps
_Repository path: `pythonlab/10-week-challenge/README.md`_

**How this works**
- You’ll build 10 tiny, real-world tools — each adds one new DevOps skill.
- We provide **what** to build and **how we’ll check it works**.  
- **No AI-written solutions.** AI may be used only for feedback, edge cases, and concept explanations.

- My Start-Date: 20.10.2025
- My End-Date 31.12.2025

---

## Challenge 1 — Text Utilities (Foundations)
**What you’ll build**  
A small toolkit that reads text files **as a stream** and reports counts or transforms lines.

**Why it matters**  
Ops tools must handle large files without loading everything into memory.

**Deliverables**  
- `wc-lite FILE` → print **lines words bytes** (like `wc`, streaming).  
- `contains FILE NEEDLE [-i]` → exit `0` if found, `1` if not.  
- `normalize FILE --to lf|crlf` → write a **new** normalized file.

**We’ll verify**  
- Works on empty files and files **without** trailing newline.  
- Memory stays flat on big files (no full read).  
- Exit codes: `0` success, `1` “not found” (for `contains`), `2` usage errors.  
- `--help` explains each command and examples.

---

## Challenge 2 — LogTools (Head / Grep / Tail)
**What you’ll build**  
A CLI with three subcommands: `head`, `grep`, `tail` — all streaming.

**Why it matters**  
These are the core patterns for reading, filtering, and sampling logs.

**Deliverables**  
- `head FILE -n N`  
- `grep FILE NEEDLE [-i] [--count]`  
- `tail FILE -n N` (must use **O(N) memory**, not full file)

**We’ll verify**  
- `tail -n 0` prints nothing; `tail` with big `N` prints whole file.  
- `grep --count` prints **only** an integer; `-i` does case-insensitive search.  
- Nonexistent file → clear message on **stderr** + exit `2`.  
- Every output line ends with exactly **one** newline.

---

## Challenge 3 — Proc-Run (Run Commands Safely)
**What you’ll build**  
A wrapper to execute system commands with timeouts and machine-readable output.

**Why it matters**  
DevOps automation must safely call CLIs and propagate correct statuses.

**Deliverables**  
- `proc-run CMD...` with:  
  - `--timeout S` (kill on timeout)  
  - `--json` → print `{cmd, returncode, duration_ms, stdout_tail}`

**We’ll verify**  
- Streams stdout/stderr live; returns the **child’s** exit code.  
- Timeout terminates the process and exits with `124`.  
- Handles large, long-running output without hanging.

---

## Challenge 4 — HTTP Client (Resilient GitHub Releases)
**What you’ll build**  
A client that lists GitHub releases robustly (timeouts, retries, pagination).

**Why it matters**  
Real APIs throttle, paginate, and fail transiently; your tools must recover.

**Deliverables**  
- `gh-releases owner/repo [--since ISO8601] [--json]`  
- Per-request **timeout**; **retry** with exponential backoff + jitter.  
- Parse `Link` headers for **pagination**.

**We’ll verify**  
- `--since` filters correctly by published date.  
- Human-friendly table by default; structured JSON with `--json`.  
- Clear message on throttle (429/403) before retrying.

---

## Challenge 5 — SQLite Artifact Index
**What you’ll build**  
Persist release + asset metadata locally and export it.

**Why it matters**  
Ops tasks need local state that is **idempotent** across runs.

**Deliverables**  
- `artifact-index` that uses Challenge 4 client to **upsert** into SQLite.  
- `export --csv PATH` and `--ndjson PATH`.  
- Store a schema version; refuse to run if DB is corrupt or mismatched.

**We’ll verify**  
- Re-running doesn’t duplicate rows.  
- Export row counts match DB.  
- Errors are clear and actionable (bad path, corrupt DB, etc.).

---

## Challenge 6 — Async Multi-Fetch (When to use asyncio)
**What you’ll build**  
A concurrent fetcher for many URLs with controlled parallelism.

**Why it matters**  
I/O-bound tasks speed up with async, but must respect limits and cancellation.

**Deliverables**  
- `multi-fetch urls.txt --concurrency N --timeout S [--ndjson]`  
- Output one NDJSON per URL: `{url, status, bytes, ms}`  
- Graceful Ctrl+C: cancel tasks, close clients, print summary.

**We’ll verify**  
- Works with 200+ URLs and stable memory.  
- Respects semaphore limit and per-request timeout.  
- No zombie tasks after cancellation.

---

## Challenge 7 — Docker Image Pruner (Safe by Default)
**What you’ll build**  
A tool to identify and optionally delete stale Docker images.

**Why it matters**  
Cleaning up safely saves disk space without breaking deployments.

**Deliverables**  
- `image-pruner [--older-than DAYS] [--filter PREFIX] [--yes]`  
- Lists candidates; **dry-run by default**; requires `--yes` to delete.  
- Shows estimated space reclaimed.

**We’ll verify**  
- Never deletes without `--yes`.  
- Clear messages on permission/daemon errors.  
- Output shows why each image was kept or deleted.

---

## Challenge 8 — K8s Toolbox (Read-Only via API)
**What you’ll build**  
Read-only Kubernetes helpers: list pods, tail logs, stream events.

**Why it matters**  
Operating clusters through the API (not only kubectl) unlocks automation.

**Deliverables**  
- `k8s-toolbox pods -n NS [-l selector]` → name, phase, age, restarts  
- `k8s-toolbox logs -n NS POD [-c CONTAINER] [--tail N] [--follow]`  
- `k8s-toolbox events -n NS [--since DURATION]`  

**We’ll verify**  
- Works with kubeconfig discovery; helpful error on auth/RBAC issues.  
- `--follow` tails and cancels cleanly.  
- Output is readable and includes key fields (phase, age, restarts).

---

## Challenge 9 — Observability Add-On (Logs & Metrics)
**What you’ll build**  
Add structured logging and optional Prometheus metrics to any prior tool.

**Why it matters**  
If you can’t observe it, you can’t operate it.

**Deliverables**  
- JSON logs per action: `{ts, level, tool, action, target, duration_ms, ok, request_id}`  
- Optional tiny HTTP server variant to expose Prometheus metrics.

**We’ll verify**  
- Logs are valid JSON and include correlation IDs.  
- Metrics counters/histograms increase after operations and can be scraped locally.

---

## Challenge 10 — Capstone: Release Mirror (End-to-End)
**What you’ll build**  
A cohesive tool that discovers release assets, syncs them locally, and keeps a manifest.

**Why it matters**  
Combines API calls, persistence, concurrency, idempotency, and packaging.

**Deliverables**  
- `release-mirror owner/repo --dest DIR [--since ISO] [--concurrency N] [--dry-run] [--json]`  
- Decide what’s missing, download with retries/timeouts, update manifest (SQLite).  
- Provide entry point packaging and a Dockerfile.

**We’ll verify**  
- Summary report: downloaded, skipped, failed, bytes, duration.  
- Re-run is idempotent (skips up-to-date).  
- Non-zero exit if any download failed.  
- Clear README with usage, assumptions, and limits.

---
# 10 Week Challenge — Python for DevOps
_Repository path: `pythonlab/10-week-challenge/README.md`_

**How this works**
- You’ll build 10 tiny, real-world tools — each adds one new DevOps skill.
- We provide **what** to build and **how we’ll check it works**.  
- **No AI-written solutions.** AI may be used only for feedback, edge cases, and concept explanations.

---

## Challenge 1 — Text Utilities (Foundations)
**What you’ll build**  
A small toolkit that reads text files **as a stream** and reports counts or transforms lines.

**Why it matters**  
Ops tools must handle large files without loading everything into memory.

**Deliverables**  
- `wc-lite FILE` → print **lines words bytes** (like `wc`, streaming).  
- `contains FILE NEEDLE [-i]` → exit `0` if found, `1` if not.  
- `normalize FILE --to lf|crlf` → write a **new** normalized file.

**We’ll verify**  
- Works on empty files and files **without** trailing newline.  
- Memory stays flat on big files (no full read).  
- Exit codes: `0` success, `1` “not found” (for `contains`), `2` usage errors.  
- `--help` explains each command and examples.

---

## Challenge 2 — LogTools (Head / Grep / Tail)
**What you’ll build**  
A CLI with three subcommands: `head`, `grep`, `tail` — all streaming.

**Why it matters**  
These are the core patterns for reading, filtering, and sampling logs.

**Deliverables**  
- `head FILE -n N`  
- `grep FILE NEEDLE [-i] [--count]`  
- `tail FILE -n N` (must use **O(N) memory**, not full file)

**We’ll verify**  
- `tail -n 0` prints nothing; `tail` with big `N` prints whole file.  
- `grep --count` prints **only** an integer; `-i` does case-insensitive search.  
- Nonexistent file → clear message on **stderr** + exit `2`.  
- Every output line ends with exactly **one** newline.

---

## Challenge 3 — Proc-Run (Run Commands Safely)
**What you’ll build**  
A wrapper to execute system commands with timeouts and machine-readable output.

**Why it matters**  
DevOps automation must safely call CLIs and propagate correct statuses.

**Deliverables**  
- `proc-run CMD...` with:  
  - `--timeout S` (kill on timeout)  
  - `--json` → print `{cmd, returncode, duration_ms, stdout_tail}`

**We’ll verify**  
- Streams stdout/stderr live; returns the **child’s** exit code.  
- Timeout terminates the process and exits with `124`.  
- Handles large, long-running output without hanging.

---

## Challenge 4 — HTTP Client (Resilient GitHub Releases)
**What you’ll build**  
A client that lists GitHub releases robustly (timeouts, retries, pagination).

**Why it matters**  
Real APIs throttle, paginate, and fail transiently; your tools must recover.

**Deliverables**  
- `gh-releases owner/repo [--since ISO8601] [--json]`  
- Per-request **timeout**; **retry** with exponential backoff + jitter.  
- Parse `Link` headers for **pagination**.

**We’ll verify**  
- `--since` filters correctly by published date.  
- Human-friendly table by default; structured JSON with `--json`.  
- Clear message on throttle (429/403) before retrying.

---

## Challenge 5 — SQLite Artifact Index
**What you’ll build**  
Persist release + asset metadata locally and export it.

**Why it matters**  
Ops tasks need local state that is **idempotent** across runs.

**Deliverables**  
- `artifact-index` that uses Challenge 4 client to **upsert** into SQLite.  
- `export --csv PATH` and `--ndjson PATH`.  
- Store a schema version; refuse to run if DB is corrupt or mismatched.

**We’ll verify**  
- Re-running doesn’t duplicate rows.  
- Export row counts match DB.  
- Errors are clear and actionable (bad path, corrupt DB, etc.).

---

## Challenge 6 — Async Multi-Fetch (When to use asyncio)
**What you’ll build**  
A concurrent fetcher for many URLs with controlled parallelism.

**Why it matters**  
I/O-bound tasks speed up with async, but must respect limits and cancellation.

**Deliverables**  
- `multi-fetch urls.txt --concurrency N --timeout S [--ndjson]`  
- Output one NDJSON per URL: `{url, status, bytes, ms}`  
- Graceful Ctrl+C: cancel tasks, close clients, print summary.

**We’ll verify**  
- Works with 200+ URLs and stable memory.  
- Respects semaphore limit and per-request timeout.  
- No zombie tasks after cancellation.

---

## Challenge 7 — Docker Image Pruner (Safe by Default)
**What you’ll build**  
A tool to identify and optionally delete stale Docker images.

**Why it matters**  
Cleaning up safely saves disk space without breaking deployments.

**Deliverables**  
- `image-pruner [--older-than DAYS] [--filter PREFIX] [--yes]`  
- Lists candidates; **dry-run by default**; requires `--yes` to delete.  
- Shows estimated space reclaimed.

**We’ll verify**  
- Never deletes without `--yes`.  
- Clear messages on permission/daemon errors.  
- Output shows why each image was kept or deleted.

---

## Challenge 8 — K8s Toolbox (Read-Only via API)
**What you’ll build**  
Read-only Kubernetes helpers: list pods, tail logs, stream events.

**Why it matters**  
Operating clusters through the API (not only kubectl) unlocks automation.

**Deliverables**  
- `k8s-toolbox pods -n NS [-l selector]` → name, phase, age, restarts  
- `k8s-toolbox logs -n NS POD [-c CONTAINER] [--tail N] [--follow]`  
- `k8s-toolbox events -n NS [--since DURATION]`  

**We’ll verify**  
- Works with kubeconfig discovery; helpful error on auth/RBAC issues.  
- `--follow` tails and cancels cleanly.  
- Output is readable and includes key fields (phase, age, restarts).

---

## Challenge 9 — Observability Add-On (Logs & Metrics)
**What you’ll build**  
Add structured logging and optional Prometheus metrics to any prior tool.

**Why it matters**  
If you can’t observe it, you can’t operate it.

**Deliverables**  
- JSON logs per action: `{ts, level, tool, action, target, duration_ms, ok, request_id}`  
- Optional tiny HTTP server variant to expose Prometheus metrics.

**We’ll verify**  
- Logs are valid JSON and include correlation IDs.  
- Metrics counters/histograms increase after operations and can be scraped locally.

---

## Challenge 10 — Capstone: Release Mirror (End-to-End)
**What you’ll build**  
A cohesive tool that discovers release assets, syncs them locally, and keeps a manifest.

**Why it matters**  
Combines API calls, persistence, concurrency, idempotency, and packaging.

**Deliverables**  
- `release-mirror owner/repo --dest DIR [--since ISO] [--concurrency N] [--dry-run] [--json]`  
- Decide what’s missing, download with retries/timeouts, update manifest (SQLite).  
- Provide entry point packaging and a Dockerfile.

**We’ll verify**  
- Summary report: downloaded, skipped, failed, bytes, duration.  
- Re-run is idempotent (skips up-to-date).  
- Non-zero exit if any download failed.  
- Clear README with usage, assumptions, and limits.

---

## Quality Bar (applies to every challenge)
- Use a virtual environment and a minimal `pyproject.toml` (ruff, black, mypy).  
- Write **at least one failing test** before coding; keep tests green.  
- Helpful `--help`, clear errors, correct exit codes.  
- **Dry-run** for destructive operations; require confirmation flags to proceed.

---

## How to use AI (and how not)
- ✅ Ask for: spec reviews, edge cases, test ideas, concept clarifications, design feedback.  
- ❌ Don’t ask for: full implementations or copy-paste solutions.


## Quality Bar (applies to every challenge)
- Use a virtual environment and a minimal `pyproject.toml` (ruff, black, mypy).  
- Write **at least one failing test** before coding; keep tests green.  
- Helpful `--help`, clear errors, correct exit codes.  
- **Dry-run** for destructive operations; require confirmation flags to proceed.

---

## How to use AI (and how not)
- ✅ Ask for: spec reviews, edge cases, test ideas, concept clarifications, design feedback.  
- ❌ Don’t ask for: full implementations or copy-paste solutions.


