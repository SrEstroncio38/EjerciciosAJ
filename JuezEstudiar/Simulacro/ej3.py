N = int(input())
peso = 0
pesos = input().strip().split()
for i in range(N):
    peso += int(pesos[i])

K = int(input())

D = list(map(int, input().strip().split()))
M = list(map(int, input().strip().split()))

balas =[]
for j in range(K):
    balas.append([D[j]/M[j], D[j], M[j]])

balas.sort(reverse=True)
balasAct = 0
daño = 0
z = 0

while balasAct < peso and z < K:
    if balasAct + balas[z][2] <= peso:
        daño += balas[z][1]
        balasAct += balas[z][2]
    else:
        daño += round((peso - balasAct) * balas[z][0])
        balasAct += (peso - balasAct)
    z += 1

print(daño)
