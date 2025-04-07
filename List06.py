#Escreva um algoritmo para ler 2 valores (considere que não serão informados valores iguais) 
# e escrever o maior deles.
value1 = float(input("Value 01: "))
value2 = float(input("Value 02: "))
if value1 > value2:
    print(f"The higher value is Value number 1: {value1}")
else:
    print(f"The higher value is Value number 2: {value2}")
