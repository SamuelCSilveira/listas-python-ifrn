"""Exercício 10: 
Crie um programa em que o usuário digite 10 valores em uma lista. Ao final o programa deve informar o maior e o menor valor digitado e suas posições na lista."""

lista = []
valor = int(input("Digite um valor: "))
lista.append(valor)
menor = valor
maior = valor

for i in range(9):
  valor = int(input("Digite um valor: "))
  lista.append(valor)
  
  if maior < valor:
    maior = valor
  if menor > valor:
    menor = valor

print(f"\nMaior: {maior}")
print(f"Índice: {lista.index(maior)}")

print(f"\nMenor: {menor}")
print(f"Índice: {lista.index(menor)}")