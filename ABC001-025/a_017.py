result = 0
for _ in range(3):
    s,e = map(int, input().split())
    result += s*e//10
else:
    print(result)
