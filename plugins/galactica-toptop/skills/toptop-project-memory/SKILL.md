---
name: toptop-project-memory
description: Maintain working context for a TOPTOP task through daughter GALACTICA; use when starting, resuming, or handing off project work.
---

# Project memory for TOPTOP

Call `galactica_toptop_client.whoami` and `get_context` for the current project path. Use `search_knowledge` for the specific question, then open the relevant canonical rows and source references. Keep the returned task ID and cite canonical IDs in working notes when they affect a decision.

The daughter PostgreSQL is the source of truth; Markdown is its journaled working projection. Qdrant and Neo4j are search/navigation indexes. Do not infer a fact from a search score or graph edge alone. Distinguish current TOPTOP facts from dated historical outcomes, model proposals, and maternal imports.

Keep a small local task note when useful: objective, source IDs, decisions, files changed, checks, next step. Do not bulk mirror the GALACTICA corpus. Do not store credentials, personal sessions, hidden reasoning, or exact messages without a verified source. At handoff, record the outcome through `finish_task`; a local note does not replace the canonical record.
