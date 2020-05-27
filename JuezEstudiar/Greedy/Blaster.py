# Posicion, Objetivo, potencia
T, O, P = map(int, input().strip().split())

# Nodos y aristas
N, M = map(int, input().strip().split())

# Costes nodos
cS = (input().split())
costes = []
for i in range (N):
    costes.append(int(cS[i]))

#Adyacencias
grafo = [[] for i in range(N)]
for j in range(M):
    a, b = map(int, input().strip().split())
    grafo[a-1].append(b)
    grafo[b-1].append(a)

pGastada = 0
esSol = False
nodo = T
meta = O
visitados = []
costesN = []
for j in range(N):
    costesN.append(float('inf'))
costesN[nodo - 1] = 0
sol = 0

while pGastada <= P and not esSol:
    visitados.append(nodo)
    nodoNext = -1
    better = float('inf')
    for j in grafo[nodo - 1]:
        if j == meta:
            sol = nodo
            esSol = True
            break;
        if pGastada + costes[j - 1] < costesN[j - 1] and j not in visitados:
            costesN[j - 1] = pGastada + costes[j - 1]
        #if costesN[j - 1] < better and j not in visitados:
            #better = costesN[j - 1]
            #nodoNext = j
    if not esSol:
        for w in range(N):
            if costesN[w] <= better and w+1 not in visitados:
                better = costesN[w]
                nodoNext = w + 1
        if (nodoNext) != meta:
            pGastada = costesN[nodoNext - 1]
            nodo = nodoNext
            #esSol = True
        #else:

if sol == 0:
    print(0)
else:
    print(P - costesN[sol - 1])