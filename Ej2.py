from random import random

nOculto = (int(random()*1000))
print(nOculto)

f = True
while f:
    nPlayer = int(input('Introduce tu número: '))
    if nOculto == nPlayer:
        print('El número introducido es correcto')
        f = False
    else:
        if nOculto > nPlayer: print('El número oculto es mayor que el introducido')
        else: print('El número oculto es menor que el introducido')
