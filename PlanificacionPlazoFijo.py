#Generar datos
def generarDatos():
    #Inicializamos una lista de datos que van del 1 al 5
    datos = {}
    datos['trabajos'] = list(range(1,6))
    datos['f'] = [2, 1, 3, 2, 1]
    datos['b'] = [60, 100, 20, 40, 20]
    return datos

#Inicializar la sol
def inicializarSolucion(datos):
    sol = {}
    sol['numAsignados'] = 0 # numero de trabajos asignados
    fechaMax = max(datos['f'])
    sol['trabajos'] = [0] * fechaMax # id del índice
    sol['f'] = [0] * fechaMax
    sol['b'] = [0] * fechaMax
    return sol

def seleccionar(datos):
    # hay una funcion que te busca un indice que cumpla x caracteristica
    select = {}
    candidatoMax = datos['b'][0]
    indiceMax = 0
    for i in range(1, len(datos['b'])):
        if datos['b'][i] > candidatoMax:
            candidatosMax = datos['b'][i]
            indiceMax = i
    select['b'] = datos['b'][indiceMax]
    select['f'] = datos['f'][indiceMax]
    select['trabajos'] = datos['trabajos'][indiceMax]
    del datos['b'][indiceMax]
    del datos['f'][indiceMax]
    del datos['trabajos'][indiceMax]
    return select, datos

def esFactible(select, sol):
    find = False
    idx = select['f'] - 1
    while not find and idx >= 0:
        if sol['trabajos'][idx] == 0:
            find = True
            return idx
        else:
            idx -= 1
    return idx

def addSol(select, sol, idx):
    sol['trabajos'][idx] = select['trabajos']
    sol['b'][idx] = select['b']
    sol['f'][idx] = select['f']
    sol['numAsignados'] += 1
    return sol

#Vamos al voraz
def tareasVoraz(datos):
    #Inicializamos una solución, en cada iteración del voraz se rellenará como la mejor sol local posible
    solu = inicializarSolucion(datos)
    fechaMax = max(datos['f'])
    while solu['numAsignados'] < fechaMax:
        [select, datos] = seleccionar(datos)
        idx = esFactible(select, solu)
        if idx > -1:
            solu = addSol(select, solu, idx)
    return solu

#Programa principal
datos = generarDatos()
solucion = tareasVoraz(datos)
print('La solucion es: ')
print(solucion)