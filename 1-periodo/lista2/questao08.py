"""Exercício 8:
Numa cidade litorânea há lei municipal que permite a produção de 50 Kg de pescados por dia. Sempre que um pescador chega à praia, um fiscal pesa os peixes e aplica uma multa de R$ 4,00 por cada Kg excedente. Faça um programa que leia o peso e informe o valor da multa, caso ultrapasse o peso permitido.
"""

peso = float(input("Digite o peso dos pescados: "))

if peso > 50:
  excedente = peso - 50
  multa = 4 * excedente
  print(f"O valor da multa será de R${multa: .2f}")

else:
  print("Esta produção não incidirá em multa.")