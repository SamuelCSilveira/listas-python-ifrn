"""Exercício 9:
Uma empresa paga R$ 12,50 por hora trabalhada (até 40 horas) e 18,50 por hora extra. Leia o número de horas semanais de um funcionário e informe o valor do pagamento da semana.
"""

horas = float(input("Digite o número de horas semanais trabalhadas: "))

if horas > 40:
  pagamento = (40 * 12.5) + ((horas - 40) * 18.5)
  print(f"Seu pagamento será de R${pagamento: .2f}")
else:
  pagamento = horas * 12.5
  print(f"Seu pagamento será de R${pagamento: .2f}")