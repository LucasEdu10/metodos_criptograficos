def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 
	
def cipherText(string, key): 
	cipher_text = [] 
	for i in range(len(string)): 
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A') 
		cipher_text.append(chr(x)) 
	return("" . join(cipher_text)) 
	
def originalText(cipher_text, key): 
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
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
    print("Texto original: ",
          originalText(cipher_text, key))


# Peguei o codigo no site https://www.geeksforgeeks.org/vigenere-cipher/, mas entendi a forma que ele está fazendo e fiz algumas alterações