#!/usr/bin/env bash
set -euo pipefail

curl -L 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT7BB5NaSQNvxVAvCla3hZBgXZHRzHvqF4os5sQb7aF5_yxqQSfYttlmif6cJnm5lH1mlaeW-fm2rvC/pub?gid=1909145563&single=true&output=csv' > data/abstracts.csv
LINE_COUNT=` cat data/abstracts.csv | wc -l`
rm -f content/abstract/submission*
for j in `seq 1 $LINE_COUNT`
do
    ROW=$j hugo new "abstract/submission-$j.md"
done
