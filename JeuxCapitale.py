import random

listCap = ['Paris','Caire','Londres','Berlin','Rome','Madrid','Dublin','Alger']

listPay = ['France','Egypte','Angleterre','Allemagne','Italie','Espagne','Irlande','Algérie']

mapCapPay = {
            'France':'Paris',
            'Egypte':'Caire',
            'Angleterre':'Londres',
            'Allemagne':'Berlin',
            'Espagne':'Madrid',
            'Irlande':'Dublin',
            'Algérie':'Alger',
            'Italie' : 'Rome'
}

pays = random.choice(listPay)

capitale = input('Veuillez saisir la capitale de ' + pays+': ')

while True:
    if capitale == mapCapPay[pays]:
        print("Bravo")
        break
    if capitale != mapCapPay[pays]:
        print("Désolé, votre réponse est incorrecte !")
        capitale = input('Veuillez réessayer: ')
