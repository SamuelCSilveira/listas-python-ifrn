"""Exercício 10:
Escreva um programa que o usuário informa o valor do salário e o programa calcula o novo salário de acordo com as seguintes condições:

Até R$ 1000,00   Até R$ 2000,00   Até R$ 3000,00   Acima de R$ 3000,00
15%              10%              5%               2.5%
"""

salario = float(input("Digite o valor do seu salário: "))

if salario > 3000:
  novo_salario = salario * 1.025
  print(f"O seu novo salário será de R${novo_salario: .2f}")

elif salario > 2000:
  novo_salario = salario * 1.05
  print(f"O seu novo salário será de R${novo_salario: .2f}")

elif salario > 1000:
  novo_salario = salario * 1.1
  print(f"O seu novo salário será de R${novo_salario: .2f}")

else:
  novo_salario = salario * 1.15
  print(f"O seu novo salário será de R${novo_salario: .2f}")