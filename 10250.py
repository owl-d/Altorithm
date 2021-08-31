#10250 : ACM 호텔

n = int(input())
for i in range(n):
    h, w, n = map(int, input().split())

    if (n % h) == 0:
        number = int((n-1) / h) + 1
        floor = h
    else:
        number = int(n / h) + 1
        floor = int(n % h)

    if number < 10:
        print(floor, "0", number, sep="")
    else:
        print(floor, number, sep="")
        