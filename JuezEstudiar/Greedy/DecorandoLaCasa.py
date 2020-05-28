# Nhab, Npuer, tiempo
N, M, T = map(int, input().strip().split())

# Adyacencias por nodos
grafo = [[] for i in range(M)]
for i in range(M):
    H1, H2, D = map(int, input().strip().split())
    grafo[H1].append([H2, D])
    grafo[H2].append([H1, D])

tActual = 0
tLimit = 0
esSol = False
nodo = 0
visitados = set()
costesN = []
for j in range(N):
    costesN.append(float('inf'))
costesN[nodo] = 0
sol = 0

while tActual <= T and not esSol:
    visitados.add(nodo)
    nodoNext = -1
    better = float('inf')
    if len(visitados) >= N:
        esSol = True
    for j in grafo[nodo]:
        if costesN[nodo] < float('inf'):
            tActual = costesN[nodo]
        else:
            tActual = 0
        if tActual + j[1] < costesN[j[0]] and j[0] not in visitados:
            costesN[j[0]] = tActual + j[1]
    if not esSol:
        for w in range(N):
            if costesN[w] <= better and w not in visitados:
                better = costesN[w]
                nodoNext = w
        nodo = nodoNext

for a in range(N):
    tLimit += costesN[a]

if tLimit > T:
    print('Aleg, ¡a decorar!')
else:
    print(tLimit)
