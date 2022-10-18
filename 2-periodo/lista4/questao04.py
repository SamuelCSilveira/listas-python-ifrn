"""Exercício 4:
Crie uma função que recebe um número entre 1 e 7 e imprime o dia da semana. Considere: 1/domingo, 2/segunda, 3/terça... 7/sábado. Se o valor não estiver no intervalo, informar que é inválido.
"""

def dia(n):
    if n == 1:
        print("Domingo")
    elif n == 2:
        print("Segunda-feira")
    elif n == 3:
        print("Terça-feira")
    elif n == 4:
        print("Quarta-feira")
    elif n == 5:
        print("Quinta-feira")
    elif n == 6:
        print("Sexta-feira")
    elif n == 7:
        print("Sábado")
    else:
        print("Número inválido")

dia(int(input("Digite um número de 1 a 7: ")))