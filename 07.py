# Exercício 7
# Passo 1: Pedir para o usuário digitar os três lados do triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Passo 2: Verificar se os lados formam um triângulo (soma de dois lados > terceiro)
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Passo 3: Verificar o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
else:
        print("Triângulo Escaleno")
 
