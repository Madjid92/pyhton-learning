from Personne import Personne
from Vehicule import Vehicule
from Voiture import Voiture
from Utilitaire import Utilitaire
from Monospace import Monospace
from Camion import Camion
from Location import Location
import datetime
from Serialize import Serialize
from datetime import datetime
import os

ListPers = []
def SaisiePers():
    nom = input("Saisissez le nom de la personne : ")
    prenom = input("Saisissez le prénom de la personne : ")
    naissance = input("Saisissez la date de naissance de la personne : ")
    pers = Personne(nom,prenom,naissance)
    ListPers.append(pers)
    return pers

ListVoiture = []
def SaisieVoiture():
    nom = input("Saisissez le nom de la voiture: ")
    model = input("Saisissez le model de la voiture: ")
    annee = input("Saisissez l'année de la voiture: ")
    matricule = input("Saisissez le matricule de la voiture: ")
    km = input("Saisissez le kilométrage de la voiture: ")
    nbrplace = input("Saisissez le nombre de places de la voiture: ")
    voit = Voiture(nom,model,annee,matricule,km,nbrplace)
    ListVoiture.append(voit)
    return voit

ListUtilitaire = []
def SaisieUtilitaire():
    nom = input("Saisissez le nom de l'utilitaire: ")
    model = input("Saisissez le model de l'utilitaire: ")
    annee = input("Saisissez l'année de l'utilitaire: ")
    matricule = input("Saisissez le matricule de l'utilitaire: ")
    km = input("Saisissez le kilométrage de l'utilitaire: ")
    volume = input("Saisissez le volume de l'utilitaire: ")
    util = Utilitaire(nom,model,annee,matricule,km,volume)
    ListUtilitaire.append(util)
    return util

ListMonospace = []
def SaisieMonospace():
    nom = input("Saisissez le nom du monospace: ")
    model = input("Saisissez le model du monospace: ")
    annee = input("Saisissez l'année du monospace: ")
    matricule = input("Saisissez le matricule du monospace: ")
    km = input("Saisissez le kilométrage du monospace: ")
    nbrplace = input("Saisissez le nombre de places du monospace: ")
    space = Monospace(nom,model,annee,matricule,km,nbrplace)
    ListMonospace.append(space)
    return space
    
ListCamion = []
def SaisieCamion():
    nom = input("Saisissez le nom du camion: ")
    model = input("Saisissez le model du camion: ")
    annee = input("Saisissez l'année du camion: ")
    matricule = input("Saisissez le matricule du camion: ")
    km = input("Saisissez le kilométrage du camion: ")
    tonnage = input("Saisissez le tonnage du camion: ")
    truck = Camion(nom,model,annee,matricule,km,tonnage)
    ListCamion.append(truck)
    return truck


ListLocation = []
def SaisieLocation():
    code = input("Saisissez le code de la location: ")
    client = ChoosePers()
    vehicule = ChooseCar()
    loc = Location(code,client,vehicule)
    ListLocation.append(loc)
    return loc

def ChoosePers():
    print("ID"+"\t"+"Nom"+"\t"+"Prénom"+"\t"+"Date de naissance"+"\n"+
    "..........................................................")
    for i in range(len(ListPers)):
        print(str(ListPers[i].id)+"\t"+ListPers[i].nom+"\t"+ListPers[i].prenom+"\t"+str(ListPers[i].naissance))
    client1 = input("Veuillez séléctionner l'ID du client: ")
    for i in range(len(ListPers)):
        if str(ListPers[i].id) == str(client1) :
            return (str(ListPers[i].id))

