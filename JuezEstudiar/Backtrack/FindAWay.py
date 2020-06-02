
def findAWayBC(f,c, tablero, N, visit, permitidas):
    if f >= N-1 and c >= N-1 and permitidas - 1 == visit:
        esSol = True
    else:
        esSol = False
        mov = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        i = 0
        while not esSol and i < len(mov):
            if esFactible(f + mov[i][0], c + mov[i][1], tablero, N):
                tablero[f + mov[i][0]][c + mov[i][1]] = 1
                visit += 1
                esSol = findAWayBC(f + mov[i][0],c + mov[i][1], tablero, N, visit, permitidas)
                if not esSol:
                    tablero[f + mov[i][0]][c + mov[i][1]] = 0
                    visit -=1
            i += 1
    return esSol



def esFactible(f, c, tablero, N):
    if f >= 0 and f < N and c >= 0 and c < N and tablero[f][c] == 0:
        return True
    else:
        return False

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

