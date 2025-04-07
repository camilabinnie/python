#Escreva um algoritmo para ler as notas das duas avaliações de um aluno no semestre, calcular e
#escrever a média semestral e a seguinte mensagem: ‘PARABÉNS! Você foi aprovado’ somente se
#o aluno foi aprovado (considere 6.0 a nota mínima para aprovação).
test1 = float(input("Score 1: "))
test2 = float(input("Score 2: "))

average = (test1 + test2) / 2

if average >= 6.0:
    print("Congratulations! You have been approved!")
else:
    print("You did not reach the required score.")

#Acrescente ao exercício acima a mensagem ‘Você foi REPROVADO! Estude mais’ caso a média
#calculada seja menor que 6,0.