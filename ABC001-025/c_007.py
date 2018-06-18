import queue

r,c = map(int, input().split())
t,s = map(int, input().split())
y,x = map(int, input().split())
f = [list(input()) for _ in range(r)]

e = ((-1,0),(0,-1),(0,1),(1,0))
f[t-1][s-1] = "0"
q = queue.Queue()
q.put([t,s])

while q:
    t,s = q.get()

    for d in e:
        if t+d[0] == y and s+d[1] == x:
            print(int(f[t-1][s-1])+1)
            exit()
        elif f[t-1 + d[0]][s-1 + d[1]] == ".":
            f[t-1 + d[0]][s-1 + d[1]] = str(int(f[t-1][s-1])+1)
            q.put([t+d[0], s+d[1]])
        else:
            continue
