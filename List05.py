#Escreva um algoritmo para ler as notas das duas avaliações de um aluno no semestre, calcular e
#escrever a média semestral. Se a média for maior que 6.0 imprimir a mensagem “APROVADO”. Se
#a média for menor que 6.0 e maior que 3.0, imprimir a mensagem “EXAME”, se a média for menor
#que 3.0 imprimir a mensagem “REPROVADO”.
test1 = float(input("Score 1: "))
test2 = float(input("Score 2: "))
average = (test1 + test2) / 2
print(f"Your average is {average}")

if average > 6.0:
    print("APPROVED")
elif average > 3.0:
    print("EXAM")
else:
    print("FAILED")
