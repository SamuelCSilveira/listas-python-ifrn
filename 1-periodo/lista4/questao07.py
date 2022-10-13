"""Exercício 7:
Crie um programa que simule um painel eletrônico que organiza uma fila. O programa exibe um menu com as seguintes opções: 1. Entrar na fila. / 2. Consultar a fila. / 3. Chamar próximo da fila. Na opção 1, o usuário digita o nome da pessoa que está entrando no final da fila. Na opção 2, o programa imprime a fila atual e diz *quantas pessoas há na fila*. Na opção 3, o programa exibe uma mensagem chamando a pessoa da vez e remove seu nome da fila. Se não houver pessoas na fila, mostre a mensagem "fila vazia"."""

fila = []

while True:
  print("1. Entrar na fila")
  print("2. Consultar a fila")
  print("3. Chamar próximo da fila")
  option = input("Opção: ")

  if option == '1':
    nome = input("\nDigite o nome da pessoa que está entrando na fila: ")
    fila.append(nome)
    print()
  
  elif option == '2':
    print(f"\n{fila}\n")
  
  elif option == '3':
    if len(fila) == 0:
      print("\nFila vazia.\n")
    else:
      chamado = fila.pop(0)
      print(f"\nPessoa da vez: {chamado}\n")
  
  else:
    print("\nOpção inválida.\n")