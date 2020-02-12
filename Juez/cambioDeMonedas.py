T = int(input())
M = input().split()
nMonedas = []
for da in M:
    nMonedas.append(int(da))
d = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in range(T):
    num = int(input())
    iter = 0
    count = 0
    for j in nMonedas:
        if j > 0 and num > 0:
            temp = j
            while temp > 0:
                nT = num // d[iter]
                if nT > 0:
                    num = num - d[iter] * nT
                    count += nT
                    temp = -1
                else:
                    temp = -1
        iter += 1
    print(count)
