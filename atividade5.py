idade = float(input("Digite sua idade: "))

if idade <= 12:
    print("Você é uma criança")
elif idade > 12 and idade <=18:
    print("Você é um Adolescente")
elif idade > 18 and idade <= 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")           