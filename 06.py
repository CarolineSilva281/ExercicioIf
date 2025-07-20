# Exercício 6
# Passo 1: Pedir para o usuário digitar três números diferentes
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# Passo 2: Comparar os três números para identificar o maior
if a > b and a > c:
    print("Maior número:", a)
elif b > a and b > c:
    print("Maior número:", b)
else:
    print("Maior número:", c)
