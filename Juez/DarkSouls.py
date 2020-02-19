def Astora(ene, level, ini, fin):
    if level <= 0:
        return 0
    if ini > fin:
        return ini
    else:
        mitad = int((ini+fin)/2)
        comp = int(ene[mitad])
        if comp > level:
            return Astora(ene, level, ini, mitad-1)
        if comp < level:
            return Astora(ene, level, mitad+1, fin)
        if comp == level:
            return mitad+1

n = int(input())
enemigos = input().split()
m = int(input())
suma = []
sum = 0

for j in range(n):
    sum += int(enemigos[j])
    suma.append(sum)
i = []
total = []

for h in range(m):
    lv = int(input(''))
    i.append(Astora(enemigos, lv, 0, n-1))

for a in range(m):
    if i[a] == 0:
        print(0, 0)
    else:
        print(i[a], suma[i[a]-1])