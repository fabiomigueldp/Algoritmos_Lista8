'''6. MDC - Máximo Divisor Comum. Euclides foi um matemático grego que viveu há
aproximadamente 2.300 anos. Seu algoritmo para calcular o MDC - máximo divisor comum de
dois inteiros positivos, a e b, é eficiente e recursivo. Está descrito abaixo:
MDC(a, b)
if b == 0 then
return a
else
c ← a%b
return MDC(b,c)
end
Escreva um programa que implemente o algoritmo recursivo de Euclides e o use para
determinar o máximo divisor comum de dois inteiros inseridos pelo usuário.'''

def mdc(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return mdc(b, c)

numero1 = int(input("Insira o primeiro número inteiro: "))
numero2 = int(input("Insira o segundo número inteiro: "))

resultado = mdc(numero1, numero2)

print("O MDC de", numero1, "e", numero2, "é", resultado)
