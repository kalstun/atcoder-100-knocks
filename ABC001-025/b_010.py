# 1   3   5
# 1   3 4   6

_ = input()
a = list(map(lambda x: x%6, map(int, input().split())))

petal = 0
petal += a.count(2)
petal += a.count(4)
petal += a.count(5)*2
petal += a.count(0)*3

print(petal)
