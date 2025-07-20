# Exercício 8
# Passo 1: Pedir para o usuário digitar um número entre 1 e 12
mes = int(input("Digite um número de 1 a 12: "))

# Passo 2: Criar dicionário que relaciona número ao nome do mês
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Passo 3: Mostrar o mês correspondente ou "Número inválido"
print(meses.get(mes, "Número inválido"))
