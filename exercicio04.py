#. Receba nome, peso e altura. Calcule IMC.

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura ** 2)

print(f"O seu IMC é: {IMC}")