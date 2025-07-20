# Exercício 4
# Passo 1: Pedir para o usuário digitar um número de 1 a 7
dia = int(input("Digite um número de 1 a 7: "))

# Passo 2: Criar um dicionário que relaciona número ao dia da semana
dias_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

# Passo 3: Mostrar o dia correspondente ou "Número inválido"
print(dias_semana.get(dia, "Número inválido"))
