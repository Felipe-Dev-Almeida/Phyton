 #Faça um programa que receba o nome, cargo e salário de um funcionário. Se o
# funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final
# exiba o nome, o cargo e o salário desse funcionário.

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: R$ "))

if salario < 1000:
    salario = salario + (salario * 0.10)
    print("O funcionário recebeu um aumento de 10%.")

else:
    print("O funcionário não recebeu aumento.")

print("\n===== DADOS DO FUNCIONÁRIO =====")
print("Nome:", nome)
print("Cargo:", cargo)
print("Salário: R$", salario)