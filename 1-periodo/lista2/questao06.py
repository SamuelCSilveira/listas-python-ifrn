"""Exercício 6:
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumidas e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

Tipo           Faixa (kWh)       Preço
Residêncial    Até 500           R$ 0,40
               Acima de 500      R$ 0,65
Comercial      Até 1000          R$ 0,55   
               Acima de 1000     R$ 0,60
Industrial     Até 5000          R$ 0,55
               Acima de 5000     R$ 0,60
"""

consumido = float(input("Digite o consumo em kWh: "))
tipo = input("Digite o tipo de instalação: ")

if tipo == 'R' or tipo == 'r':
  if consumido <= 500:
    valor = consumido * 0.40
    print(f"O preço a pagar será: R${valor: .2f}")
  else:
    valor = consumido * 0.65
    print(f"O preço a pagar será: R${valor: .2f}")

elif tipo == 'C' or tipo == 'c':
  if consumido <= 1000:
    valor = consumido * 0.55
    print(f"O preço a pagar será: R${valor: .2f}")
  else:
    valor = consumido * 0.60
    print(f"O preço a pagar será: R${valor: .2f}")

elif tipo == 'I' or tipo == 'i':
  if consumido <= 5000:
    valor = consumido * 0.55
    print(f"O preço a pagar será: R${valor: .2f}")
  else:
    valor = consumido * 0.60
    print(f"O preço a pagar será: R${valor: .2f}")

else:
  print("Tipo de instalação inválido.")