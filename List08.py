#Escreva um algoritmo para ler o ano de nascimento de uma pessoa e escrever uma mensagem
#que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

from datetime import date
current_year = date.today().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

if age >= 16:
    print("You are allowed to vote this year.")
else:
    print("You are not allowed to vote this year.")

