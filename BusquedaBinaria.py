def bBin(x, vec, ini, fin):
    if fin == ini:
        return x == vec[ini]
    else:
        b = int((fin+ini)/2)
        if x == vec[b]:
            return True
        if x > vec[b]:
            return bBin(x, vec, b+1, fin)
        else:
            return bBin(x, vec, ini, b-1)



a = [1, 2, 3, 4, 5, 6, 7, 8, 10, 34, 67, 80, 192, 500]
elem = int(input('Introduce un elemento: '))
if bBin(elem, a, 0, len(a)-1):
    print(elem, 'está contenido en el vector')
else:
    print(elem, 'no está en el vector')