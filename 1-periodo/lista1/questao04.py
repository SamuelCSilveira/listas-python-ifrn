"""Exercício 4:
Elaborar um programa que calcule e apresente o volume de uma caixa retangular, por meio 
da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
"""

comprimento = float(input("Digite o comprimento da caixa retangular (em m): "))
largura = float(input("Digite o largura da caixa retangular (em m): "))
altura = float(input("Digite o altura da caixa retangular (em m): "))
volume = comprimento * largura * altura

print(f"O volume da caixa retangular é: {volume} m³")