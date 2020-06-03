N = int(input().strip())

partidos = []
diputados = 0
maxes = []
diptuTot = -1
ganador = ''
for i in range(N):
    names = input().strip().split()
    if int(names[1]) > diptuTot:
        ganador = names[0]
        diptuTot = int(names[1])
    if int(names[1]) > 0:
        partidos.append([int(names[2])/int(names[1]), names[0], int(names[1]), int(names[2])])
    else:
        partidos.append([int(names[2]), names[0], int(names[1]), int(names[2])])
    diputados += int(names[1])


partidos.sort()
sol = []
sol.append(ganador)
j = 0
diptuMax = int(diputados/2) + 1

while diptuTot < diptuMax and j < N:
    if partidos[j][1] not in sol:
        if diptuTot + partidos[j][2] < diptuMax:
            sol.append(partidos[j][1])
            diptuTot += partidos[j][2]
        else:
            sol.append(partidos[j][1])
            diptuTot += partidos[j][2]
    j += 1

sol.sort()
print(ganador)
for a in range(len(sol)):
    if sol[a] != ganador:
        print(sol[a])