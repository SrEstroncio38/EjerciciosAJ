# Numero pociones y tiempo para beberlas
N, M = map(int, input().strip().split())
potis = []

for i in range(N):
    poti = int(input())
    potis.append(poti)

potis.sort()

j = 0
tActual = 0
acumulado = 0
while j < N and tActual <= M:
    acumulado += potis[j]
    tActual += acumulado
    j += 1

if tActual <= M:
    print('AleG')
else:
    print('Dora')