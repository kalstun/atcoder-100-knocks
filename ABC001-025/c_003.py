n,k = map(int, input().split())
r = list(map(int, input().split()))
reviewed = sorted(r)[-k:]
rate = 0
for v in reviewed:
    rate = (rate + v) / 2
else:
    print(rate)
