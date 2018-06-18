s = list(input())
n = int(input())
for _ in range(n):
    l,r = map(int, input().split())
    s[l-1:r] = reversed(s[l-1:r])
else:
    print("".join(s))
