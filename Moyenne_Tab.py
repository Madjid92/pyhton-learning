def Avg_liste(liste):
    s = 0
    for i in range(len(liste)):
        s = s + liste[i]
    m = s / len(liste)
    return m

def input_list():
    liste = []
    while True:
        try:     
            x = float(input('entrez une valeur: '))
            liste.append(x)
        except:
            break
    return liste

#liste = input_list()
#print(liste)
#Moy = Avg_liste(liste)
#print(Moy)


def convertStringToListNbr (strList) :
    liste = []
    lastIndexBeginNbr = 0
    i = 0
    while True :
        if(i == len(strList) or (strList[i] == ',')):
            try :
                liste.append(int(strList[lastIndexBeginNbr:i]))
            except :
                print("votre list est erroner")
        
        if i == len(strList):
            break

        if((strList[i] == ',')):
            lastIndexBeginNbr = i+1
        i+=1
    return liste


x = (input('Saisissez des nombres séparés par des virgules :'))
print("List : "+x)
print("La moyen de la list est : "+str(Avg_liste(convertStringToListNbr(x))))


