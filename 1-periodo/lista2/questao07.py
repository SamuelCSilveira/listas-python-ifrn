"""Exercício 7:
Informe a altura e o sexo de uma pessoa e calcule o peso ideal, utilizando as seguintes fórmulas: Para homens: (72*altura)-58. Para mulheres: (62.1*altura)-44.7
"""

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M ou F): ")

if sexo == 'M' or sexo == 'm':
  peso = (72 * altura) - 58
  print(f"Seu peso ideal é de {peso: .1f}kg.")

elif sexo == 'F' or sexo == 'f':
  peso = (62.1 * altura) - 44.7
  print(f"Seu peso ideal é de {peso: .1f}kg.")

else:
  print("Sexo inválido.")