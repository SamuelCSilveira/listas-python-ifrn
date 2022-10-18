"""Exercício 4:
Digite as notas de uma prova para uma turma de 10 alunos e calcule a média da turma. Dica: use uma variável para acumular a soma de todas as notas, por último, já fora do laço, faça a divisão para calcular a média.
"""

soma = 0

for i in range(10):
    nota = int(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / 10
print(f"A média de notas da turma é {media}.")