def BusquedaBin(list, level, ini, fin):
    if ini > fin:
        return ini
    mitad = int((ini + fin) / 2)
    if level < list[mitad]:
        return BusquedaBin(list, level , ini, mitad - 1)
    else:
        return BusquedaBin(list, level, mitad + 1, fin)


N = int(input().strip())

ns = input().strip().split()
n = []
sum = 0
for i in range (N-1):
    sum += int(ns[i])
    n.append(sum)

M = int(input().strip())
idx = []
for j in range(M):
    exp = int(input())
    idx.append(BusquedaBin(n, exp, 0, N - 2))

for a in range(M):
    print(idx[a] + 1)



