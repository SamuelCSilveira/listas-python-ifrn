"""Exercício 2:
Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, 
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve
fornecer o tempo gasto (TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. 
Desta forma, será possível obter a distância percorrida com a fórmula 
DISTANCIA ← TEMPO * VELOCIDADE. Possuindo o valor da distância, basta calcular a 
quantidade de litros de combustível utilizada na viagem com a fórmula 
LITROS_USADOS ← DISTANCIA / 12. Ao final, o programa deve apresentar os valores da 
velocidade média (VELOCIDADE), tempo gasto na viagem (TEMPO), a distancia percorrida 
(DISTANCIA) e a quantidade de litros (LITROS_USADOS) utilizada na viagem.
"""

tempo = int(input("Digite o tempo gasto (em horas) na viagem: "))
velocidade = float(input("Digite a velócidade média (em km/h) durante a viagem: "))

distancia = tempo * velocidade
litros_usados = distancia / 12

print(f"Tempo de viagem: {tempo} horas")
print(f"Velocidade média: {velocidade} km/h")
print(f"Distância percorrida: {distancia} km")
print(f"Quantidade de litros usados: {litros_usados : .1f} litros")