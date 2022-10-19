"""Exercício 14.11:
Modifique o programa anterior para escrever, por extenso, números de 1 até 100.
"""

def extenso(n):
    # 1 - 20
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

    # 21 - 100
    elif n == 30:
        return "Trinta"
    elif n == 40:
        return "Quarenta"
    elif n == 50:
        return "Cinquenta"
    elif n == 60:
        return "Sessenta"
    elif n == 70:
        return "Setenta"
    elif n == 80:
        return "Oitenta"
    elif n == 90:
        return "Noventa"
    elif n == 100:
        return "Cem"

    elif n > 20 and n < 30:
        return extenso(20) + " e " + extenso(n-20)
    elif n > 30 and n < 40:
        return extenso(30) + " e " + extenso(n-30)
    elif n > 40 and n < 50:
        return extenso(40) + " e " + extenso(n-40)
    elif n > 50 and n < 60:
        return extenso(50) + " e " + extenso(n-50)
    elif n > 60 and n < 70:
        return extenso(60) + " e " + extenso(n-60)
    elif n > 70 and n < 80:
        return extenso(70) + " e " + extenso(n-70)
    elif n > 80 and n < 80:
        return extenso(80) + " e " + extenso(n-80)
    elif n > 90 and n < 100:
        return extenso(90) + " e " + extenso(n-90)
    
    else:
        print("Número inválido!")

numero = int(input("Digite um número de 1 a 100: "))
resultado = extenso(numero)
print(resultado)