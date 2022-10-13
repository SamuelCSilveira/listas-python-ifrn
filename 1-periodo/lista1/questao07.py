"""Exercício 7:
Digite as notas de um aluno para os 4 bimestres do ano e calcule a sua média aritmética.
"""

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média aritmética é {media : .1f}")