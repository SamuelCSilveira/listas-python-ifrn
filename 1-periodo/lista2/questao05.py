"""Exercício 5:
Escreva um programa que informa sobre a aprovação de um empréstimo habitacional. O usuário informa o valor da casa, o salário e a quantidade de anos a pagar. O valor da prestação não pode ser superior a 30% do salário. Informe o valor da prestação e se o empréstimo será aprovado ou não. Não são considerados juros neste exemplo.
"""

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de anos a pagar: "))

prestacao = valor_casa / (anos * 12)

if prestacao > 0.3 * salario:
  print(f"O valor da prestação será: R${prestacao: .2f}")
  print("O empréstimo não foi aprovado.")

else:
  print(f"O valor da prestação será: R${prestacao: .2f}")
  print("O empréstimo foi aprovado.")