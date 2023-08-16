'''
6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido
'''

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))

maior_valor = max(val1, val2)
menor_valor = min(val2, val2)
diferenca = maior_valor - menor_valor

print("A diferença entre o maior valor ({}) e o menor valor ({}) é: {}".format(maior_valor, menor_valor, diferenca))

