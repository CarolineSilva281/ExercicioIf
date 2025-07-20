# Exercício 2
# Passo 1: Pedir para o usuário digitar a temperatura em graus Celsius
temp = float(input("Digite a temperatura em graus Celsius: "))

# Passo 2: Verificar a faixa da temperatura e imprimir a mensagem correspondente
if temp < 0:
    print("Está congelando!")
elif temp <= 25:
    print("Temperatura amena.")
else:
    print("Está quente!")