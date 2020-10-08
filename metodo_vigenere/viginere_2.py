def cripto():
    frase = str(input('Digite a frase desejada: '))
    frase = frase.replace(" ","")
    print(frase)

    # Cifra plaintext com a cifra de Vigenere
    # Decifra se decrypt for True
    # https://siriarah.wordpress.com/2015/02/03/criptografia-cifra-de-vigenere-em-python/
    
    password = self.repeat_password(password, plaintext)
    plaintext = self.format_str(plaintext)
    textout = ''
    for idx, char in enumerate(plaintext.upper()):
        # indice da letra da cifra
        idx_key = self.plain.find(password[idx])
        # gera alfabeto cifrado
        c_alphabet = self.shift_alphabet(self.plain, idx_key)

        if decrypt:
            idx_p = c_alphabet.find(char)
            textout += self.plain[idx_p]
        else:
            idx_p = self.plain.find(char)
            textout += c_alphabet[idx_p]

    return textout


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
        # elif opc == 2:
        #     dscripto()
        # else:
        #     check = False
        #     print('Até a proxima!')

menu()