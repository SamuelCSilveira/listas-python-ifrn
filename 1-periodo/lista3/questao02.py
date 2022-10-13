"""Exercício 2:
Modifique o programa anterior de maneira que o usuário também digite o início e o fim da
tabuada, ao invés de ir de 1 a 10. Ex. Tabuada de: 2, início: 5, fim: 12. Vai imprimir: 2 x 5 = 10, 2 x 6 = 12, ... 2 x 12 = 24."""

num = int(input("Digite um número de 1 a 9: "))
cont = int(input("Digite um número para iniciar a tabuada: "))
fim = int(input("Digite um número para terminar a tabuada: "))


while cont <= fim:
  print(num, 'x', cont, '=', num * cont)
  cont += 1