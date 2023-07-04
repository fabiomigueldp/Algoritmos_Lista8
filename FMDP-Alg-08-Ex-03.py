'''3. Palíndromo. Faça uma função Python recursiva que recebe uma string e retorne um valor
lógico indicando se ela é ou não é um palíndromo. OBS: Um palíndromo é uma palavra ou
frase, que é igual quando lida da esquerda para a direita ou da direita para a esquerda
(Espaços em branco e sinais de pontuação devem ser descartados). Exemplo de palíndromo:
"saudavel leva duas”.'''

def is_palindrome(text):
    text = ''.join(e for e in text if e.isalnum())

    if len(text) < 2:
        return True

    if text[0].lower() == text[-1].lower():
        return is_palindrome(text[1:-1])
    else:
        return False

texto = input("Insira uma palavra ou frase: ")
if is_palindrome(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
