"""Exercício 13:
Crie um programa, dividido em funções, que simulam um sistema de cadastro. Ao executar o programa, o seguinte menu é exibido:

**** MENU ****

1 Cadastrar
2 Listar
3 Excluir
4 Sair

Escolha uma opção:

O usuário digita um dos números e a respectiva função é chamada.

cadastrar() - solicita a digitação do nome e acrescenta-o na lista.
listar() - imprime a lista em ordem alfabética, um nome em cada linha.
excluir() - solicita a digitação do nome e remove-o da lista.

O programa deve se repetir até que o usuário escolha a opção 4.
"""
# Funções
def cadastrar(lista):
    nome = input("\nDigite o nome para cadastrar: ")
    lista.append(nome)

def listar(lista):
    lista.sort()
    print("\nListagem: ")
    for nome in lista:
        print(nome)

def excluir(lista):
    nome = input("\nDigite o nome para excluir: ")
    for item in lista:
        if nome == item:
            lista.pop()

# Programa
lista = []

while True:
    print("\n*** MENU ***\n")
    print("1 Cadastrar")
    print("2 Listar")
    print("3 Excluir")
    print("4 Sair\n")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar(lista)
    elif opcao == 2:
        listar(lista)
    elif opcao == 3:
        excluir(lista)
    elif opcao == 4:
        break
    else:
        print("\nOpção inválida!")