n = int(input(''))
media = 0
lista = {}
for i in range(n):
    m = int(input(''))
    media = media + m
    lista[i] = m

media = media // n
for i in lista:
    if lista[i] > media:
        print(lista[i])