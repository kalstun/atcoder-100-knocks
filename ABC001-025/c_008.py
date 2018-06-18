from collections import Counter

n = int(input())
c = [int(input()) for _ in range(n)]

d = Counter(c)
e = Counter(c)
s = sorted(d.keys())

for i in range(len(s)-1,-1,-1):
    for j in range(i+1,len(s)):
        if s[j] % s[i] == 0:
            e[s[j]] = d[s[i]] + e[s[j]]

front = lambda x: ((e[x]+1)//2)/e[x]
print(sum(map(front, c)))
