class alfabetos():
    def __init__(self,texto):
        self.alfabetoOriginal = 'abcdefghijklmnopqrstuvwxyz'
        self.texto = texto
        self.frequencia = 0.073
        self.frequencias_portugues_decimal = {
    'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499, 'e': 0.1257,
    'f': 0.0102, 'g': 0.0130, 'h': 0.0128, 'i': 0.0618, 'j': 0.0040,
    'k': 0.0002, 'l': 0.0278, 'm': 0.0474, 'n': 0.0505, 'o': 0.1073,
    'p': 0.0252, 'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
    'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021, 'y': 0.0001, 'z': 0.0047
}
        self.analisedefrequencia = None
    def analiseFrequencia(self):
        analise = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
        i = int(len(self.texto))
        for k in self.texto:
            analise[k] +=1
        
        for k in analise.keys():
            analise[k] = (analise[k])/i
        self.analisedefrequencia = analise
        return analise
    
    def ComparadorFrequencias(self,frequencias):
        frequencia_mais_proxima = min(frequencias, key=lambda x: abs(x - self.frequencia))
        return (frequencia_mais_proxima, frequencias.index(frequencia_mais_proxima)+1 )
    
def decript(text): 
    alf = alfabetos(text)
    alf.analiseFrequencia()
    constantesdefrequencia = []
    frequencias_original_lista = list(alf.frequencias_portugues_decimal.values())
    frequencia_criptografada_lista = list(alf.analisedefrequencia.values())

    for k in range(1,26):
        frequencia = 0
        for i in range(0,26):
            deslocamento = k + i 
            if deslocamento > 25:
                deslocamento = deslocamento%26
            
            frequencia += frequencias_original_lista[i]*frequencia_criptografada_lista[deslocamento]

        constantesdefrequencia.append(frequencia)
    return alf.ComparadorFrequencias(constantesdefrequencia)[1]

print(decript('nanyvfrfznvferpragrfzbfgenzdhrnfserdhrapvnfqryrgenfqnzrfznsbezndhrnfserdhrapvnfqrcnynienfgraqrzninevnegnagbcrybrfpevgbedhnagbcrybnffhagbanbfrcbqrrfperirehzrafnvbfboerenvbfkfrzhfbserdhragrqryrgenfkfrnerqnpnbgrenhznserdhrapvnqryrgenfrfcrpvnyzragrrfgenaunfrbrafnvbrfboerbhfbserdhragrqrenvbfkcnenbgengnzragbqrmroenfabdngneqvsreragrfnhgberfgrzunovgbfdhrcbqrzfreersyrgvqbfabhfbqnfyrgenfbrfgvybqrrfpevgnqrurzvatjnlcberkrzcybrivfviryzragrqvsreragrqbrfgvybqrsnhyxareyrgenfovtenznfgevtenznfnfserdhrapvnfqrcnynienfbpbzcevzragbqnfcnynienfrbpbzcevzragbqnffragrapnfcbqrzfrepnyphynqbfcbenhgberfcrpvsvpbrhfnqbfcnencebinebhartnennhgbevnqbfgrkgbfzrfzbcnenbfnhgberfphwbfrfgvybfanbfnbgnbqviretragrf'))
