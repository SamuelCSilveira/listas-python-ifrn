"""Exercício 2:
Modifique o programa anterior para solicitar a nota da recuperação se o aluno ficou abaixo de 6. Calcule a média final usando a primeira média e a nota da recuperação. O aluno será aprovado se a média final for 5 ou mais, caso contrário, será reprovado. Mostre a média final e a mensagem.
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média é de{media: .1f}.")

if media >= 6:
  print("Você está aprovado.")

else:
  nota_rec = float(input("Digite a nota da recuperação: "))
  media_final = (media + nota_rec) / 2
  print(f"A média final é{media_final: .1f}.")
  
  if media_final >= 5:
    print("Você está aprovado.")
  
  else:
    print("Você está reprovado.")