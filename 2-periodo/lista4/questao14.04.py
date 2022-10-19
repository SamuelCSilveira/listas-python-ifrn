"""Exercício 14.4:
Crie uma função que recebe um número entre 1 e 7 e imprime o dia da semana. Considere: 1/domingo, 2/segunda, 3/terça... 7/sábado. Se o valor não estiver no intervalo, informar que é inválido.
"""

def dia(n):
    if n == 1:
        return "Domingo"
    elif n == 2:
        return "Segunda-feira"
    elif n == 3:
       return "Terça-feira"
    elif n == 4:
        return "Quarta-feira"
    elif n == 5:
        return "Quinta-feira"
    elif n == 6:
        return "Sexta-feira"
    elif n == 7:
        return "Sábado"
    else:
        return "Número inválido"

resultado = dia(int(input("Digite um número de 1 a 7: ")))
print(resultado)