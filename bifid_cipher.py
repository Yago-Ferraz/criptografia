def encript(text: str,period: int):
    #key_squad = "abcdefghijklmnopqrstuvwxyz .,0123456789-+!?%*/;:)"
    key_squad = 'phqgmeaylnofdxkrcvszwbuti'
    row=''
    col=''
    for k in text:
        index = key_squad.index(k)
        row += str(index//5)
        col += str(index%5)
    
    group = (len(row)//period)
    if len(row)%period > 0:
        group+=1

    row_split = []
    col_split = []
    
    for i in range(group):

        row_split.append(row[i*period:((i*period)+period)])
        col_split.append(col[i*period:((i*period)+period)])

    sequence = ''

    text_encry = ''
    for i in range(len(row_split)):
        sequence += row_split[i] + col_split[i]

    for i in range(0,(len(sequence)),2):
        numb = [sequence[i],sequence[i+1]]
        numb =int(numb[0])*5 +int(numb[1])%5
        text_encry += key_squad[numb]

    return text_encry

def decript(text: str ,period: int):
    #key_squad = "abcdefghijklmnopqrstuvwxyz .,0123456789-+!?%*/;:)"
    key_squad = 'phqgmeaylnofdxkrcvszwbuti'
    sequence = ''
    for k in text:
        index = key_squad.index(k)
        sequence += str(index//5)
        sequence += str(index%5)
    
    row=''
    col=''

    for i in range(len(sequence)//(period*2)):
            row +=sequence[0:period]
            sequence = sequence.replace(sequence[0:period],'')
            col +=sequence[0:period]
            sequence = sequence.replace(sequence[0:period],'')

    row += sequence[0:len(sequence)//2]
    col += sequence[len(sequence)//2::] 

    plaintext = ''

    for i in range(len(row)):
        letter =int(row[i])*5 +int(col[i])%5
        plaintext+= key_squad[letter]

    
    return plaintext

print(encript('defendtheeastwallofthecastle',5))

print(decript('ffyhmkhycpliashadtrlhcchlblr',5))