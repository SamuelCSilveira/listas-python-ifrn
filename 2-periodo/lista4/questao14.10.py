"""Exercício 14.10:
Crie uma função que recebe um número entre 1 e 20 e retorne o número por extenso. Ex.: 1/um, 9/nove, 15/quinze, etc. Se o valor não estiver no intervalo, informar que é inválido.
"""

def extenso(n):
    if n == 1:
        return "Um"
    elif n == 2:
        return "Dois"
    elif n == 3:
        return "Três"
    elif n == 4:
        return "Quatro"
    elif n == 5:
        return "Cinco"
    elif n == 6:
        return "Seis"
    elif n == 7:
        return "Sete"
    elif n == 8:
        return "Oito"
    elif n == 9:
        return "Nove"
    elif n == 10:
        return "Dez"
    elif n == 11:
        return "Onze"
    elif n == 12:
        return "Doze"
    elif n == 13:
        return "Treze"
    elif n == 14:
        return "Catorze"
    elif n == 15:
        return "Quinze"
    elif n == 16:
        return "Dezesseis"
    elif n == 17:
        return "Dezessete"
    elif n == 18:
        return "Dezoito"
    elif n == 19:
        return "Dezenove"
    elif n == 20:
        return "Vinte"
    else:
        print("Número inválido!")

numero = int(input("Digite um número de 1 a 20: "))
resultado = extenso(numero)
print(resultado)