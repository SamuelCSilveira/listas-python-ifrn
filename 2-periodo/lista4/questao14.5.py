"""Exercício 14.5:
Crie uma função que recebe um número entre 1 e 12 e imprime o mês do ano. Considere: 1/janeiro, 2/fevereiro, ... 12/dezembro. Se o valor não estiver no intervalo, informar que é inválido.
"""

def mes(n):
    if n == 1:
        return "Janeiro"
    elif n == 2:
        return "Fevereiro"
    elif n == 3:
        return "Março"
    elif n == 4:
        return "Abril"
    elif n == 5:
        return "Maio"
    elif n == 6:
        return "Junho"
    elif n == 7:
        return "Julho"
    elif n == 8:
        return "Agosto"
    elif n == 9:
        return "Setembro"
    elif n == 10:
        return "Outubro"
    elif n == 11:
        return "Novembro"
    elif n == 12:
        return "Dezembro"
    else:
        return "Número inválido"

resultado = mes(int(input("Digite um número de 1 a 12: ")))
print(resultado)