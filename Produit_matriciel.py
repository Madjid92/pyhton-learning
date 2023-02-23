
def insert_matrice():
    mat = []
    i = 1
    while True:
        lign = input('Produit matriciel:'+'\n'+'Insérez les chiffres de la ligne '+str(i) + ' séparés par une (,) ou saisissez ok pour valider votre matrice: ')
        if(lign == "ok") :
            break
        lign = lign.split(',')
        try:
            lign = [ int(lign[i]) for i in range(len(lign))]
        except :
            print("Erreur dans votre saisie , les éléments doivent être entiers")
            continue
        mat.append(lign)
        i = i +1
    return mat

m1 = insert_matrice()
m2 = insert_matrice()
print(m1)
print(m2)


def test_matrice(m):
    longueure_ligne = []
    for i in range(len(m)):
        longueure_ligne.append(len(m[i]))
    
    print(longueure_ligne)
    print(len(longueure_ligne))

    for i in range(len(longueure_ligne)-1):
        if(not longueure_ligne[i] == longueure_ligne[i+1]):
            return False
    return True

verif_m1 = test_matrice(m1)
verif_m2 = test_matrice(m2)


def test_prod_matr(m1,m2):
    for i in range(len(m1)):
        if len(m1[i]) == len(m2):
            return True
        else:
            return False


def produit_matriciel(m1,m2):
    list=[]
    prod_matr=[]
    for y in range(len(m1)):
        m3=[]
        for i in range(len(m1)):
            prod=0
            for x in range(len(m2)):
                list.append((m1[i][x])*(m2[x][y]))
                prod=prod+((m1[i][x])*(m2[x][y]))
            m3.append(prod)
        prod_matr.append(m3)
    print(list)
    return(prod_matr)

if verif_m1 and verif_m2:
    if test_prod_matr(m1,m2):
        print(produit_matriciel(m1,m2))
    else:
        print("Produit matriciel impossible, revoyez la longueur de vos matrices !")
else:
    print("Erreur, matrice non conforme !")