"""Exercício 4:
Crie um programa que pergunta quantos alunos participam de uma classe. Use um laço for para solicitar a digitação do nome e da nota para cada aluno, armazenando tudo em uma lista. Após a digitação, percorra a lista (usando um laço for) e imprima frases com o nome, nota e resultado do aluno, de acordo com as regras abaixo.

De 60 a 100 – aprovado.
De 40 a 59 – em recuperação.
Abaixo de 40 – reprovado.

Veja o exemplo de saída:
João tem média 100 e está aprovado.
Maria tem média 50 e está em recuperação.
Carlos tem média 30 e está reprovado.
"""

quantidade = int(input("Digite a quantidade de alunos da classe: "))
alunos = []

for i in range(quantidade):
  nome = input(f"Digite o nome do {i+1}° aluno: ")
  nota = int(input(f"Digite a nota do {i+1}° aluno: "))
  if nota < 40:
    situacao = "reprovado."
  elif nota < 60:
    situacao = "em recuperação."
  else:
    situacao = "aprovado."
  alunos.append([nome, nota, situacao])

for i in alunos:
  print(f"{i[0]} tem média {i[1]} e está {i[2]}")