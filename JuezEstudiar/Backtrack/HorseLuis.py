
def findAWayBC(f,c, metax, metay, tablero, N, visit, mejorVisit):
    if f == metax and c == metay:
        if visit < mejorVisit:
            mejorVisit = visit+1
    else:
        mov = [[2, 1],[2, -1],[1, 2],[1, -2],[-2, 1],[-2, -1],[-1, 2],[-1, -2]]
        i = 0
        while i < len(mov):
            if esFactible(f + mov[i][0], c + mov[i][1], tablero, N):
                tablero[f + mov[i][0]][c + mov[i][1]] = 1
                visit += 1
                mejorVisit = findAWayBC(f + mov[i][0],c + mov[i][1],metax, metay, tablero, N, visit, mejorVisit)
                tablero[f + mov[i][0]][c + mov[i][1]] = 0
                visit -=1
            i += 1
    return mejorVisit



def esFactible(f, c, tablero, N):
    if f >= 0 and f < N and c >= 0 and c < N and tablero[f][c] == 0:
        return True
    else:
        return False

# N
N = 5

# Tablero
tablero = []
fila = [0] * N
for i in range(N):
    tablero.append(fila)
# f, col
fila, col = map(int, input().strip().split())

#metax, metay
metax, metay = map(int, input().strip().split())

visit = 0
mejorVisit = float('inf')
sol = findAWayBC(fila, col, metax, metay, tablero, N, visit, mejorVisit)

print(sol)
