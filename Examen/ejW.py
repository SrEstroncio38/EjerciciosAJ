N, M = map(int, input().strip().split())

pruebas = []
for i in range(N):
    id, duracion = map(int, input().strip().split())
    pruebas.append([duracion, id])

pruebas.sort()

maxes = []
for a in range(M):
    tiempoMax = int(input().strip())
    maxes.append(tiempoMax)

sol = []
for z in range(M):
    p = 0
    tiempoActual = 0
    cont = 0
    tAcumulado = 0
    while p < N and tiempoActual <= maxes[z]:
        tAcumulado += pruebas[p][0]
        if tAcumulado + tiempoActual <= maxes[z]:
            cont += 1
            tiempoActual += tAcumulado
        else:
            tiempoActual += tAcumulado
        p += 1
    sol.append(cont)

for j in range(len(sol)):
    print(sol[j])

