def esFactible(solucion,fila,columna):
    factible = True
    i = 1
    while factible and i <= fila:
        factibleColumna = solucion[fila - i] != columna
        factibleDiag1 = solucion[fila - i] != columna - i
        factibleDiag2 = solucion[fila - i] != columna + i
        factible = factibleColumna and factibleDiag1 and factibleDiag2
        i += 1
    return factible

def NReinasVA(solucion,fila):
    N = len(solucion)
    if fila >= N:
        esSol = True
    else:
        esSol = False
        columna = 0
        while not esSol and columna < N:
            if esFactible(solucion,fila,columna):
                solucion[fila] = columna
                [solucion,esSol] = NReinasVA(solucion,fila+1)
                if not esSol:
                    solucion[fila] = 0
            columna += 1
    return solucion,esSol

# N, M
N, M = map(int, input().strip().split())

col = []
sol = []
if M > 0 and N > 3:
    pjs = input().strip().split()
    for i in range(N):
        if i < M:
            col.append(int(pjs[i]))
            sol.append(int(pjs[i]))
        else:
            col.append(0)
            sol.append(0)

    fila = M
    [solucion,exito] = NReinasVA(sol,fila)
    if exito:
        print('ADELANTE')
    else:
        print('VUELVE A EMPEZAR')

elif M <= 0 and N > 3:
    print('ADELANTE')
else:
    print('VUELCE A EMPEZAR')

