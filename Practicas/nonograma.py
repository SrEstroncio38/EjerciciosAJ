def iniSol(rows):
    return [0] * rows

def nonoBacktrack(sol, filaActual, rows, cols, fCon, cCon, activeCols):
    if filaActual >= rows:
        esSol = True
    else:
        esSol = False
        colActual = 0
        while not esSol and colActual < cols:
            isValid, newCCon, newAcCols, badLine = esFactible(filaActual, colActual, fCon, cCon, activeCols)
            if isValid:
                sol[filaActual] = colActual + 1
                [sol, esSol] = nonoBacktrack(sol, filaActual+1, rows, cols, fCon, newCCon, newAcCols)
                # Reseteo solución y las condiciones en las columnas
                if not esSol:
                    sol[filaActual] = 0
            if badLine:
                colActual += cols
            colActual += 1
            badLine = False
    # print('backtrack',filaActual)
    return sol, esSol


def esFactible(filaActual, colActual, fCon, cCon, activeCols):
    # Tengo que mirar que en la columna actual * las col que ocupan los # haya suficiente espacio para usarlas
    if colActual + fCon[filaActual] - 1 >= len(cCon):
        return False, cCon, activeCols, False
    if (colActual != 0):
        if (cCon[colActual - 1] > 0 and activeCols[colActual - 1]):
            return False, cCon, activeCols, False
    if (fCon[filaActual] != 0):
        lastCol = colActual + fCon[filaActual]
        if (lastCol < len(cCon)):
            if (cCon[lastCol] > 0 and activeCols[colActual + fCon[filaActual]]):
                return False, cCon, activeCols, False
    else:
        lastCol = colActual + 1
        if (lastCol < len(cCon)):
            if (cCon[lastCol] > 0 and activeCols[colActual + 1]):
                return False, cCon, activeCols, False
        if(cCon[colActual] > 0 and activeCols[colActual]):
            return False, cCon, activeCols, False
        else:
            return True, cCon, activeCols, False
    cConCopy = cCon[:]
    aColsCopy = activeCols[:]
    for i in range(fCon[filaActual]):
        if cConCopy[colActual+i] <= 0:
            return False, cCon, activeCols, False
        else:
            cConCopy[colActual+i] -= 1
            aColsCopy[colActual+i] = True
    else:
        return True, cConCopy, aColsCopy, False

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


# Programa principal
import time

rows, cols = map(int, input().strip().split())
fCon = []
str = input().split()
for i in range (rows):
    fCon.append(int(str[i]))
cCon = []
str = input().split()
for i in range (cols):
    cCon.append(int(str[i]))
start_time = time.time()
# fCon = map(int, input().strip().split())
# cCon = map(int, input().strip().split())
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
print("--- %s seconds ---" % (time.time() - start_time))