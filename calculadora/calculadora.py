def cesar():
    convertido2 = ''
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def cripto():
        # alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # convertido = ''
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
        # alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # convertido = ''
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
        check = True
        while(check):
            print('')
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
                check = False
                print('Até a proxima!')

    menu()


def menu():
    check = True
    while(check):
        print("|========================================|")
        print("|        [1] METODO CESAR                |")
        print("|        [2] METODO PLAYFAIR             |")
        print("|        [3] METODO VIGENERE             |")
        print("|        [0] ENCERRAR                    |")
        print("|========================================|")
        
        opc = int(input('Escolha uma opção: '))
        if opc == 1:
            cesar()
        else:
            check = False
            print('Até a proxima!')
        
menu()