'''
2. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000
'''

numero = float(input("Digite um número: "))

if numero < 1000:
    print("O número está abaixo de 1000.")
if numero <= 5000:
    print("O número está entre 1000 e 5000.")
else:
    print("O número está acima de 5000.")

