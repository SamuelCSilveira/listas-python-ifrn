"""Exercício 14.2:
Crie uma função que solicita a digitação de 2 valores e exibe o resultado da soma entre eles.
"""

def soma():
    v1 = float(input("Digite um valor: "))
    v2 = float(input("Digite outro valor: "))
    return v1 + v2
    

resultado = soma()
print(f"O valor da soma é {resultado}.")