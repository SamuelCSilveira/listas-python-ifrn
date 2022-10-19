"""Exercício 8:
Crie uma função que recebe um número e imprime um intervalo com seus 10 primeiros múltiplos.
"""

def multiplos(n):
    for i in range(10):
        print(n * (i+1))

numero = int(input("Digite um valor: "))
multiplos(numero)