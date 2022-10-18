"""Exercício 6:
Crie uma função que recebe um número e diz se ele é primo.
"""

def primo(n):
    cont = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            cont += 1
    if cont > 2:
        print(f"O número {n} não é primo.")
    else:
        print(f"O número {n} é primo.")

primo(int(input("Digite um valor inteiro para saber se é primo: ")))