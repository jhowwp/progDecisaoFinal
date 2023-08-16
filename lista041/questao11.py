'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

num = int(input("Informe um número inteiro que possua 3 algarismos: "))

if ( num >= 100 and num <= 999 ):
    centena = num // 100
    print(f"O algarismo das centenas de {num} é {centenas}")
else
    print(f"O valor informado nao possui o algarismo: ")