{{- range $i, $r := getCSV "," "data/abstracts.csv" -}}
{{ if eq (getenv "ROW") (string $i) }}
---
title: "{{ index $r 5 | title }}"
tags: ["{{ index $r 4 }}"]
weight: {{ $i }}
---

{{ index $r 6 }}

{{ index $r 7 }}

- Submitter: {{ index $r 2}} ({{ index $r 3 }})
- Supervisor: {{ index $r 4 }}
- email: {{ index $r 1 }}
{{ end }}
{{ end }}

