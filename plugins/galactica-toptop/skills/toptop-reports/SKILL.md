---
name: toptop-reports
description: Build TOPTOP analytical reports from authorized daughter GALACTICA context and verified source data; use for KPI, marketplace, sales, finance, and 1C reporting requests.
---


# Reports from TOPTOP data


For operational data, first call `whoami` and `trend_list_sources`. Its current personal TREND grants, report catalog and availability determine what can be read; GALACTICA knowledge/task/Markdown rights do not grant source access. TOPTOP tools never access another client, even when the TREND user has rights there.

Choose the existing report that matches the task: `trend_describe_report` returns operations, filters and bounds; `trend_read_report` executes the selected operation. The catalog includes non-ABC reports. Use only described parameters and operations; `trend_read_abc` remains a compatibility tool.

For 1C data, call `trend_list_databases`, `trend_list_tables` and `trend_describe_table` before `trend_query_database`. Select explicit columns; push filters and aggregations into the bounded query. One authorized table per query; no raw SQL, writes or cross-database identifiers. Combine separate reads only after validating business keys and grain.

For MPStats, use `trend_list_source_methods` to discover permitted published GET methods and parameters, then `trend_read_source`. Use the server's existing connection; never ask for database passwords, API keys, SSH or local connection setup. API tariff restrictions and network failures are distinct from TREND authorization.

Inspect `availability`, `reason_code`, partial coverage and `truncated` before using any response. A listed permission is not proof that the source is technically available. Do not present unavailable reports, truncated totals or empty unverified periods as a successful business conclusion. Preserve source, period, filters, query time and reported update timestamp. Query time is not source refresh time. Historical GALACTICA knowledge cannot replace missing operational data. On denied access, ask the administrator to review that person's existing TREND grants; do not request an administrator account or broaden rights yourself.

Start with the decision the report supports. Search daughter knowledge for metric definitions, source systems, grain, update lag, and existing report methods. `list_skills` and `get_skill` may expose imported maternal report procedures: check each candidate's source, status, version, and scope before applying it. An imported candidate is guidance, not a validated TOPTOP computation.


For each metric, record numerator, denominator, period, time zone, grain, filters, source, freshness, and treatment of missing data. Obtain TOPTOP operational figures through its approved TREND connection and verify the caller's source permissions before reading them. Do not infer live figures from GALACTICA knowledge alone. Check overlap between 1C documents and their movements, between Розница/УТ/ERP, and between marketplace feeds before aggregating. Inventory is a snapshot at a date. A document and its register movement are not independent sales. Compare a sample against the operational source and state any reconciliation gap.


Separate observed values from estimates and recommendations. Link tables and conclusions to canonical IDs or source artifacts, with the date checked. If the needed live data is not exposed through authorized tools, state the gap and request the source; do not use a cached knowledge summary as a current financial result.

