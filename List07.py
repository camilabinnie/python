#Ler um valor numérico que esteja na faixa de valores de 1 até 9. O programa deve apresentar a
#mensagem “O valor está na faixa permitida”, caso o valor informado esteja entre 1 e 9. Se o valor
#estiver fora dessa faixa, o programa deve apresentar a mensagem “O valor está fora da faixa
#permitida”.
value = int(input("Enter a number between 1 and 9: "))
if 1 <= value <= 9:
    print("The value is within the allowed range")
else:
    print("The value is outside the allowed range")
