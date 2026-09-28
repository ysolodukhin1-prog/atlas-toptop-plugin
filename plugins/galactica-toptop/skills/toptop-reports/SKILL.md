---
name: toptop-reports
description: Build TOPTOP analytical reports from authorized daughter GALACTICA context and verified source data; use for KPI, marketplace, sales, finance, and 1C reporting requests.
---

# Reports from TOPTOP data

Use `galactica_toptop_client.trend_read_abc` for current ABC summary or stats from Ozon/Wildberries. Use the same personal TREND login as GALACTICA; no separate source link is required. On denied access, ask the administrator to check the explicit GALACTICA and ABC data grants in TREND. Never ask for passwords in chat. Other reports and arbitrary SQL are not exposed yet. Preserve returned period, filters, query time, and freshness status. A query time is not a verified source update time.

Start with the decision the report supports. Search daughter knowledge for metric definitions, source systems, grain, update lag, and existing report methods. `list_skills` and `get_skill` may expose imported maternal report procedures: check each candidate's source, status, version, and scope before applying it. An imported candidate is guidance, not a validated TOPTOP computation.

For each metric, record numerator, denominator, period, time zone, grain, filters, source, freshness, and treatment of missing data. Obtain TOPTOP operational figures through its approved TREND connection and verify the caller's source permissions before reading them. Do not infer live figures from GALACTICA knowledge alone. Check overlap between 1C documents and their movements, between Розница/УТ/ERP, and between marketplace feeds before aggregating. Inventory is a snapshot at a date. A document and its register movement are not independent sales. Compare a sample against the operational source and state any reconciliation gap.

Separate observed values from estimates and recommendations. Link tables and conclusions to canonical IDs or source artifacts, with the date checked. If the needed live data is not exposed through authorized tools, state the gap and request the source; do not use a cached knowledge summary as a current financial result.
