"""Exercício 6:
Crie um programa que sorteie números aleatórios entre 1 e 100. Preencha uma lista com 20 elementos diferentes, organize em ordem decrescente e imprima na tela."""

import random

lista = []

for i in range(20):
  num = random.randint(1, 100)
  while num in lista:
    num = random.randint(1, 100)  
  lista.append(num)

lista.sort(reverse = True)
print(lista)