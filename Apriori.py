import itertools
import csv

records = []
row_count = 0
cols = 0
row_count = sum(1 for row in csv.reader(open('Book2.csv', "rt")))
min_support = int(input("Enter minimum support: "))
with open('Book2.csv', 'r') as f:
    reader = csv.reader(f)
    records = list(reader)
for i in records:
    while ' ' in i:
        i.remove(' ')
    while '' in i:
        i.remove('')
c1 = []
for i in range(0, len(records)):
    for j in range(0, len(records[i])):
        if records[i][j] not in c1:
            c1.append(records[i][j])
freq = {}
for i in range(0, len(records)):
    for j in range(0, len(records[i])):
        if records[i][j] not in freq:
            freq[records[i][j]] = 1
        else:
            freq[records[i][j]] = freq[records[i][j]] + 1
l = [[]]
for i in range(0, len(c1)):
    if freq[c1[i]] >= min_support:
        l[0].append(c1[i])
c2 = list(itertools.combinations(l[0], 2))
for k in c2:
    for i in range(0, len(records)):
        if k[0] in records[i] and k[1] in records[i]:
            if k not in freq:
                freq[tuple(k)] = 1
            else:
                freq[tuple(k)] = freq[tuple(k)] + 1
x = []
l.append([])
print("Second frequent item set is: ")
for i in c2:
    if i in freq and freq[i] >= min_support:
        l[1].append(i)
        print(i, freq[i])
        for k in i:
            if k not in x:
                x.append(k)
