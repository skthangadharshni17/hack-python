from collections import Counter

def word_order():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    
    # Counter preserves insertion order in Python 3.7+
    counts = Counter(words)
    
    print(len(counts))
    print(*(counts.values()))

if __name__ == '__main__':
    word_order()