"""Exercício 1:
Crie um programa que use um laço for para solicitar a digitação do nome de 5 alunos. Após a digitação, exiba a lista.
"""

lista = []

for i in range(5):
  lista.append(input(f"Digite o nome do {i+1}° aluno: "))

print(lista)