"""Exercício 17:
Crie um programa que pede ao usuário para digitar: o número inicial de uma sequência, o número final de uma sequência, o incremento da sequência. Imprima a sequência desejada. Obs.: O programa deve detectar se a sequencia é crescente ou decrescente e fazer o incremento (positivo ou negativo) corretamente. Ex.: Se o usuário digitar 10 (ini.), 4 (fim), 2 (incr.), o programa deve imprimir: 10, 8, 6, 4, mesmo tendo digitado um incremento positivo.
"""

inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
incremento = int(input("Digite o valor de incremento da sequência: "))
if inicial <= final:
  sequencia = list(range(inicial, final+1, incremento))
else:
  sequencia = list(range(inicial, final-1, -incremento))
print(sequencia)