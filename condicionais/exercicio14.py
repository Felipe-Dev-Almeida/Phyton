# Faça um programa receba dois valores e imprima qual é o maior número digitado.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)

elif numero2 > numero1:
    print("O maior número é:", numero2)

else:
    print("Os dois números são iguais.")