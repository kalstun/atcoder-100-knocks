a = int(input())
b = int(input())
c = int(input())
score = (a,b,c)
for i in range(3):
    if score[i] == max(score):
        print(1)
    elif score[i] == min(score):
        print(3)
    else:
        print(2)
