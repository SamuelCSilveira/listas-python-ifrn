"""Exercício 15:
Crie um programa que pede ao usuário para digitar: o número inicial de uma sequência (menor valor), o número final de uma sequência (maior valor). Imprima a sequência desejada.
"""

inicial = int(input("Digite o número inicial da sequência: "))
final = int(input("Digite o número final da sequência: ")) + 1
sequencia = list(range(inicial, final))
print(sequencia)