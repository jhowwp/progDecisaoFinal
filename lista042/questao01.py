'''
1. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

numero = float(input("Digite um número: "))

if numero > 1000:
    print("O número digitado está acima de 1000.")
if numero < 1000:
    print("O número digitado está abaixo de 1000.")
else:
    print("O número digitado é igual a 1000.")
