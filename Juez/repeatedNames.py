n = int(input(''))
listaNombres = {}

for i in range(n):
    nombre = input('')
    if nombre in listaNombres:
        listaNombres[nombre] = listaNombres[nombre] + 1
    else:
        listaNombres[nombre] = 1

m = int(input(''))

for i in range(m):
    nombreP = input('')
    if nombreP in listaNombres:
        print(listaNombres[nombreP])
    else:
        print('NUEVO')

