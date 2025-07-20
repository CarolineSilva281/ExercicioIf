# Exercício 10
# Passo 1: Pedir para o usuário digitar número de horas trabalhadas
horas = float(input("Digite o número de horas trabalhadas: "))

# Passo 2: Pedir para o usuário digitar o valor da hora
valor_hora = float(input("Digite o valor da hora: "))

# Passo 3: Calcular salário bruto
salario = horas * valor_hora

# Passo 4: Mostrar salário bruto
print(f"Salário bruto: R${salario:.2f}")

# Passo 5: Classificar o salário conforme faixa
if salario <= 1000:
    print("Salário baixo")
elif salario <= 3000:
    print("Salário médio")
else:
    print("Salário alto")