def ChooseCar():
    print("Les voitures disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Nbr places"+"\n"+
    "..............................................................................................")
    for i in range(len(ListVoiture)):
        print(ListVoiture[i].nom+"\t"+ListVoiture[i].model+"\t"+str(ListVoiture[i].annee)+"\t"+ListVoiture[i].matricule+"\t"+
        str(ListVoiture[i].km)+"\t"+str(ListVoiture[i].nbrplace))
    
    print("Les monospaces disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Nbr places"+"\n"+
    "..............................................................................................")
    for i in range(len(ListMonospace)):
        print(ListMonospace[i].nom+"\t"+ListMonospace[i].model+"\t"+str(ListMonospace[i].annee)+"\t"+ListMonospace[i].matricule+"\t"+
        str(ListMonospace[i].km)+"\t"+str(ListMonospace[i].nbrplace))
    
    print("Les utilitaires disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Volume"+"\n"+
    "..............................................................................................")
    for i in range(len(ListUtilitaire)):
        print(ListUtilitaire[i].nom+"\t"+ListUtilitaire[i].model+"\t"+str(ListUtilitaire[i].annee)+"\t"+ListUtilitaire[i].matricule+"\t"+
        str(ListUtilitaire[i].km)+"\t"+str(ListUtilitaire[i].volume))
    
    print("Les camions disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Tonnage"+"\n"+
    "..............................................................................................")
    for i in range(len(ListCamion)):
        print(ListCamion[i].nom+"\t"+ListCamion[i].model+"\t"+str(ListCamion[i].annee)+"\t"+ListCamion[i].matricule+"\t"+
        str(ListCamion[i].km)+"\t"+str(ListCamion[i].tonnage))

    vehicule1 = input("Veuillez saisir le matricule du véhicule: ")

    for i in range(len(ListVoiture)):
        if str(ListVoiture[i].matricule) == str(vehicule1) :
            return (ListVoiture[i].matricule)
    
    for i in range(len(ListMonospace)):
        if str(ListMonospace[i].matricule) == str(vehicule1) :
            return (ListMonospace[i].matricule)
    
    for i in range(len(ListUtilitaire)):
        if str(ListUtilitaire[i].matricule) == str(vehicule1) :
            return (ListUtilitaire[i].matricule)

    for i in range(len(ListCamion)):
        if str(ListCamion[i].matricule) == str(vehicule1) :
            return (ListCamion[i].matricule)

mapClass = {
   "personne.txt" : Personne,"voiture.txt" : Voiture,"monospace.txt" : Monospace,"camion.txt":Camion,"utilitaire.txt":Utilitaire,"location.txt":Location
}
mapClass1 = {
    "personne.txt" : ListPers,"voiture.txt" : ListVoiture,"monospace.txt" : ListMonospace,"camion.txt":ListCamion,"utilitaire.txt":ListUtilitaire,"location.txt":ListLocation
}

def fileToObject(fileName:str ) :
    f = open(fileName,"r")
    lignes = f.readlines()
    for ligne in (lignes):
        ligne = ligne[0:-1] 
        instance = mapClass[fileName].load(ligne)
        mapClass1[fileName].append(instance) 
    f.close()

def existFile(fileName:str):
    try:
        f = open(fileName,"r")
        fileToObject(fileName)
    except :
        f = open(fileName,"x")
        f.close()

existFile("personne.txt")
existFile("voiture.txt")
existFile("monospace.txt")
existFile("utilitaire.txt")
existFile("camion.txt")

os.remove("personne.txt")
os.remove("voiture.txt")
os.remove("monospace.txt")
os.remove("utilitaire.txt")
os.remove("camion.txt")

def CheckLocation():
    return not(len(ListPers) == 0 or len(ListVoiture) == 0 and len(ListUtilitaire) == 0 and len(ListCamion) == 0 and len(ListMonospace) == 0)


def displayMsg():
    print("Saisissez A pour ajouter un client."+"\n"+"Saisissez B pour ajouter une voiture."+"\n"+
            "Saisissez C pour ajouter un monospace."+"\n"+"Saisissez D pour ajouter un utilitaire."+"\n"+
            "Saisissez E pour ajouter un camion.")
    if CheckLocation():
        print("Saisissez F pour ajouter une location.")


def save(fileName :str, lst: list[Serialize]):
    f = open(fileName,"a",encoding='utf-8')
    for i in range(len(lst)):
        f.write(lst[i].stringify())
    f.close()           

print("Bienvenue au menu d'enregistrement de l'agence  :")

while True:
    displayMsg()
    x = input("Veuillez faire votre saisie, ou ok pour quitter: ")
    if x == "ok":
        save("personne.txt",ListPers)
        save("voiture.txt",ListVoiture)
        save("utilitaire.txt",ListUtilitaire)
        save("monospace.txt",ListMonospace)
        save("camion.txt",ListCamion)
        save("location.txt",ListLocation)
        break
    if x != "A" and x != "B" and x != "C" and x != "D" and x != "E" and  x != "F":
        print("Votre choix n'est pas sur la liste !")
        continue
    if x == "F" and not CheckLocation() : 
        print("Votre choix n'est pas sur la liste !")
        continue
    if x == "A":
        SaisiePers()
    if x == "B":
        SaisieVoiture()
    if x == "C":
        SaisieMonospace()
    if x == "D":
        SaisieUtilitaire()
    if x == "E":
        SaisieCamion()
    if x == "F" :
        SaisieLocation()

def displayArray(list) :
    for i in  range(len(list)):
        return list[i]

CheckLocation()

#displayArray(ListPers)
#displayArray(ListVoiture)
#displayArray(ListUtilitaire)
#displayArray(ListMonospace)
#displayArray(ListCamion)
#displayArray(ListLocation)








