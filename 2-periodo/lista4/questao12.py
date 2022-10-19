"""Exercício 12:
Modifique o programa anterior para escrever, por extenso, números de 1 até 1000.
"""

def extenso(n):
    # 1 - 20
    if n == 1:
        print("Um", end="")
    elif n == 2:
        print("Dois", end="")
    elif n == 3:
        print("Três", end="")
    elif n == 4:
        print("Quatro", end="")
    elif n == 5:
        print("Cinco", end="")
    elif n == 6:
        print("Seis", end="")
    elif n == 7:
        print("Sete", end="")
    elif n == 8:
        print("Oito", end="")
    elif n == 9:
        print("Nove", end="")
    elif n == 10:
        print("Dez", end="")
    elif n == 11:
        print("Onze", end="")
    elif n == 12:
        print("Doze", end="")
    elif n == 13:
        print("Treze", end="")
    elif n == 14:
        print("Catorze", end="")
    elif n == 15:
        print("Quinze", end="")
    elif n == 16:
        print("Dezesseis", end="")
    elif n == 17:
        print("Dezessete", end="")
    elif n == 18:
        print("Dezoito", end="")
    elif n == 19:
        print("Dezenove", end="")
    elif n == 20:
        print("Vinte", end="")

    # 21 - 100
    elif n == 30:
        print("Trinta", end="")
    elif n == 40:
        print("Quarenta", end="")
    elif n == 50:
        print("Cinquenta", end="")
    elif n == 60:
        print("Sessenta", end="")
    elif n == 70:
        print("Setenta", end="")
    elif n == 80:
        print("Oitenta", end="")
    elif n == 90:
        print("Noventa", end="")
    elif n == 100:
        print("Cem", end="")

    elif n > 20 and n < 30:
        extenso(20)
        print(" e ", end="")
        extenso(n-20)
    elif n > 30 and n < 40:
        extenso(30)
        print(" e ", end="")
        extenso(n-30)
    elif n > 40 and n < 50:
        extenso(40)
        print(" e ", end="")
        extenso(n-40)
    elif n > 50 and n < 60:
        extenso(50)
        print(" e ", end="")
        extenso(n-50)
    elif n > 60 and n < 70:
        extenso(60)
        print(" e ", end="")
        extenso(n-60)
    elif n > 70 and n < 80:
        extenso(70)
        print(" e ", end="")
        extenso(n-70)
    elif n > 80 and n < 80:
        extenso(80)
        print(" e ", end="")
        extenso(n-80)
    elif n > 90 and n < 100:
        extenso(90)
        print(" e ", end="")
        extenso(n-90)

    # 101 - 1000
    elif n == 200:
        print("Duzentos", end="")
    elif n == 300:
        print("Trezentos", end="")
    elif n == 400:
        print("Quatrocentos", end="")
    elif n == 500:
        print("Quinhentos", end="")
    elif n == 600:
        print("Seiscentos", end="")
    elif n == 700:
        print("Setecentos", end="")
    elif n == 800:
        print("Oitocentos", end="")
    elif n == 900:
        print("Novecentos", end="")
    elif n == 1000:
        print("Mil", end="")

    elif n > 100 and n < 200:
        print("Cento e ", end="")
        extenso(n-100)
    elif n > 200 and n < 300:
        extenso(200)
        print(" e ", end="")
        extenso(n-200)
    elif n > 300 and n < 400:
        extenso(300)
        print(" e ", end="")
        extenso(n-300)
    elif n > 400 and n < 500:
        extenso(400)
        print(" e ", end="")
        extenso(n-400)
    elif n > 500 and n < 600:
        extenso(500)
        print(" e ", end="")
        extenso(n-500)
    elif n > 600 and n < 700:
        extenso(600)
        print(" e ", end="")
        extenso(n-600)
    elif n > 700 and n < 800:
        extenso(700)
        print(" e ", end="")
        extenso(n-700)
    elif n > 800 and n < 900:
        extenso(800)
        print(" e ", end="")
        extenso(n-800)
    elif n > 900 and n < 1000:
        extenso(900)
        print(" e ", end="")
        extenso(n-900)
    
    else:
        print("Número inválido!")

numero = int(input("Digite um número de 1 a 1000: "))
extenso(numero)