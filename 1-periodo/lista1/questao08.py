"""Exercício 8:
Digite as notas de um aluno para os 4 bimestres do ano e calcule a sua média ponderada. 
Os pesos para cada bimestre são, respectivamente: 2, 3, 4, 6.   
"""

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 6)) / 15

print(f"A média ponderada é {media : .1f}")