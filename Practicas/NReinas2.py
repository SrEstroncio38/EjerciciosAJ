def inicializarSolucion(N):
    return [0] * N

def inicializarTablero(N):
    fila = [0] * N
    tablero = []
    for i in range(N):
        tablero.append(fila[:])
    return tablero

def imprimirSolucion(solucion):
    N = len(solucion)
    tablero = inicializarTablero(N)
    for fila in range(N):
        tablero[fila][solucion[fila]] = 1
        for columna in range(N):
            print(tablero[fila][columna],' ',end='')
        print()

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

# Prog Ppal:
N = 4
solucion = inicializarSolucion(N)
fila = 0
[solucion,exito] = NReinasVA(solucion,fila)
if exito:
    imprimirSolucion(solucion)
else:
    print('La instancia del problema planteada no tiene solución')
