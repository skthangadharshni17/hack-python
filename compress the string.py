from itertools import groupby
S = input().strip()
result = []
for k, g in groupby(S):
     result.append((len(list(g)), int(k)))
print(*result)