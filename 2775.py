#2775 : 부녀회장이 될테야

case = int(input())
for i in range(case):
    k = int(input())
    n = int(input())

    a = []
    line = []
    for j in range(n):
        line.append(j + 1)

    for i in range(k+1):
        post = 0
        a.append(line)
        line = []
        for j in range(n):
            line.append(a[i][j] + post)
            post = line[j]

    print(a[k][n-1])