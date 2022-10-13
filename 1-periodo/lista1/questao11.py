"""Exercício 11:
Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma 
comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. Elabore um 
algoritmo para calcular e imprimir o salário do vendedor num dado mês recebendo como dados 
de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas.    
"""

nome = input("Digite o nome do vendedor: ")
num_carros = int(input("Digite o número de carros vendidos: "))
total_vendas = float(input("Digite o valor total das vendas do vendedor: "))

comissao = num_carros * 50
porcentagem = total_vendas * 0.05

salario = 500 + comissao + porcentagem

print(f"Salário de {nome}:")
print("Base: R$ 500,00")
print(f"Comissão: R${comissao : .2f}")
print(f"Porcentagem de vendas: R${porcentagem : .2f}")
print(f"Total: R${salario : .2f}")