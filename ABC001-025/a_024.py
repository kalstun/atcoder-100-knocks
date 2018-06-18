a,b,c,k = map(int, input().split())
s,t = map(int, input().split())
if s+t >= k:
    discount = 1
else:
    discount = 0
print(a*s + b*t - c*(s+t)*discount)
