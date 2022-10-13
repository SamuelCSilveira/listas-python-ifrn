"""Exercício 1:
Crie um programa que imprime a tabuada de um número digitado pelo usuário. Ex. Usuário
digitou "2", o programa imprime: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6 ..."""

num = int(input("Digite um número de 1 a 9: "))
x = 1

while x <= 10:
  print(num, 'x', x, '=', num * x)
  x += 1