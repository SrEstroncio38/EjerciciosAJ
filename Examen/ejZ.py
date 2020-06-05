
def backtracking(f,c, metax, metay, tablero, N, M, visit, mejorVisit):
    if f == metax and c == metay:
        if visit < mejorVisit:
            mejorVisit = visit
    else:
        mov = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        i = 0
        while i < len(mov):
            if esFactible(f + mov[i][0], c + mov[i][1], tablero, N, M):
                tablero[f + mov[i][0]][c + mov[i][1]][0] = 1
                visit += 1
                mejorVisit = backtracking(f + mov[i][0],c + mov[i][1],metax, metay, tablero, N, M, visit, mejorVisit)
                if tablero[f + mov[i][0]][c + mov[i][1]][1]:
                    tablero[f + mov[i][0]][c + mov[i][1]][0] = -1
                else:
                    tablero[f + mov[i][0]][c + mov[i][1]][0] = 0
                visit -=1
            i += 1
    return mejorVisit



def esFactible(f, c, tablero, N, M):
    if f >= 0 and f < N and c >= 0 and c < M:
        if tablero[f][c][0] == 0:
            return True
        if tablero[f][c][0] == 2:
            return True
        if (tablero[f][c][0] == -1 and (f + c) / 2 != 0):
            return True
    else:
        return False

# N
N, M= map(int,input().strip().split())

# Tablero
tablero = []
metax = 0
metay = 0

for i in range(N):
    fila = input().strip().split()
    fila2 = []
    for j in range(M):
        a = int(fila[j])
        muro = False
        if a == 2:
            metax = i
            metay = j
        if a == -1:
            muro = True
        fila2.append([a, muro])
    tablero.append(fila2)
tablero[0][0] = [1, False]
fila = 0
col = 0
visit = 0
mejorVisit = float('inf')

sol = backtracking(fila, col,metax, metay, tablero, N, M, visit, mejorVisit)

print(sol)
