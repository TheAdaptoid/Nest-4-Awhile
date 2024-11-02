keyPhrase = input().replace(" ", "")
tobeEncrypted = input().replace(" ", "")

alphebet = "abcdefghijklmnoprstuvwxyz"
keyPhrase += alphebet
p = ""
for char in keyPhrase:
    if char not in p:
        p = p+char
keyPhrase = p

keyPhraseRows = []
keyPhraseRows.append(keyPhrase[0:5])
keyPhraseRows.append(keyPhrase[5:10])
keyPhraseRows.append(keyPhrase[10:15])
keyPhraseRows.append(keyPhrase[15:20])
keyPhraseRows.append(keyPhrase[20:25])

keyPhraseColumns = [[], [], [], [], []]
for row in keyPhraseRows:
    for i in range(len(row)):
        keyPhraseColumns[i].append(row[i])

newEncrypted = ""
for i in range(len(list(tobeEncrypted))):
    if i == 0:
        newEncrypted += tobeEncrypted[0]
    else:
        if tobeEncrypted[i] == tobeEncrypted[i-1]:
            newEncrypted+="x"+tobeEncrypted[i]
        else:
            newEncrypted += tobeEncrypted[i]

if(not len(newEncrypted) % 2 == 0):
    newEncrypted+="x"

encryptedListDiaphram = []
for i in range(int(len(newEncrypted)/2)):
    encryptedListDiaphram.append([newEncrypted[i*2], newEncrypted[(i*2)+1]])
    i += 1


temp_encryptedListDiaphram = []

for item in encryptedListDiaphram:
    new_item = []
    found = False
    for row in keyPhraseRows:
        row = list(row)
        if(item[0] in row and item[1] in row):
            found = True
            indexLetA = row.index(item[0])
            indexLetB = row.index(item[1])

            if(indexLetA == 4): indexLetA = 0
            else: indexLetA += 1
            if(indexLetB == 4): indexLetB = 0
            else: indexLetB += 1
            new_item = [row[indexLetA], row[indexLetB]]
            break
    
    for row in keyPhraseColumns:
        row = list(row)
        if(item[0] in row and item[1] in row):
            found = True
            indexLetA = row.index(item[0])
            indexLetB = row.index(item[1])

            if(indexLetA == 4): indexLetA = 0
            else: indexLetA += 1
            if(indexLetB == 4): indexLetB = 0
            else: indexLetB += 1
            new_item = [row[indexLetA], row[indexLetB]]
            break
    
    if(not found):
        positionA = []
        positionB = []
        
        for row in keyPhraseRows:
            if(item[0] in row or item[1] in row):
                if(item[0] in row):
                    positionA.append(row.index(item[0]))
                    positionA.append(keyPhraseRows.index(row))
                
                if(item[1] in row):
                    positionB.append(row.index(item[1]))
                    positionB.append(keyPhraseRows.index(row))
            
        newPosA = [positionB[0], positionA[1]]
        newPosB = [positionA[0], positionB[1]]

        new_item = [keyPhraseRows[newPosA[1]][newPosA[0]], keyPhraseRows[newPosB[1]][newPosB[0]]]


    temp_encryptedListDiaphram.append(new_item)

encryptedListDiaphram = temp_encryptedListDiaphram
exportedWord = ""
for diaphram in encryptedListDiaphram:
    exportedWord += diaphram[0] + diaphram[1]

print(exportedWord.upper())