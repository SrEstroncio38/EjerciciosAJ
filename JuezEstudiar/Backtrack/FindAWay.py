
def findAWayBC(f,c, tablero, N, visit, permitidas):
    if f >= N-1 and c >= N-1 and permitidas - 1 == visit:
        esSol = True
    else:
        esSol = False
        while not esSol:
            [facDer, facIzq, facTop, facBot] = esFactible(f, c, tablero, N)
            if facDer and c+1 < N:
                tablero[f][c] = 1
                visit += 1
                esSol = findAWayBC(f, c + 1, tablero, N, visit, permitidas)
                if not esSol:
                    visit -= 1
                    tablero[f][c] = 0
            elif facIzq and c - 1 >= 0:
                tablero[f][c] = 1
                visit += 1
                esSol = findAWayBC(f, c - 1 , tablero, N, visit, permitidas)
                if not esSol:
                    visit -= 1
                    tablero[f][c] = 0
            elif facTop and f - 1 >= 0:
                tablero[f][c] = 1
                visit += 1
                esSol = findAWayBC(f - 1, c, tablero, N, visit, permitidas)
                if not esSol:
                    visit -= 1
                    tablero[f][c] = 0
            elif facBot and f + 1 < N:
                tablero[f][c] = 1
                visit += 1
                esSol = findAWayBC(f + 1, c, tablero, N, visit, permitidas)
                if not esSol:
                    visit -= 1
                    tablero[f][c] = 0
            elif f >= N-1 and c >= N-1 and permitidas - 1 == visit:
                esSol = True
                break
            elif permitidas - 1 == visit and not(f >= N-1 and c >= N-1):
                esSol = False
                break
    return esSol



def esFactible(f, c, tablero, N):
    facDer = False
    facIzq = False
    facTop = False
    facBot = False
    if c+1 < N:
        facDer = tablero[f][c+1] == 0
    if c-1 >= 0:
        facIzq = tablero[f][c-1] == 0
    if f-1 >= 0:
        facTop = tablero[f-1][c] == 0
    if f + 1 < N:
        facBot = tablero[f+1][c] == 0
    return [facDer, facIzq, facTop, facBot]

# N
N = int(input())

# Tablero
tablero = []
permitidas = 0
for i in range(N):
    fila = input().strip().split()
    fila2 = []
    for j in range(N):
        a = int(fila[j])
        if a >= 0:
            permitidas += 1
        fila2.append(a)
    tablero.append(fila2)

fila = 0
col = 0
visit = 0
sol = findAWayBC(fila, col, tablero, N, visit, permitidas)

if sol:
    print('SI')
else:
    print('NO')

