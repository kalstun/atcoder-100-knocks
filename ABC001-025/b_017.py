x = input()

flag_ch = False

for letter in x:
    if flag_ch:
        if letter == "h":
            flag_ch = False
            continue
        else:
            print("NO")
            break
    elif letter == "c":
        flag_ch = True
        continue
    elif letter in "oku":
        continue
    else:
        print("NO")
        break
else:
    if flag_ch:
        print("NO")
    else:
        print("YES")
