"""Exercício 5:
Crie uma função que recebe um número entre 1 e 12 e imprime o mês do ano. Considere: 1/janeiro, 2/fevereiro, ... 12/dezembro. Se o valor não estiver no intervalo, informar que é inválido.
"""

def mes(n):
    if n == 1:
        print("Janeiro")
    elif n == 2:
        print("Fevereiro")
    elif n == 3:
        print("Março")
    elif n == 4:
        print("Abril")
    elif n == 5:
        print("Maio")
    elif n == 6:
        print("Junho")
    elif n == 7:
        print("Julho")
    elif n == 8:
        print("Agosto")
    elif n == 9:
        print("Setembro")
    elif n == 10:
        print("Outubro")
    elif n == 11:
        print("Novembro")
    elif n == 12:
        print("Dezembro")
    else:
        print("Número inválido")

mes(int(input("Digite um número de 1 a 12: ")))