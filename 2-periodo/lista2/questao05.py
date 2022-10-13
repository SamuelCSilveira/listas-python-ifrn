"""Exercício 5:
Crie um programa utiliza dois laços for encadeados para que sortear combinações para a loteria. Pergunte ao usuário quantos “jogos” ele deseja fazer. Para cada “jogo” o programa sorteia 6 números entre 1 e 60. Dica: use a biblioteca random e a função randint para sortear os números.
EXTRA: Pesquise como usar a função sample da biblioteca random para evitar repetições de números no mesmo jogo.
"""

import random

quantidade = int(input("Digite o número de jogos que deseja fazer: "))
jogos = []
numeros = []

for i in range(60):
  numeros.append(i+1)

for i in range(quantidade):
#  jogo = []
#  for n in range(6):
#    jogo.append(random.randint(1, 60))
#  jogos.append(jogo)                     # Utilizando a função randint
  jogos.append(random.sample(numeros, 6)) # Utilizando a função sample

print(jogos)