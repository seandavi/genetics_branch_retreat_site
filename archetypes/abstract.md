{{- range $i, $r := getCSV "," "data/abstracts.csv" -}}
{{ if eq (getenv "ROW") (string $i) }}
---
title: "{{ index $r 5 | title }}"
tags: ["{{ index $r 4 }}"]
weight: {{ $i }}
author: {{ index $r 2 }}
length: {{ index $r 8 }}           
---

{{ index $r 6 }}

- Submitter: {{ index $r 2}} ({{ index $r 3 }})
- email: {{ index $r 1 }}
                  
{{ index $r 7 }}


{{ end }}
{{ end }}

