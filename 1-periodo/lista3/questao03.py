"""Exercício 3:
Crie um programa em que o usuário digite 10 números e o programa apresente a soma desses
números. Dica: use uma variável para acumular a soma dos números, como no exemplo: soma =
soma + numero."""

cont = 0
soma = 0

while cont < 10:
  valor = int(input("Digite um valor para a soma: "))
  soma += valor
  cont += 1

print(f"O valor da soma é {soma}.")