"""Exercício 3:
Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente.
"""

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a < b and b < c:
  print(a)
  print(b)
  print(c)

if a < c and c < b:
  print(a)
  print(c)
  print(b)

if b < a and a < c:
  print(b)
  print(a)
  print(c)

if b < c and c < a:
  print(b)
  print(c)
  print(a)

if c < a and a < b:
  print(c)
  print(a)
  print(b)

if c < b and b < a:
  print(c)
  print(b)
  print(a)