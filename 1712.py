#1712 : 손익분기점

a, b, c = map(int, input().split())

if b >= c :
  n = -2
else:
  n = a//(c-b) #만족하는 최소의 n

print(n+1)
