word = list(input())
wrd = filter(lambda l: l not in ["a", "e", "i", "u", "o"], word)
print("".join(wrd))
