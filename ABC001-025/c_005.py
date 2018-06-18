t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 0
for make in a:
    buy = b[i]
    if make <= buy and buy <= make+t :
        i += 1
        if i == m:
            print("yes")
            break
    elif buy < make:
        print("no")
        break
    else:
        continue
else:
    print("no")
