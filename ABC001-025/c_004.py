n = int(input())
n = n%30
s = list("123456123456")
c = [s[n//5]]
l = s[n//5+1 : n//5+n%5+1]
r = s[n//5+n%5+1 : n//5+6]
print("".join(l+c+r))
