 #Exercício 1
# Passo 1: Pedir para o usuário digitar um número inteiro
num = int(input("Digite um número inteiro: "))

# Passo 2: Verificar se o número é positivo, negativo ou zero
if num > 0:
    print("Número positivo")
elif num < 0:
    print("Número negativo")
else:
    print("É zero")