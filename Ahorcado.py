def Actualizar(letra, palabra, oldBlankWord):
    newBlankWord = ''
    for i in range(len(oldBlankWord)):
        if (letra == palabra[i]):
            newBlankWord += palabra[i]
        else:
            newBlankWord += oldBlankWord[i]
    return newBlankWord

word = input('Introduce la palabra a adivinar jugador A: ').lower()
blankWord= '*'* len(word)
print('La palabra oculta tiene ', len(word),' letras', blankWord)
fin = False
intentos = 5
while (not fin and intentos > 0):
    letraUser = input('Introduce una letra: ').lower()
    if letraUser in word:
        blankWord = Actualizar(letraUser, word, blankWord)
        print('Acertaste, introduce otra letra para', blankWord)
    else:
        print('Fallaste, introduce otra letra para', blankWord)
        intentos -= 1
    fin = blankWord == word

if fin:
    print('Has ganado, la palabra era:', blankWord)
else:
    print('Perdiste puto, la palabra era:', blankWord)