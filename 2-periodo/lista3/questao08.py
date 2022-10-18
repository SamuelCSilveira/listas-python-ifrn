"""Exercício 08:
Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., etc. Esta série se caracteriza pela soma de um termo atual com o seu anterior subsequente, para que seja formado o próximo valor da sequência. Portanto começando com os números 1, 1 o próximo termo é 1+1=2, o próximo é 1+2=3, o próximo é 2+3=5, o próximo 3+5=8, etc."""

fibonacci = 0
ant1 = 1
ant2 = 0
cont = 0

for i in range(15):
  if fibonacci < 1:
    fibonacci = ant1
  else:
    fibonacci = ant1 + ant2
    ant2 = ant1
    ant1 = fibonacci
  print(fibonacci)