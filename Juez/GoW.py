def level(ene, lvl, ini, fin):
    if ini >= fin:
        c = int(ene[ini])
        if c > lvl:
            return [ini-1, ini]
        if c < lvl:
            return [ini, ini+1]
        else:
            return [ini-1, ini+1]
    else :
        mitad = int((ini+fin)/2)
        comp = int(ene[mitad])
        if comp > lvl:
            return level(ene, lvl, ini, mitad-1)
        if comp < lvl:
            return level(ene, lvl, mitad+1, fin)
        if comp == lvl:
            return [mitad-1, mitad+1]

n = int(input())
enemigos = input().split()
q = int(input())
levels = input().split()

for i in range (q):
    jl = level(enemigos, int(levels[i]), 0, n-1)
    if jl[1] > n - 1 and jl[0] < 0:
        print('X', 'X')
    elif jl[0] < 0:
        print('X', enemigos[jl[1]])
    elif jl[1] > n-1:
        print(enemigos[jl[0]], 'X')
    else:
        print(enemigos[jl[0]], enemigos[jl[1]])