tabela_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def codificar_base64_manual(mensagem):
    # Converte a mensagem para binário
    mensagem_binario = ''.join([f'{ord(c):08b}' for c in mensagem])
    print(mensagem_binario)

    blocos_6bits = [mensagem_binario[i:i+6] for i in range(0, len(mensagem_binario), 6)]

    if len(blocos_6bits[-1]) < 6:
        blocos_6bits[-1] = blocos_6bits[-1].ljust(6, '0')

    mensagem_codificada = ''.join([tabela_base64[int(b, 2)] for b in blocos_6bits])

    while len(mensagem_codificada) % 4 != 0:
        mensagem_codificada += '='
    
    return mensagem_codificada


def decodificar_base64_manual(mensagem_codificada):
    # Remove o caractere de padding '='
    mensagem_codificada = mensagem_codificada.replace('=', '')
    

    binario = ''
    for letra in mensagem_codificada:

        b = tabela_base64.index(letra)
        binario += f'{b:06b}'  
    

    binario = binario[:len(binario) - (len(binario) % 8)]
    
 
    texto = ''
    for i in range(0, len(binario), 8):
        bloco_8bits = binario[i:i+8]
        caractere = chr(int(bloco_8bits, 2)) 
        texto += caractere
    
    return texto

mensagem_original = "Exemplo Base64"
mensagem_codificada = codificar_base64_manual(mensagem_original)
print("Mensagem Original:", mensagem_original)
print("Mensagem Codificada:", mensagem_codificada)



print(decodificar_base64_manual('RXhlbXBsbyBCYXNlNjQ='))

