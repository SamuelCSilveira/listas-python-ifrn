"""Exercício 1:
Crie um programa que imprime a tabuada de um número digitado pelo usuário. Ex. Usuário digitou "2", o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ...
"""

numero = int(input("Digite um número para calcular a tabuada: "))

for i in range(10):
    tabuada = numero * (i + 1)
    print(f"{numero} x {i + 1} = {tabuada}")