import math

n = int(input())
num = math.ceil((n-1)/6)

if n == 1:
    print(1)
elif 1 <= n & n <= 7:
    print(2)
else:
    for i in range(100000):
        pre_last = i*(i+1)/2
        last = (i+1)*(i+2)/2
        if (num > pre_last) and (num <= last):
            print(i+2)
            break
