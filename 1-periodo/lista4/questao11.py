"""Exercício 11:
Crie um programa que o usuário digite as notas de 10 alunos de uma turma. Depois calcule e imprima a média das notas, a maior e a menor nota."""

notas = []
menor = 10
maior = 0
media = 0

for i in range(10):
  nota = float(input(f"A nota do aluno {i+1}: "))
  notas.append(nota)
  
  if maior < nota:
    maior = nota
  if menor > nota:
    menor = nota

  media += nota/10



print(f"\nMédia: {media: .1f}")
print(f"Maior: {maior: .1f}")
print(f"Menor: {menor: .1f}")