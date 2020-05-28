# Pilotes, arista
N, M = map(int, input().strip().split())

# a, b
grafo = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)

visitados = set()
nodo = 0
cucharadas = 0
while nodo < N:
    if nodo not in visitados:
        cola = []
        cola.append(nodo)
        visitados.add(nodo)
        while len(cola) > 0:
            n = cola.pop()
            for a in grafo[n]:
                if a not in visitados:
                    visitados.add(a)
                    cola.append(a)
        cucharadas += 1
    nodo += 1
print(cucharadas)

