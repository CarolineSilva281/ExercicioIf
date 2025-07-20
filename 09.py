# Exercício 9
# Passo 1: Pedir para o usuário digitar um caractere
caractere = input("Digite um caractere: ")

# Passo 2: Verificar se é letra maiúscula, minúscula ou caractere especial
if caractere.isalpha():
    if caractere.isupper():
        print("Letra maiúscula")
    else:
        print("Letra minúscula")
else:
    print("Caractere especial")
