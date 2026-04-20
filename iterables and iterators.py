from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

combos = list(combinations(L, K))
favorable = [c for c in combos if 'a' in c]

print(f"{len(favorable) / len(combos):.4f}")