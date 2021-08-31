#2869 : 달팽이는 올라가고 싶다

import sys
import math

a, b, v = sys.stdin.readline().split()
a = int(a)
b = int(b)
v = int(v)

day = math.ceil((v-b) / (a-b))

print(day)