inN = int(input('Introduce un número: '))
d = [500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in d:
    n = inN // i
    if n >= 1:
        if i > 2:
            if n == 1: print(n, "billete de", i, "euros")
            else: print(n, "billetes de", i, "euros")
        else:
            if n == 1: print(n, "moneda de", i, "euros")
            else: print(n, "monedas de", i, "euros")
        inN = inN - i * n