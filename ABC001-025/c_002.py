a,b,c,d,e,f = map(int, input().split())
a -= e
b -= f
c -= e
d -= f
print(abs(a*d - b*c)/2)
