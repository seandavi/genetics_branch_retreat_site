#!/usr/bin/env python3

import csv
import requests
import json

resp = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vT7BB5NaSQNvxVAvCla3hZBgXZHRzHvqF4os5sQb7aF5_yxqQSfYttlmif6cJnm5lH1mlaeW-fm2rvC/pub?gid=1909145563&single=true&output=csv")

header_map = {
    "Timestamp": "timestamp",
    "Email Address": "email",
    "Submitter Name": "submitter",
    "What is your current position?": "position",
    "Supervisor Name": "PI",
    "Abstract title": "title",
    "Full author list": "authors",
    "Body of abstract": "abstract"
}

reader = csv.DictReader(resp.text.strip().split('\n'))
reader.fieldnames = list([header_map[x] for x in reader.fieldnames])
rows = list([row for row in reader])

with open('app/src/assets/abstracts.json','w') as f:
    f.write(json.dumps(rows))
