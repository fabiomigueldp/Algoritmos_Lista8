'''11. Codificação run-lenght. Escreva uma função recursiva que implemente a técnica de
compressão run-lenght descrita no exercício anterior. Sua função deve receber uma lista ou
uma string como seu único parâmetro. Ela deve retornar a lista compactada em run-lenght
como seu único resultado. Inclua um programa principal que leia uma string do usuário, a
compacte e exiba o resultado codificado em run-lenght.

Dica: talvez você precise implementar um laço de repetição dentro de sua função recursiva.'''

def compactar(lista):
    if not lista:  
        return []

    elemento = lista[0]
    contador = 1
    i = 1

    while i < len(lista) and lista[i] == elemento:
        contador += 1
        i += 1

    return [elemento, contador] + compactar(lista[i:])

entrada = input("Digite uma string: ")
lista_entrada = list(entrada)
lista_codificada = compactar(lista_entrada)

print("Lista codificada em run-length:", lista_codificada)
