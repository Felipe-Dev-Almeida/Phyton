# operadores lógicos
# and - ambas as expressões devem retornar verdadeiras
# or - basta apenas uma das expressões retornar verdadeira
# not inverte o resultado da expressões lógica

idade = int(input("Qual é sua idade?"))
ingresso = input("Você tem ingresso? s/n")

# conjugar com o operador and
if idade >= 18 or ingresso == "s" :
    print("Seja bem-vindo a festa🥳")
else :
    print("Você não pode entar na festa")