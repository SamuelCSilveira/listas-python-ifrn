"""Exercício 6:
Escreva um programa que pergunta o valor de depósito inicial para uma poupança, e a taxa de rendimento mensal. Apresente o saldo dos próximos 24 meses, considerando o rendimento sobre o saldo atual de cada mês.
"""

saldo = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite a taxa de rendimento mensal: "))

for mes in range(24):
  rendimento = saldo * taxa / 100
  saldo += rendimento
  print(f"\nMês {mes+1}:")
  print(f"Rendimento mensal: R${rendimento : .2f}")
  print(f"Saldo atual: R${saldo : .2f}")