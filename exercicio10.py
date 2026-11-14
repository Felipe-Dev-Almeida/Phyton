# Elabore um programa para cálculo de preços de produtos que solicite o preço de
# compra do produto e o percentual a ser aplicado em cima desse valor para a venda.
# Calcule e exiba o preço de venda do produto. Se o percentual a ser aplicado for
# inferior a 50%, exiba uma mensagem informando ao usuário que o produto será
# vendido com uma margem muito pequena de lucro.

precocompra = float(input("Digite o preço de compra do produto: R$ "))
percentual = float(input("Digite o percentual de lucro desejado: "))

precovenda = precocompra + (precocompra * percentual / 100)

print("\n===== PREÇO DO PRODUTO =====")
print("Preço de compra: R$", precocompra)
print("Percentual aplicado:", percentual, "%")
print("Preço de venda: R$", precovenda)

if percentual < 50:
    print("Atenção: O produto será vendido com uma margem muito pequena de lucro.")

else:
    print("O produto possui uma margem de lucro adequada.")