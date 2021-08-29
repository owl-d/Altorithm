#1193 : 분수 찾기

n = int(input())
last = 0

for i in range(10000000):
    line = i+1
    last += line
    if n <= last:
        break

first = last - line + 1

order = n - first
up = order + 1
down = line - order

if line % 2 == 1: #홀수
    print(down, "/", up, sep="")
else: #짝수
    print(up, "/", down, sep="")
