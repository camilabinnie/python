#Ler três valores para os lados de um triângulo: A, B e C. Verificar se os lados fornecidos formam
#realmente um triângulo. Se formar, deve ser indicado o tipo de triângulo: Isósceles, escaleno ou
#eqüilátero.
A = float(input("Enter side A: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))

if A + B > C and B + C > A and A + C > B:
    print("The sides form a triangle.")

    if A == B == C:
        print("It is an equilateral triangle.")
    elif A == B or B == C or A == C:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")
        
else:
    print("The sides do not form a triangle.")