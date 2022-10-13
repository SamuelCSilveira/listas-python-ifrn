"""Exercício 6:
Em uma eleição sindical concorreram ao cargo de presidente três candidatos (A, B e C). 
Durante a apuração dos votos foram computados votos nulos e votos em branco, além dos 
votos válidos para cada candidato. Deve ser criado um programa de computador que efetue 
a leitura da quantidade de votos válidos para cada candidato, além de efetuar também a 
leitura da quantidade de votos nulos e votos em branco. Ao final o programa deve 
apresentar o número total de eleitores, considerando votos válidos, nulos e em branco; 
o percentual correspondente de votos válidos em relação à quantidade de eleitores; o 
percentual correspondente de votos válidos de cada candidato em relação à quantidade de 
eleitores, além do percentual de votos brancos e votos nulos;
"""

candidatoA = int(input("Digite a quantidade de votos no candidato A: "))
candidatoB = int(input("Digite a quantidade de votos no candidato B: "))
candidatoC = int(input("Digite a quantidade de votos no candidato C: "))
branco = int(input("Digite a quantidade de votos em branco: "))
nulo = int(input("Digite a quantidade de votos nulos: "))

total_de_eleitores = candidatoA + candidatoB + candidatoC + branco + nulo

perc_validos = ((candidatoA + candidatoB + candidatoC) / total_de_eleitores) * 100
perc_A = (candidatoA / total_de_eleitores) * 100
perc_B = (candidatoB / total_de_eleitores) * 100
perc_C = (candidatoC / total_de_eleitores) * 100
perc_invalidos = ((branco + nulo) / total_de_eleitores) * 100

print(f"Número total de eleitores: {total_de_eleitores} eleitores")
print(f"Percentual de votos válidos: {perc_validos : .1f}%")
print(f"Percentual de votos do candidato A: {perc_A : .1f}%")
print(f"Percentual de votos do candidato B: {perc_B : .1f}%")
print(f"Percentual de votos do candidato C: {perc_C : .1f}%")
print(f"Percentual de votos brancos e nulos: {perc_invalidos : .1f}%")