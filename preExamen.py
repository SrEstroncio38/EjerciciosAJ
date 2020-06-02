'''
MANDAMIENTOS
    - Usar set() para visitados u otros en lo que hacer contains
    - Cuidado con los indices en aristas (-1 si empieza por 1)
    - Al llamar a backtracking, no olvidar IGUALARLO y actualizar el paso (avance)
    - Cuidado con lo que printeamos al subirlo al juez (borrar prints)
    - Una vez subido un ejercicio al juez, pasar a otro directamente
    - Si en los límites:
        a) Si son muy grandes --> Greedy o DyV
        b) Si son pequeños    --> Backtracking
'''

### ENTRADA ESTÁNDAR ###

nValores = int(input())

a, b = map(int, input().strip().split())

lista = []
for i in range(nValores):
    lista.append(int(input()))

tablero = [[0 for i in range(nColumnas)] for n in range(nFilas)]
for i in range(nFilas):
    tablero[i] = list(map(int, input().strip().split()))

aristas = [[] for i in range(numNodos)]
for i in range(numAristas):
    a, b = map(int, input().strip().split())
    aristas[int(a)-1].append(int(b-1))
    aristas[int(b)-1].append(int(a-1))

### SALIDA ###

for i in range(nValores):
    print(array[i], "", end="")

for i in range(nValores):
    print(array[i])

for i in range(nFilas):
    for n in range(nColumnas):
        print(array[i][n], "", end="")
    print()


### ORDENACION ###

def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        mitadIzq = lista[:mid]
        mitadDer = lista[mid:]

        mergeSort(mitadIzq)
        mergeSort(mitadDer)

        i=0
        j=0
        k=0
        while i < len(mitadIzq) and j < len(mitadDer):
            if int(mitadIzq[i]) <= int(mitadDer[j]):
                lista[k] = mitadIzq[i]
                i=i+1
            else:
                lista[k] = mitadDer[j]
                j=j+1
            k=k+1

        while i < len(mitadIzq):
            lista[k] = mitadIzq[i]
            i=i+1
            k=k+1

        while j < len(mitadDer):
            lista[k] = mitadDer[j]
            j=j+1
            k=k+1

### BACKTRACKING ###

def backtracking1Sol (tablero, paso):
    if paso == len(tablero) * len(tablero[0]):
        esSol = True
    else:
        esSol = False
        mov = [] # Movimientos posibles
        i = 0
        while i < len(mov) and not esSol:
            if esFactible(tablero, paso):
                # Relleno datos
                tablero, esSol = backtracking1Sol(tablero, paso+1)
                if not esSol:
                    # Reseteo datos
            i += 1
    return tablero, esSol

def backtrackingBestSol (tablero, paso, mejorSol):
    if paso == len(tablero) * len(tablero[0]):
        esSol = True
        mejorSol = [] # Mejor solucion encontrada comparada con la que habia
    else:
        esSol = False
        mov = [] # Movimientos posibles
        i = 0
        while i < len(mov):
            if esFactible(tablero, paso):
                # Relleno datos
                tablero, esSol, mejorSol = backtracking1Sol(tablero, paso+1, mejorSol)
                if not esSol:
                    # Reseteo datos
            i += 1
    return tablero, esSol, mejorSol

### DyV ###

def divideYVenceras(array, limit, inicio, fin):
    if inicio != fin:
        mid = (fin + 1 - inicio) // 2
        if int(array[inicio + mid]) <= limit:
            return divideYVenceras(array, limit, inicio + mid, fin)
        elif int(array[inicio + mid]) > limit:
            return divideYVenceras(array, limit, inicio, fin - mid)
    else:
        if int(array[inicio]) > limit:
            inicio = inicio - 1
        return inicio
        # return array[inicio]

### Voraces ###

def mochila (casos, nMax):
    # Calculo de beneficio / gasto hacerlo al coger los datos mejor <3
    for i in range(len(casos)):
        casos[i].append(casos[i][2] / casos[i][1])

    # Ordeno array por el calculo anterior
    casos.sort(key=elem3, reverse=True)

    sol = [0] * len(casos)
    costeAcum = 0
    benAcum = 0
    i = 0
    while costeAcum < nMax:
        if costeAcum + casos[i][1] <= nMax:
            costeAcum += casos[i][1]
            benAcum += casos[i][2]
            sol[casos[i][0]] = 1
            i += 1
        else:
            sol[casos[i][0]] = (nMax - costeAcum) / casos[i][1]
            benAcum += (casos[i][2] * sol[casos[i][0]]).__round__()
            costeAcum = nMax

    return [sol, benAcum]

