"""Exercício 2:
Crie um programa em que o usuário digite 10 valores em uma lista e depois imprima a lista."""

lista = []

for i in range(10):
  lista.append(input("Digite um valor: "))

print(lista)