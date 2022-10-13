"""Exercício 3:
Crie um programa que sorteie 10 números entre 1 e 100 e guarde-os numa lista. Ordene a lista em ordem crescente e imprima na tela os valores sorteados."""

from random import randint

lista = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
print(lista)