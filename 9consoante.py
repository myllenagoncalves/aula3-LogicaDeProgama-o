palavra = (input('Digite uma palavra: '))
contador = 0
for letra in palavra:
    if letra not in "aeiou":
        contador = contador + 1

print(contador)