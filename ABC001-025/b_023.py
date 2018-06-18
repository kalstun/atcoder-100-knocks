n = int(input())
s = input()

def check_abc(string):
    if string == "b":
        return True
    else:
        t = string[0]
        for i in string[1:]:
            if (t=="a" and i=="b") \
            or (t=="b" and i=="c") \
            or (t=="c" and i=="a"):
                t = i
                continue
            else:
                return False
        else:
            return True

def check(s):
    if s[0] == "a" and len(s) % 6 == 3:
        if check_abc(s):
            return len(s)//2
    elif s[0] == "b" and len(s) % 6 == 1:
        if check_abc(s):
            return len(s)//2
    elif s[0] == "c" and len(s) % 6 == 5:
        if check_abc(s):
            return len(s)//2
    return -1

print(check(s))
