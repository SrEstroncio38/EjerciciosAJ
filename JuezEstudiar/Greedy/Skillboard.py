# Habilidades, Aristas
N, M = map(int, input().strip().split())

# Costes y definicion aristas
aristas = []
for i in range(M):
    X, Y, Z = map(int, input().strip().split())
    aristas.append([Z, X, Y])

aristas.sort()

conexas = []
#  Guardo en la posicion X el nodo X+1 pero lo represento como X
for j in range(N):
    conexas.append(j)

esSol = False
w = 0
coste = 0
while w < M and not esSol:
    nodoDer = -1
    nodoIzq = -1
    nodoDer = conexas[aristas[w][2]-1]
    nodoIzq = conexas[aristas[w][1]-1]
    convexCond = conexas[0]
    if nodoDer != nodoIzq:
        equals = True
        sumar = False
        for j in range(N):
            if conexas[j] == (nodoDer):
                conexas[j] = (nodoIzq)
                sumar = True
        if sumar:
            coste += aristas[w][0]
    for a in range(N):
        if convexCond != conexas[a]:
            equals = False
            break;
    if equals:
        esSol = True
    w += 1
if w == M:
    convexCond = conexas[0]
    equals = True
    for a in range(N):
        if convexCond != conexas[a]:
            equals = False
            break;
    if equals:
        esSol = True

if esSol:
    print(coste)
else:
    coste = 0
    convexTry = conexas[0]
    con = []
    for h in range(N):
        if conexas[h] == convexTry:
            con.append(h + 1)
    for g in range(M):
        if aristas[g][1] in con:
            coste += aristas[g][0]
            con.remove(aristas[g][1])
    print(coste)