"""Exercício 10:
Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha, banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor total acumulado da área residencial."""

state = ''
area_total = 0

for i in range(1000):
  nome = input("Digite o nome do cômodo: ")
  largura = float(input("Digite a largura do cômodo: "))
  comprimento = float(input("Digite o comprimento do cômodo: "))
  area = largura * comprimento
  area_total += area
  print(f"\nA área do(a) {nome} é {area} m².")
  state = input("\nDeseja continuar calculando as áreas dos cômodos? ")
  print('\n')
  if state.lower() == "nao":
    break

print(f"A área residencial total é de {area_total} m².")