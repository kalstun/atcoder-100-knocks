n = int(input())
a = list(map(int, input().split()))
ra = sorted(a, reverse=True)
while ra[-1] == 0:
    ra.pop()
    n -= 1
else:
    sa = sum(ra)
    if sa % n:
        print(sa // n + 1)
    else:
        print(sa // n)
