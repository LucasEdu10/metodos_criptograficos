def cripto():
    frase = str(input('Digite a frase desejada: '))
    frase = frase.replace(" ","")
    print(frase)



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
