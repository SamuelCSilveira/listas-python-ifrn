"""Exercício 3: 
Crie uma função que solicita a digitação de 2 valores e exibe o resultado das 4 operações (+, -, *, /).
"""

def operacoes():
    v1 = float(input("Digite um valor: "))
    v2 = float(input("Digite outro valor: "))
    print(f"{v1} + {v2} = {v1+v2}")
    print(f"{v1} - {v2} = {v1-v2}")
    print(f"{v1} * {v2} = {v1*v2}")
    print(f"{v1} / {v2} = {v1/v2}")

operacoes()