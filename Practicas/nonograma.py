def iniSol(rows):
    return [0] * rows

def nonoBacktrack(sol, filaActual, rows, cols, fCon, cCon, activeCols):
    # sol es un array de tantas posiciones como filas haya y guardará la columna donde se insertará la solucion
    # para el print, ya que al ir en bloque puedo guardar solo donde empieza
    if filaActual >= rows:
        esSol = True
    else:
        esSol = False
        colActual = 0
        while not esSol and colActual < cols:
            isValid, newCCon, newAcCols = esFactible(filaActual, colActual, fCon, cCon, activeCols)
            if isValid:
                sol[filaActual] = colActual + 1
                # printSol(sol, rows, cols, fCon, cCon)
                [sol, esSol] = nonoBacktrack(sol, filaActual+1, rows, cols, fCon, newCCon, newAcCols)
                # Reseteo solución y las condiciones en las columnas
                if not esSol:
                    sol[filaActual] = 0
            colActual += 1
    # print('backtrack',filaActual)

    # printSol(sol, rows, cols, fCon, cCon)
    # print()
    return sol, esSol


def esFactible(filaActual, colActual, fCon, cCon, activeCols):
    # Para saber si es factible primero compruebo si la fila a insertar, desde la columna en la que estoy tiene
    # espacio para colocarse y también si se esta dejando un hueco en las columnas ya que al ser nonogramas
    # simples no puede haber espacios entre los # de una fila y una columna, también reviso si hay que insertar
    # 0 (una columna en blanco) ya que ha que comprobar si esta es viable por los huecos
    colSize = len(cCon)
    lastCol = colActual + fCon[filaActual]
    if colActual + fCon[filaActual] - 1 >= colSize:
        return False, cCon, activeCols
    if (colActual != 0):
        i = 1
        while colActual - i >= 0:
            if (cCon[colActual - i] > 0 and activeCols[colActual - i]):
                return False, cCon, activeCols
            i += 1
    i = 0
    while lastCol + i < colSize:
        if (fCon[filaActual] != 0):
            if (lastCol + i < colSize):
                if (cCon[lastCol + i] > 0 and activeCols[lastCol + i]):
                    return False, cCon, activeCols
        else:
            lastCol = colActual + 1
            if (lastCol + i < colSize):
                if (cCon[lastCol + i] > 0 and activeCols[lastCol + i]):
                    return False, cCon, activeCols
            if (cCon[colActual] > 0 and activeCols[colActual]):
                return False, cCon, activeCols
        i += 1

    # Si pasa las restricciones anteriores se intenta insertar la fila comprobando que coincida con las condiciones de
    # columnas dadas
    cConCopy = cCon[:]
    aColsCopy = activeCols[:]
    for i in range(fCon[filaActual]):
        if cConCopy[colActual+i] <= 0:
            return False, cCon, activeCols
        else:
            cConCopy[colActual+i] -= 1
            aColsCopy[colActual+i] = True
    else:
        return True, cConCopy, aColsCopy

def printSol(sol, rows, cols, fCon, cCon):
    nono = initNono(rows, cols)
    for fila in range(rows):
        if fCon[fila] != 0:
            nono[fila][sol[fila]-1] = 1
        i = 0
        while(i < cols):
            if nono[fila][i] == 1:
                if fCon[fila] > 0:
                    for j in range(fCon[fila]):
                        print('#', end='')
                    i += fCon[fila]
            else:
                print('-', end='')
                i += 1
        print()

def initNono(rows, cols):
    f = [0] * cols
    nono = []
    for i in range(rows):
        nono.append(f[:])
    return nono


######### Programa principal ##########
# import time

# Recogemos la entrada
rows, cols = map(int, input().strip().split())
fCon = []
str = input().split()
tCols, tRows = [0 , 0]
kimPossible = False
for i in range (rows):
    fCon.append(int(str[i]))
    tRows += int(str[i])
    if (int(str[i]) > cols):
        kimPossible = True
cCon = []
str = input().split()
for i in range (cols):
    cCon.append(int(str[i]))
    tCols += int(str[i])
    if (int(str[i]) > rows):
        kimPossible = True

# start_time = time.time()
# Comprobamos que el número de # a colocar quepa en el nonograma y que el numero de # sea el mismo
if kimPossible or tCols != tRows:
    print('IMPOSIBLE')
else:
    sol = iniSol(rows)
    filaIni = 0
    activeCols = [False] * cols
    [sol, esSol] = nonoBacktrack(sol, filaIni, rows, cols, fCon, cCon, activeCols)
    #esSol = True
    #sol = [2, 2, 1, 1, 1]
    if esSol:
        printSol(sol, rows, cols, fCon, cCon)
    else:
        print('IMPOSIBLE')
# print("--- %s seconds ---" % (time.time() - start_time))