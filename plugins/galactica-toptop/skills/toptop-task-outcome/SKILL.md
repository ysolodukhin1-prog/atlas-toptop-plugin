---
name: toptop-task-outcome
description: Complete a TOPTOP task with a structured, sourced outcome in daughter GALACTICA; use after substantive work or when handing off an interrupted task.
---

# Task outcome for TOPTOP

Use the `task_id` returned by `start_task`. Before finishing, check the actual artifacts and results. Submit one `finish_task` with status `succeeded`, `partial`, or `failed` and these summary fields: `request`, `criteria`, `actions`, `result`, `decisions`, `rejected_options`, `skills_used`, `checks`, `changed_files`, `limitations`, `next_step`, `message_refs`, `artifact_refs`.

List only skills really applied, with their versions when available. Mark unverified claims and missing checks in `limitations`. Exact quotes require a stored exact source; do not reconstruct them from memory. The outcome is immutable; correct an inaccurate outcome with a new task instead of silently overwriting it. `finish_task` queues the daughter protocolizer, but the result is not proof that extraction or index projection has already completed.

For data work record which authorized report/source was actually called, query period, source freshness evidence, partial/truncated output and explicit failures. A catalog entry or past successful read is not a new verification. Exclude secrets and full business query results from technical outcomes.
