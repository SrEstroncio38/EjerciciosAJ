def Euclides(n, m):
    if n > m:
        if n % m != 0:
            Euclides(n % m, m)
        else:
            print('El mcd es', m)
    if n < m:
        if m % n != 0:
            Euclides(m % n, n)
        else:
            print('El mcd es', n)

Euclides(200, 7)