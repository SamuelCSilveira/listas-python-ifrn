"""Exercício 7:
Crie uma função que recebe dois valores e imprime qual deles é o maior ou diz se são iguais.
"""

def iguais(v1, v2):
    if v1 == v2:
        print("Os valores são iguais.")
    else:
        print("Os valores não são iguais.")

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

iguais(valor1, valor2)