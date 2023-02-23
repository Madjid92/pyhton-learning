from Modulo import modulo 

def InputListUser():
    liste=[]
    while True:
        x = input('insérez un nombre, sinon ok pour quitter :')
        if x == 'ok':
            break
        try:
            x = int(x)
            liste.append(x)
        except ValueError :
            print('La valeur saisie doit étre un entier')
        except :
            print ("Erreur inconue")
    return liste


def NbrChifPair(liste):
    paires = []
    for i in range(len(liste)):
        if modulo(2,liste[i]) == 0:
            paires.append(liste[i])
        else:
            continue
    return len(paires)

login = InputListUser()
print(login)
#test = 
print(NbrChifPair(login))





        




