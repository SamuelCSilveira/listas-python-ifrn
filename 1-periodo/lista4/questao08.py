"""Exercício 8:
Crie um programa que sorteia 20 números e guarda-os numa lista. Permita que o usuário faça pesquisas na lista. Se o número pesquisado existe na lista, informe a sua posição. Se o elemento não existe, mostre uma mensagem informando. O usuário poderá repetir novas pesquisas quantas vezes quiser."""

import random

lista = []

for i in range(20):
  num = random.randint(0, 100)
  lista.append(num)

while True:
  pesquisa = int(input("Digite um número de 1 a 100 para pesquisar: "))

  if pesquisa in lista:
    print(f"O número escolhido está no índice {lista.index(pesquisa)}.\n")
  else:
    print("O número escolhido não está na lista.\n")