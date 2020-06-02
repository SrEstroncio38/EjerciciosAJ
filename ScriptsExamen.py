############ ENTRADADAS Y SALIDAS ####################

# Varios Valores en una misma fila
N, M = map(int, input().strip().split())

# N valores pero sin parejas
nValores = 0
lista = []
for i in range(nValores):
    lista.append(int(input()))

# Grafo
grafo = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)

# Salida
# Vector Hor
for i in range(nValores):
    print(lista[i],'',end='')

# Vector Ver
for i in range(nValores):
    print(lista[i])

# Matriz
nFilas = 0
nCol = 0
for i in range(nFilas):
    for n in range(nCol):
        print(lista[i][n], '', end='')
    print()

############ BACKTRACKING ####################
def BacktrackingMejorSolucion(f,c, metax, metay, tablero, N, visit, mejorVisit):
    #Comprobamos que sea una solucion
    if f == metax and c == metay:
        #Comprobamos que la solucion actual sea mejor que la anterior
        if visit < mejorVisit:
            #Guardamos la solucion actual como mejor solucion
            mejorVisit = visit+1
    #Si no es solucion preparamos y comenzamos el bucle
    else:
        mov = [[2, 1],[2, -1],[1, 2],[1, -2],[-2, 1],[-2, -1],[-1, 2],[-1, -2]]
        i = 0
        # No hace falta el esSol, queremos que recorra el arbol completo, porque
        # cuando sea solución queremos que vuelva atrás no que continue
        while i < len(mov):
            #Comprobamos que sea factible
            if esFactible(f + mov[i][0], c + mov[i][1], tablero, N):
                #Probamos la siguiente solucion
                tablero[f + mov[i][0]][c + mov[i][1]] = 1
                visit += 1
                #Mejor solucion es igual al siguiente paso
                mejorVisit = findAWayBC(f + mov[i][0],c + mov[i][1],metax, metay, tablero, N, visit, mejorVisit)
                #La reiniciamos la solucion
                tablero[f + mov[i][0]][c + mov[i][1]] = 0
                visit -=1
            #Siguiente prueba
            i += 1
    return mejorVisit
