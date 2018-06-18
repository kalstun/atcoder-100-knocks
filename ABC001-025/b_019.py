s = "aabbbaad"
c = 0
l = "!"
r = []
for i in s:
    if i == l:
        c += 1
    else:
        r.append(l+str(c))
        l = i
        c = 1
else:
    r.append(l+str(c))
    print("".join(r[1:]))
