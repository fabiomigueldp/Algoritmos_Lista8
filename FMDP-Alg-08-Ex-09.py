'''9. Raiz quadrada recursiva. No exercício 9 da lista 4 você explorou como a iteração pode ser
usada para calcular a raiz quadrada de um número. Naquele exercício, uma melhor
aproximação da raiz quadrada foi gerada com cada iteração adicional de um laço de repetição.
Neste exercício, você deve usar a mesma estratégia de aproximação, mas você usará
recursão ao invés de iteração.
Crie uma função de raiz quadrada com dois parâmetros. O primeiro parâmetro, n, é o número
para o qual a raiz quadrada está sendo calculada. O segundo parâmetro, estimativa, é a
estimativa atual para a raiz quadrada. O parâmetro de estimativa deve ter um valor padrão de
1,0. Não forneça um valor padrão para o primeiro parâmetro.
Sua função de raiz quadrada será recursiva. O caso básico ocorre quando o valor absoluto da
diferença entre estimativa2 (estimativa ao quadrado) e n é menor ou igual a 10-12. Neste caso,
sua função deve retornar o valor de estimativa porque está próximo o suficiente da raiz
quadrada de n. Caso contrário, sua função deve retornar o resultado da chamada a si própria
passando n como primeiro parâmetro e como o segundo parâmetro.
Escreva um programa principal que demonstre sua função calculando a raiz quadrada de
vários valores diferentes. Ao chamar sua função de raiz quadrada a partir do programa
principal, você deve passar apenas um parâmetro para ela, de modo que o valor padrão para
estimativa seja usado.

Dica: pesquise sobre funções com argumentos padrão (default arguments) em Python.'''

def raiz_quadrada(n, estimativa=1.0):
    if abs(estimativa ** 2 - n) <= 10e-12:
        return estimativa
    else:
        nova_estimativa = (estimativa + n / estimativa) / 2
        return raiz_quadrada(n, nova_estimativa)

numeros = [4, 9, 16, 25, 36]

for num in numeros:
    resultado = raiz_quadrada(num)
    print(f"A raiz quadrada de {num} é {resultado}")

