nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceita nota: "))
nota4 = float(input("Digite sua quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print(f"Parabéns você foi aprovado sua média é {media}")
    
else:
    print(f"Sua média é {media}, você foi reprovado")   