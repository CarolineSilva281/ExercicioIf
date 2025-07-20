# Exercício 5
# Passo 1: Pedir a nota do aluno
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Passo 2: Verificar se a nota é válida
if nota < 0 or nota > 10:
    print("Nota inválida.")
# Passo 3: Verificar a faixa da nota e mostrar a situação do aluno
elif nota < 5:
    print("Reprovado")
elif nota <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
