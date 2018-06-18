n = int(input())
a = [int(input()) for _ in range(n)]

s = list(set(a))
s.sort()
s.pop()
print(s.pop())
