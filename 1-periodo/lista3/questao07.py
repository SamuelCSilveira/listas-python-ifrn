"""Exercício 07:
Escreva um programa que pergunta o valor inicial de uma dívida, a taxa mensal de juros e o valor que será pago a cada mês. Informe o número de meses necessários para quitar a dívida, o total pago e quanto de juros foi pago."""

divida = float(input("Digite o valor inicial da dívida: "))
taxa = float(input("Digite o valor da taxa mensal de juros: "))
abatimento = float(input("Digite o valor a ser pago a cada mês: "))
juros = divida * taxa / 100

if juros >= abatimento:
  print("\nValor pago mensalmente é insuficiente para cobrir os juros!")

else:
  meses = 0
  totjuros = 0
  totpago = divida

  while divida > 0:
    juros = divida * taxa / 100
    divida = divida + juros - abatimento
    meses += 1
    totjuros += juros


  totpago += totjuros

  print(f"\nNúmero de meses para quitar a dívida: {meses} meses")
  print(f"Total pago: R${totpago : .2f}")
  print(f"Total de juros: R${totjuros : .2f}")