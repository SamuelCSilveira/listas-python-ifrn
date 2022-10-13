"""Exercício 9:
Modifique o programa 8 para que o usuário digite dois valores na pesquisa. O programa percorre a lista procurando os dois ao mesmo tempo e diz qual dos dois valores foi encontrado primeiro (mais próximo do início da lista). Dica: use um intervalo de sorteio pequeno, com números entre 1 e 10, por exemplo."""

import random

lista = []

for i in range(10):
  num = random.randint(0, 100)
  lista.append(num)
  
while True:
  pesquisa1 = int(input("Digite um número de 1 a 100 para pesquisar: "))
  pesquisa2 = int(input("Digite um número de 1 a 100 para pesquisar: "))

  for valor in lista:
    if pesquisa1 == valor:
      print(f"Valor {pesquisa1} encontrado no índice {lista.index(pesquisa1)}\n")
      break
    elif pesquisa2 == valor:
      print(f"Valor {pesquisa2} encontrado no índice {lista.index(pesquisa2)}\n")
      break
  else:
    print("Os números escolhidos não foram encontrados na lista.\n")