# Numero casos y Dinero Cherlo
N, M = map(int, input().strip().split())
trabajos = []

for i in range(N):
    coste, beneficio = map(int, input().strip().split())
    trabajos.append([beneficio/coste, coste, beneficio, i])

trabajos.sort(reverse=True)
costeT = 0
sol = []
j = 0
bT = 0

while costeT < M and j <= N:
    if costeT + trabajos[j][1] < M:
        sol.append(trabajos[j][3])
        bT += trabajos[j][2]
        costeT += trabajos[j][1]
    else:
        sol.append(trabajos[j][3])
        bT += round((M - costeT) * trabajos[j][0])
        # bT += round((M - costeT) * (trabajos[j][2] / trabajos[j][1]))
        costeT += trabajos[j][1]
    j += 1

sol.sort()
for w in sol:
    print(w,'', end='')
print()
print(bT)
