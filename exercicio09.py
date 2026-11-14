# Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a
# 500 reais. Escreva um programa que receba o salário de um funcionário e imprima o
# valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a aumento.

salario = float(input("Digite o salário do funcionário: R$ "))

if salario < 500:
    salario = salario + (salario * 0.30)
    print("O funcionário recebeu um aumento de 30%.")
    print("Salário reajustado: R$", salario)

else:
    print("O funcionário não tem direito ao aumento.")