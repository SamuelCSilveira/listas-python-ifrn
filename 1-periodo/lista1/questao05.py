"""Exercício 5:
Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o 
valor do percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo 
salário (variável NS).
"""

sm = float(input("Digite o valor do salário mensal: "))
pr = float(input("Digite o valor do percentual de reajuste do salário: "))
ns = sm + ((pr/100) * sm)

print(f"O valor do novo salário é de: R${ns}")