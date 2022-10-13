"""Exercício 4:
Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando se o número é par ou ímpar.
"""

x = int(input("Digite um número inteiro: "))

if x % 2 == 0:
  print("O número é par.")

else:
  print("O número é ímpar.")