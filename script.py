import tldextract
import pandas as pd
import sys
import os

data = pd.read_csv(sys.argv[1])

col_no = int(sys.argv[2])

link = {}

for row in data.values:
    col = str(row[col_no]).strip()
    if col is None or len(col) == 0:
        continue
    domain = tldextract.extract(col).domain
    if domain in link:
        link[domain] += 1
    else:
        link[domain] = 1

dup = []

for key in link:
    if link[key] > 1:
        dup.append(key)

fil = set()

if os.path.exists('filter.txt'):
    filter = open('filter.txt','r')

    for l in filter.readlines():
        col = str(l).strip()
        domain = tldextract.extract(col).domain
        fil.add(domain)

if len(fil) > 0:
    print(list(fil.intersection(dup)))
else:
    print(dup)
