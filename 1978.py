#1978 : 소수 찾기

n = int(input())

num_list = list(map(int, input().split()))
out = 0

for i in range(n):
    B = False
    for j in range(num_list[i]):
        if j+2 == num_list[i]:
            break
        if num_list[i] == 1:
            B = True
            break
        if num_list[i] % (j+2) == 0:
            B = True
            break
    if B == False:
        out += 1

print(out)