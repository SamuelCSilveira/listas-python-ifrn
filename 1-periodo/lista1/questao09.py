"""Exercício 9:
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem 
do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. Supondo que a 
porcentagem do distribuidor seja de 12% e a dos impostos de 45%, prepare um algoritmo 
para ler o custo de fábrica do carro e imprimir o custo ao consumidor.
"""

custo_fabrica = float(input("Digite o custo de fábrica do veículo: "))

distribuidor = custo_fabrica * 0.12
impostos = custo_fabrica * 0.45
custo_consumidor = custo_fabrica + distribuidor + impostos

print(f"O custo do carro ao consumidor será de: R${custo_consumidor : .2f}")