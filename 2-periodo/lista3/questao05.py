"""Exercício 5:
Faça um programa que calcula a potência a partir de dois valores digitados pelo usuário. Não use o operador de potência, faça apenas multiplicações. Se o usuário digitar: base = 2, expoente = 3, o programa deve repetir a multiplicação 2 x 2 x 2 para obter o resultado.
"""

base = float(input("Digite o valor da base da potência: "))
expoente = int(input("Digite o valor do expoente da potência: "))
potencia = base

for i in range(expoente-1):
    potencia *= base

print(f"O resultado da potência é {potencia}")