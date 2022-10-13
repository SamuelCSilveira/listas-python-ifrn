"""Exercício 5:
Crie um programa que o usuário digita os dados de duas listas com 3 elementos cada. Depois crie uma terceira lista com a junção dos elementos das outras duas. Imprima a nova lista."""

lista1 = []
lista2 = []

for i in range(3):
  lista1.append(input(f"Digite o valor {i+1} da primeira lista: "))

for i in range(3):
  lista2.append(input(f"Digite o valor {i+1} da segunda lista: "))

lista3 = lista1 + lista2
print(lista3)