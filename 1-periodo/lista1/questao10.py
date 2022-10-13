"""Exercício 10:
O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade 
de cada item que você consumiu e calcule a conta final.

Hambúrguer................. R$ 3,00
Cheeseburger............... R$ 2,50
Fritas............................ R$ 2,50
Refrigerante................. R$ 1,00
Milkshake..................... R$ 3,00    
"""

hamburger = int(input("Digite a quantidade de hambúrgeres consumidos: "))
cheeseburger = int(input("Digite a quantidade de cheeseburgers consumidos: "))
fritas = int(input("Digite a quantidade de porções de fritas consumidas: "))
refrigerante = int(input("Digite a quantidade de refrigerantes consumidos: "))
milkshake = int(input("Digite a quantidade de milkshakes consumidos: "))


valor = (hamburger * 3) + (cheeseburger * 2.5) + (fritas * 2.5) + (refrigerante * 1) + (milkshake * 3)

print(f"O valor da conta final é de: R${valor : .2f}")