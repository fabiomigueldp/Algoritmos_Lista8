'''7. Conversão decimal → binário iterativa. Escreva uma função que converte um número
decimal (base 10) em binário (base 2). A função deve receber como parâmetro o número
inteiro decimal (q) e, em seguida, deve realizar a conversão usando o algoritmo de divisão
mostrado abaixo. Quando o algoritmo for concluído, o resultado contém a representação
binária do número, que deve ser retornada pela função como uma string.
DecBinIterativo(q)
result ← ””
repeat
r ← q%2
result ← str(r) + result
q ← q//2
until q == 0;
return result'''

def DecBinIterativo(q):
    result = ""
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q // 2
    return result

decimal = int(input("Insira um número decimal: "))

binario = DecBinIterativo(decimal)

print("O número binário equivalente é:", binario)
