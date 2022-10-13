"""Exercício 3:
Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a 
troca dos valores de forma que a variável A passe a possuir o valor da variável B e a 
variável B passe a possuir o valor da variável A. Apresentar os valores trocados.
"""



a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

valora = a
valorb = b

b = valora
a = valorb

# Uma outra forma de realizar é utilizando tuplas: a, b = b, a

print(f"Valor de A: {a}")
print(f"Valor de B: {b}")