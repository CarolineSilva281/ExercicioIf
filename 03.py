# Exercício 3
# Passo 1: Pedir para o usuário digitar uma letra
letra = input("Digite uma letra: ").lower() 

# Passo 2: Verificar se é vogal, consoante ou inválido
if letra in "aeiou":
    print("É uma vogal")
elif letra.isalpha():
    print("É uma consoante")
else:
    print("Não é uma letra válida")