def dijkstraCaminoMinimo(posInicial, posObjetivo, pesosNodos, numNodos, aristas):
    visitados = []
    posActual = posInicial
    solucion = 0
    vectorDist = [float("inf")] * numNodos
    visitados.append(posActual)
    vectorDist[posActual] = 0
    fin = False
    while posActual != posObjetivo:
        min = float("inf")
        nodoSig = -1
        for i in range(len(aristas[posActual])):
            if not visitados.__contains__(aristas[posActual][i]):
                if posObjetivo == aristas[posActual][i]:
                    fin = True
                    break
                else:
                    if vectorDist[aristas[posActual][i]] > vectorDist[posActual] + pesosNodos[aristas[posActual][i]]:
                        vectorDist[aristas[posActual][i]] = vectorDist[posActual] + pesosNodos[aristas[posActual][i]]

        for i in range(len(vectorDist)):
            if not visitados.__contains__(i) and min > vectorDist[i]:
                min = vectorDist[i]
                nodoSig = i

        if fin:
            solucion = vectorDist[posActual]
            return solucion

        if nodoSig != posActual:
            visitados.append(nodoSig)
            posActual = nodoSig
        else:
            solucion = 0
            return solucion

    solucion = vectorDist[posActual]
    return solucion

def dijkstraCaminosMinimosDesdeUnNodo(posInicial, numNodos, aristas):
    visitados = set()
    posActual = posInicial

    vectorDist = [float("inf")] * numNodos
    visitados.add(posActual)
    vectorDist[posActual] = 0

    while len(visitados) != numNodos:
        min = float("inf")
        nodoSig = -1
        for i in range(len(aristas[posActual])):
            if not visitados.__contains__(aristas[posActual][i][0]):
                if vectorDist[aristas[posActual][i][0]] > vectorDist[posActual] + aristas[posActual][i][1]:
                    vectorDist[aristas[posActual][i][0]] = vectorDist[posActual] + aristas[posActual][i][1]

        for i in range(len(vectorDist)):
            if not visitados.__contains__(i) and min > vectorDist[i]:
                min = vectorDist[i]
                nodoSig = i

        if nodoSig != posActual:
            visitados.add(nodoSig)
            posActual = nodoSig

    return vectorDist

def prim(nodoInicio, aristas, nNodos):
    aristasCandidatas = []
    solucion = []
    coste = 0
    nodoSig = nodoInicio

    while len(solucion) < nNodos-1:
        # Añadimos a la solucion
        solucion.append(nodoSig)
        for i in range(len(aristas[nodoSig])):
            if aristas[nodoSig][i][0] not in solucion:
                aristasCandidatas.append(aristas[nodoSig][i])

        # Ordenamos para coger la de menor coste
        aristasCandidatas.sort(key=secondValue)
        while len(aristasCandidatas) > 0 and aristasCandidatas[0][0] in solucion:
            aristasCandidatas.pop(0)
        if len(aristasCandidatas) != 0:
            # Actualizamos solucion
            nodoSig = aristasCandidatas[0][0]
            coste += aristasCandidatas[0][1]
            # Sacamos la arista seleccionada
            aristasCandidatas.pop(0)
        else:
            break
    return coste

def kruskal(aristas, nNodos):
    # Ordeno por peso
    aristas.sort()
    conexas = []
    # Guardo en la posicion X el nodo X+1 pero lo represento como X
    for j in range(nNodos):
        conexas.append(j)

    esSol = False
    w = 0
    coste = 0
    while w < len(aristas) and not esSol:
        nodoDer = conexas[aristas[w][2] - 1]
        nodoIzq = conexas[aristas[w][1] - 1]
        convexCond = conexas[0]
        if nodoDer != nodoIzq:
            equals = True
            sumar = False
            for j in range(nNodos):
                if conexas[j] == nodoDer:
                    conexas[j] = nodoIzq
                    sumar = True
            if sumar:
                coste += aristas[w][0]
        for a in range(nNodos):
            if convexCond != conexas[a]:
                equals = False
                break
        if equals:
            esSol = True
        w += 1
    if w == len(aristas):
        convexCond = conexas[0]
        equals = True
        for a in range(nNodos):
            if convexCond != conexas[a]:
                equals = False
                break
        if equals:
            esSol = True

### Otros ###

def busquedaAnchura(aristas):
    coste = 0
    visitado = set()
    for i in range(len(aristas)):
        if not visitado.__contains__(i):
            coste += 1
            visitado.add(i)
            if len(aristas[i]) > 0:
                q = list()
                q.append(i)
                while len(q) > 0:
                    # Extraemos los adyacentes de un nodo
                    nodo = q.pop(0)
                    for n in range(len(aristas[nodo])):
                        if not visitado.__contains__(aristas[nodo][n]):
                            visitado.add(aristas[nodo][n])
                            q.append(aristas[nodo][n])

    return coste