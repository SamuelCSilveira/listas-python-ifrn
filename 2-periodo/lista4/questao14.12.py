"""Exercício 14.12:
Modifique o programa anterior para escrever, por extenso, números de 1 até 1000.
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

    # 101 - 1000
    elif n == 200:
        return "Duzentos"
    elif n == 300:
        return "Trezentos"
    elif n == 400:
        return "Quatrocentos"
    elif n == 500:
        return "Quinhentos"
    elif n == 600:
        return "Seiscentos"
    elif n == 700:
        return "Setecentos"
    elif n == 800:
        return "Oitocentos"
    elif n == 900:
        return "Novecentos"
    elif n == 1000:
        return "Mil"

    elif n > 100 and n < 200:
        return "Cento e " + extenso(n-100)
    elif n > 200 and n < 300:
        return extenso (200) + " e " + extenso(n-200)
    elif n > 300 and n < 400:
        return extenso (300) + " e " + extenso(n-300)
    elif n > 400 and n < 500:
        return extenso (400) + " e " + extenso(n-400)
    elif n > 500 and n < 600:
        return extenso (500) + " e " + extenso(n-500)
    elif n > 600 and n < 700:
        return extenso (600) + " e " + extenso(n-600)
    elif n > 700 and n < 800:
        return extenso (700) + " e " + extenso(n-700)
    elif n > 800 and n < 900:
        return extenso (800) + " e " + extenso(n-800)
    elif n > 900 and n < 1000:
        return extenso (900) + " e " + extenso(n-900)
    
    else:
        print("Número inválido!")

numero = int(input("Digite um número de 1 a 1000: "))
resultado = extenso(numero)
print(resultado)