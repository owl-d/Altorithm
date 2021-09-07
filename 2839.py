#2839 : 설탕 배달

n = int(input())

for i in range(n//5+2):
    temp = n - 5*(n//5+1-i)
    if (temp >= 0) and (temp % 3) == 0:
        guess = temp/3 + (n//5+1-i)
        break
    else:
        guess = -1

print(int(guess))