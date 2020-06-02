def esFactible(visitados, nodo):
    if nodo not in visitados:
        return True
    else:
        return False


def backtrack(nodo, nodoMeta, grafo, sol, visitados):
    if nodoMeta in grafo[nodo] and len(visitados) == len(grafo):
        sol += 1
    else:
        i = 0
        while i < len(grafo[nodo]):
            if esFactible(visitados, grafo[nodo][i]):
                visitados.add(grafo[nodo][i])
                sol = backtrack(grafo[nodo][i], nodoMeta, grafo, sol, visitados)
                visitados.remove(grafo[nodo][i])
            i += 1
    return sol




#N M
N, M = map(int, input().strip().split())

grafo = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)

nodoMeta = 0
nodo = 0
sol = 0
visitados = set()
visitados.add(nodo)

sol = backtrack(nodo, nodoMeta, grafo, sol, visitados)
print(sol)