'''4. Fibonacci com memorização de resultado. Escreva uma nova versão da sua função
recursiva do exercício 2 (Fibonacci) utilizando a técnica de memorização de resultado para
melhorar desempenho e consumo de memória.'''

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        result = n
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    memo[n] = result 

    return result

numero = int(input("Insira um número inteiro positivo: "))
resultado = fibonacci(numero)
print(f"O {numero}º termo da sequência de Fibonacci é {resultado}")
