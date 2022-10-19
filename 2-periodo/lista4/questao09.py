"""Exercício 9:
Crie uma função que imprime a sequência numérica indo de 1 até o número informado. Ex. sequencia(6) imprime 1, 2, 3, 4, 5, 6.
"""

def sequencia(n):
    for i in range(1, n+1):
        print(i)

numero = int(input("Digite um valor: "))
sequencia(numero)