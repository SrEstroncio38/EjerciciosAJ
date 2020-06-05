N = int(input().strip())

particulas = []

for i in range(N):
    a = input()
    particulas.append([len(a),a])

particulas.sort(reverse=True)

letras = ''
letra = ''

particula = particulas[0]
for a in range (len(particula[1])):
    letra += particula[1][a]
    estaEnTodas = True
    for j in range(N):
        if letra not in particulas[j][1]:
            estaEnTodas = False
            break
    if estaEnTodas and len(letra) > len(letras):
        letras = letra

print(letras)



