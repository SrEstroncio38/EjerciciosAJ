

def EquiposBattleRoyal(personaje, lvls, sol, mejorSol, equipos):
    if personaje >= len(lvls):
        sol = max(abs(equipos[0] - equipos[1]), abs(equipos[0] - equipos[2]), abs(equipos[1] - equipos[2]))
        if sol <= mejorSol:
            mejorSol = sol
    else:
        j = 0
        while j < 3:
            equipos[j] += lvls[personaje]
            mejorSol = EquiposBattleRoyal(personaje + 1, lvls, sol, mejorSol, equipos)
            equipos[j] -= lvls[personaje]
            j += 1

    return mejorSol
# N
N = int(input())

# niveles
niveles = input().strip().split()
lvls = []
equipos = [0] * 3


for i in range(N):
    lvls.append(int(niveles[i]))

sol = 0
mejorSol = float('inf')
personaje = 0

mejorSol = EquiposBattleRoyal(personaje, lvls, sol, mejorSol, equipos)
print(mejorSol)

