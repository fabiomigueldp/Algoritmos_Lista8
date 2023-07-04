'''5. Total de valores numéricos. Escreva um programa que leia os valores numéricos do usuário
até que uma linha em branco seja inserida. Exiba a soma total de valores inseridos pelo
usuário (ou 0,0 se o primeiro valor inserido for uma linha em branco). Conclua esta tarefa
usando recursão. Seu programa não pode usar nenhum laço de repetição.

Dica: o corpo da sua função recursiva precisará ler um valor do usuário e, em seguida,
determinar se deve ou não fazer uma chamada recursiva. Sua função não precisa de
nenhum parâmetro, mas precisará retornar um resultado numérico.'''

def calcular_total():
    valor = input("Insira um valor numérico (ou deixe em branco para sair): ")

    if valor == "":
        return 0.0
    else:
        try:
            numero = float(valor)
            resto = calcular_total()
            return numero + resto
        except ValueError:
            print("Valor inválido. Tente novamente.")
            return calcular_total()

total = calcular_total()
print("Total:", total)
