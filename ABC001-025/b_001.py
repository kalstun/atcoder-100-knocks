def vv(length):
    if length < 100:
        return "00"
    elif length <= 5000:
        fixed = length // 100
        return "{:0>2}".format(str(fixed))
    elif length <= 30000:
        fixed = length // 1000 + 50
        return str(fixed)
    elif length <= 70000:
        fixed = (length // 1000 - 30) // 5 + 80
        return str(fixed)
    else:
        return "89"

m = int(input())
print(vv(m))
