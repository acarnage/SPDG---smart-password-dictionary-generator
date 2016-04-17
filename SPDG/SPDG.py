import sys
print("Veuillez nous donner quelques informations...")
PRENOM = input("Entrez prenom: ")
NOM = input("Entrez nom: ")
DATE_DE_NAISSANCE = input("Entrez date de naissance (JJMMAAAA): ")

def checkDATA():
    nulle = 0

    if PRENOM == "":
        nulle+=1

    if NOM == "":
        nulle+=1

    if DATE_DE_NAISSANCE == "":
        nulle+=1

    if len(DATE_DE_NAISSANCE) == 8:
        try:
            DATE_DE_NAISSANCE2 = int(DATE_DE_NAISSANCE)
        except:
            return False

    else:
        return False

    if nulle >= 2:
        return False
    else:
        return True


def writeInFile(file,data):
    fileOpened = open(file,"a+")
    fileOpened.write(data + "\n")
    fileOpened.close()

def baseDATA(data):
    data = data.lower()
    data = data.strip()
    list = []
    list.append(data)
    list.append(data.capitalize())
    list.append(data[:1].lower() + data[1:].upper())

    tamper = ""
    for i in range(0, len(data)):
        if i % 2 == 0:
            tamper += data[i].upper()
        else:
            tamper += data[i].lower()

    list.append(tamper)
    return list

if not checkDATA():
    print("/!\ Erreur pas assez de données ou données incorrect")

def dateList(date):
    list=[]
    list.append(date)
    list.append(date[:4] + date[6:])

    return list

def appendDate(date,list):
    newlist = []
    for item in list:
        newlist.append( item + date)
        newlist.append(item + date[:4] + date[6:])

    return newlist




def complexScheme(a,b):
    newlist = []
    newlist.append(a[:1].lower() + b.lower())
    newlist.append(b[:1].lower() + a.lower())
    newlist.append(a[:1].upper() + b.lower())
    newlist.append(b[:1].upper() + a.lower())
    newlist.append(a[:1].lower() + b.upper())
    newlist.append(b[:1].lower() + a.upper())

    return newlist

def addTwoList(lista,listb):
    listnew = []
    for item in lista:
        for item2 in listb:
            listnew.append(item + item2)

    for item in listb:
        for item2 in lista:
            listnew.append(item + item2)

    return listnew

def writeList(list):
    for item in list:
        writeInFile("dico.txt",item)


a = baseDATA(PRENOM)
b = baseDATA(NOM)
c = addTwoList(a,b)
d = dateList(DATE_DE_NAISSANCE)
e = addTwoList(a,d)
f = addTwoList(b,d)
g = complexScheme(PRENOM,NOM)
h = addTwoList(d,g)


writeList(a)
writeList(b)
writeList(c)
writeList(d)
writeList(e)
writeList(f)
writeList(g)
writeList(h)
