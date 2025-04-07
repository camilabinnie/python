#As maçãs custam R$ 0,30 se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
#compradas pelo menos doze. Escreva um algoritmo que leia o número de maçãs compradas,
#calcule e escreva o valor total da compra.
apple_number = int(input("How many apples were bought? "))

if apple_number >= 12:
    total_value = apple_number * 0.25
else:
    total_value = apple_number * 0.30

print(f"Total value to pay is R$ {total_value:.2f}")
