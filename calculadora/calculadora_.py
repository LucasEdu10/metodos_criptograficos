def vigenere():
    def generateKey(string, key): 
        key = list(key) 
        if len(string) == len(key):
            return(key) 
        else:
            for i in range(len(string) - len(key)): 
                key.append(key[i % len(key)]) 
        return("" . join(key)) 

    def cipherText(string, key): 
        cipher_text = []
        for i in range(len(string)): 
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A') 
            cipher_text.append(chr(x)) 
        return("" . join(cipher_text)) 

    def originalText(cipher_text, key):
        orig_text = [] 
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A') 
            orig_text.append(chr(x)) 
        return("" . join(orig_text)) 

    # Driver code 
    if __name__ == "__main__": 
        string = str(input("Digite a palavra: "))
        string = string.replace(" ", "")
        string = string.upper()
        keyword = "CRIPTO"
        key = generateKey(string, keyword) 
        cipher_text = cipherText(string,key)
        print("CIFRADA :", cipher_text)
        print("Texto original: ", originalText(cipher_text, key))
        
# Peguei o codigo no site https://www.geeksforgeeks.org/vigenere-cipher/, mas entendi a forma que ele está fazendo e fiz algumas alterações

def cesar():
    convertido2 = ''
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def cripto():
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
        elif opc == 2:
            print("Infelizmente não fiz")
        elif opc == 3:
            vigenere()
        else:
            check = False
            print('Até a proxima!')
        
menu()