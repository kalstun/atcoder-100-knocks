n,m = map(int, input().split())

if m < n*2 or m > n*4:
    r = [-1, -1, -1]
elif m == n*4:
    r = [0, 0, n]
else:
    a = m // n
    b = m % n
    if a == 2:
        r = [n-b, b, 0]
    else:
        r = [0, n-b, b]

print(" ".join(map(str, r)))

"""
# 一人以上を保証する場合
n -= 3
m -= 9
if n <= 0 or m <= 0:
    if n == 0 and m == 0:
        r = [1, 1, 1]
    else:
        r = [-1, -1, -1]
elif m < n*2 or m > n*4:
    r = [-1, -1, -1]
elif m == n*4:
    r = [1, 1, n+1]
else:
    a = m // n
    b = m % n
    if a == 2:
        r = [n+1-b, 1+b, 1]
    else:
        r = [1, n+1-b, 1+b]

print(" ".join(map(str, r)))
"""
