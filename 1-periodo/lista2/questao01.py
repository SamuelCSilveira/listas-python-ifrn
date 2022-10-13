"""Exercício 1:
Ler quatro notas de um aluno, calcular a média aritmética e imprimir a média e uma mensagem dizendo que o aluno foi aprovado, se a média for maior ou igual a 6, ou reprovado para uma nota abaixo de 6.
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média é de{media: .1f}.")

if media >= 6:
  print("Você está aprovado.")

else:
  print("Você está reprovado.")