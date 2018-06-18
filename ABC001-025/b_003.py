s = input()
t = input()

result = True

for (a,b) in zip(s,t):
    if a == b:
        continue
    elif a == "@":
        if b in "atcoder@":
            continue
        else:
            result = False
            break
    elif b == "@":
        if a in "atcoder":
            continue
        else:
            result = False
            break
    else:
        result = False
        break

if result:
    print("You can win")
else:
    print("You will lose")
