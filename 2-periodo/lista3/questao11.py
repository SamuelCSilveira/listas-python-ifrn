"""Exercício 11:
Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo usuário."""

maior = 0
val = int(input("Digite um número inteiro: "))
menor = val

for i in range(1000):
  if menor > val:
    menor = val
  if maior < val:
    maior = val
  val = int(input("Digite um número inteiro: "))
  if val < 0:
    break

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")