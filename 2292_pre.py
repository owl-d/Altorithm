#Runtime Error

def cal_floor(n, m, first, i):
    if n < first:
        print(i-1)
    else:
        cal_floor(n, m+6, first+m, i+1)

n = int(input())
if n == 1:
    print(1)
elif 1 <= n & n <= 7:
    print(2)
else:
    cal_floor(n, 12, 8, 3)


