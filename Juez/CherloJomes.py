
# Casos y dinero que tiene Cherlo
N,M = map(int, input().strip().split())

# Recogo los datos y guardo lo que me interesa
candidatos = []


for i in range(N):
    coste, beneficio = map(int, input().strip().split())
    candidatos.append((beneficio/coste, coste, beneficio, i))

candidatos.sort(reverse=True)

# recorro la lista de candidatos
j = 0
sol = []
benFinal = 0
while(j < len(candidatos) and M > 0):
    M = M - candidatos[j][1]
    if M < 0:
        benFinal += round((M + candidatos[j][1]) * candidatos[j][0])
        sol.append(candidatos[j][3])
    else:
        benFinal += candidatos[j][2]
        sol.append(candidatos[j][3])
    j += 1

sol.sort()

for a in sol:
    print(a, "", end="")
print()
print(benFinal)