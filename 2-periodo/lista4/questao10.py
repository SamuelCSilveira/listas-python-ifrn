"""Exercício 10:
Crie uma função que recebe um número entre 1 e 20 e imprime o número por extenso. Ex.: 1/um, 9/nove, 15/quinze, etc. Se o valor não estiver no intervalo, informar que é inválido.
"""

def extenso(n):
    if n == 1:
        print("Um")
    elif n == 2:
        print("Dois")
    elif n == 3:
        print("Três")
    elif n == 4:
        print("Quatro")
    elif n == 5:
        print("Cinco")
    elif n == 6:
        print("Seis")
    elif n == 7:
        print("Sete")
    elif n == 8:
        print("Oito")
    elif n == 9:
        print("Nove")
    elif n == 10:
        print("Dez")
    elif n == 11:
        print("Onze")
    elif n == 12:
        print("Doze")
    elif n == 13:
        print("Treze")
    elif n == 14:
        print("Catorze")
    elif n == 15:
        print("Quinze")
    elif n == 16:
        print("Dezesseis")
    elif n == 17:
        print("Dezessete")
    elif n == 18:
        print("Dezoito")
    elif n == 19:
        print("Dezenove")
    elif n == 20:
        print("Vinte")
    else:
        print("Número inválido!")

numero = int(input("Digite um número de 1 a 20: "))
extenso(numero)