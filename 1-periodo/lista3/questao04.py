"""Exercício 4:
Digite as notas de uma prova para uma turma de 10 alunos e calcule a média da turma. Dica: use uma variável para acumular a soma de todas as notas, por último, já fora do laço, faça a divisão para calcular a média."""

cont = 0
soma = 0

while cont < 10:
  valor = float(input(f"Digite a nota do aluno {cont+1}: "))
  soma += valor
  cont += 1

media = soma/cont
print(f"A média das notas dos alunos é {media}.")