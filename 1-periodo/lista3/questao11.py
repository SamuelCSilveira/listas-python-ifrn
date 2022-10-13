"""Exercício 11:
Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário."""

maior = 0
val = int(input("Digite um número inteiro: "))
menor = val

while val >= 0:
  if menor > val:
    menor = val
  if maior < val:
    maior = val
  val = int(input("Digite um número inteiro: "))

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")