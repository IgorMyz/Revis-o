senha = None

while senha != 8765:
    senha = input("Digite sua senha: ")
    if senha == "8765":
        print("Acesso Permitido")
        break
    else:
        print("Senha Incorreta")    