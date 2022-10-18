"""Exercício 3:
Crie um programa em que o usuário digite 10 números e o programa apresente a soma desses números. Dica: use uma variável para acumular a soma dos números, como no exemplo: soma = soma + numero.
"""

soma = 0

for i in range(10):
    numero = int(input("Digite um valor: "))
    soma += numero

print(f"O valor da soma é {soma}.")