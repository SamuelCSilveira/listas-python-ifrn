"""Exercício 16:
Modifique o programa anterior para que ele também possa gerar sequências decrescentes. O programa deve identificar automaticamente se é uma sequência crescente ou decrescente. Ex.: Se o usuário digitar 1 e 5, ele vai imprimir: 1, 2, 3, 4, 5. Se o usuário digitar 5 e 1, ele vai imprimir: 5, 4, 3, 2, 1.
"""

inicial = int(input("Digite o número inicial da sequência: "))
final = int(input("Digite o número final da sequência: "))
if inicial <= final:
  sequencia = list(range(inicial, final+1))
else:
  sequencia = list(range(inicial, final-1, -1))
print(sequencia)