#1011 : Fly me to the Alpha Centauri

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    distance = y - x
    max = 1
    out = 1
    new = 1

    for j in range(distance):
        if distance > max:
            out += 1
        else:
            break

        if out%2==1: #홀수면 +1, 아니면 유지
            new += 1
        max += new

    print(out)