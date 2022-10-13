"""Exercício 11:
Faça um programa que leia a idade de um atleta e informa a qual categoria ele pertence:

Até 8 anos   Até 11 anos   Até 14 anos   Até 17 anos   18 ou mais
pré-mirim    mirim         infantil      juvenil       adulto
"""

idade = int(input("Digite a idade do atleta: "))

if idade >= 18:
  print("O atleta é da categoria adulto.")

elif idade > 14:
  print("O atleta é da categoria juvenil.")

elif idade > 11:
  print("O atleta é da categoria infantil.")

elif idade > 8:
  print("O atleta é da categoria mirim.")

else:
  print("O atleta é da categoria pré-mirim.")