 #Faça um programa que receba um número inteiro do usuário e informe se este
# número é positivo ou negativo.

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo.")

elif numero < 0:
    print("O número é negativo.")

else:
    print("O número é zero.")