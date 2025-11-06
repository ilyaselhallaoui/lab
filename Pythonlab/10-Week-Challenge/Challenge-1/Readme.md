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
