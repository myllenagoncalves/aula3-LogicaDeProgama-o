#6. Faça um programa para verificar se um número é primo. Utilize a
# condicional IF dentro do laço FOR.

numero = int(input('Digite o numero: '))
contador = 0

for num in range(1, numero+1 ):
    if numero % num == 0:
        contador += 1
if contador > 2: 
    print("O numero não é primo.")
elif contador == 1:
    print("O numero 1 não é primo.")
else:
    print("O numero é primo.")