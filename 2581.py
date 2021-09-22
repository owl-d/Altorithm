#2581 : 소수2

min = int(input())
max = int(input())

list = []
sum = 0
sosu = False

for i in range(max-min+1):
    S = False
    num = i + min
    if num == 1:
        S = True
    elif num == 2:
        S = False
    else:
        for j in range(num-2):
            if num % (j+2) == 0:
                S = True
                break

    if S == False:
        sum += num
        list.append(num)
        sosu = True

if sosu == False:
    print("-1")
else:
    print(sum)
    print(list[0])