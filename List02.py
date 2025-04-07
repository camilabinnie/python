# Escreva um algoritmo para ler um valor numérico inteiro positivo ou negativo e apresentar o valor
#lido como sendo um valor positivo, ou seja, se o valor lido for menor ou igual a zero, ele deve ser
#multiplicado por -1.
value = int(input("Enter an integer number"))
if value <= 0:
    value = value * -1
print(f"Your positive number is {value}")
