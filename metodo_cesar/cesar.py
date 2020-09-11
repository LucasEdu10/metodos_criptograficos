
convertido2 = ''

def cripto():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    convertido = ''
    palavra = str(input("Digite a palavra: "))
    key = int(input("Digite a chave: "))
    palavra = palavra.upper()
    for palavras in palavra:
        if palavras in alfabeto:
            posicao = alfabeto.find(palavras)
            posicao = (posicao + key) % 26
            convertido = convertido + alfabeto[posicao]

    print('A palavra foi: ',palavra)
    print('A palavra criptografada é: ',convertido)

def dscripto():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    convertido = ''
    palavra = str(input("Digite a palavra: "))
    key = int(input("Digite a chave: "))
    palavra = palavra.upper()
    for palavras in palavra:
        if palavras in alfabeto:
            posicao = alfabeto.find(palavras)
            posicao = (posicao - key) % 26
            convertido = convertido + alfabeto[posicao]
    print('A palavra descriptografada é: ',convertido)

def menu():
    print('|========================|')
    print('| [1] - Encriptografar   |')
    print('| [2] - Descriptografar  |')
    print('| [0] - Encerrar         |')
    print('|========================|')
    print('')
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        cripto()
    elif opc == 2:
        dscripto()
    else:
        print('Até a proxima!')

menu()