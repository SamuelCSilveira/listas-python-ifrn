"""Exercício 2:
Modifique o programa anterior de maneira que o usuário também digite o início e o fim da tabuada, ao invés de ir de 1 a 10. Ex. Tabuada de: 2, início: 5, fim: 12. Vai imprimir: 2 x 5 = 10, 2 x 6 = 12, ... 2 x 12 = 24.
"""

numero = int(input("Digite um número para calcular a tabuada: "))
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

for i in range(inicio-1, fim):
    tabuada = numero * (i + 1)
    print(f"{numero} x {i + 1} = {tabuada}")