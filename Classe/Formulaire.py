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

savedFilesDirName = "./savedFiles/"

def displayArray(map:dict) :
    for i in  map:
        print(map[i])

mapIdPers = {}
def SaisiePers():
    nom = input("Saisissez le nom de la personne : ")
    prenom = input("Saisissez le prénom de la personne : ")
    naissance = input("Saisissez la date de naissance de la personne : ")
    pers = Personne(nom,prenom,naissance)
    mapIdPers[pers.id]=pers
    return pers

mapIdVoit = {}
def SaisieVoiture():
    nom = input("Saisissez le nom de la voiture: ")
    model = input("Saisissez le model de la voiture: ")
    annee = input("Saisissez l'année de la voiture: ")
    matricule = input("Saisissez le matricule de la voiture: ")
    km = input("Saisissez le kilométrage de la voiture: ")
    nbrplace = input("Saisissez le nombre de places de la voiture: ")
    voit = Voiture(nom,model,annee,matricule,km,nbrplace)
    mapIdVoit[voit.matricule] = voit
    return voit

mapIdUtil = {}
def SaisieUtilitaire():
    nom = input("Saisissez le nom de l'utilitaire: ")
    model = input("Saisissez le model de l'utilitaire: ")
    annee = input("Saisissez l'année de l'utilitaire: ")
    matricule = input("Saisissez le matricule de l'utilitaire: ")
    km = input("Saisissez le kilométrage de l'utilitaire: ")
    volume = input("Saisissez le volume de l'utilitaire: ")
    util = Utilitaire(nom,model,annee,matricule,km,volume)
    mapIdUtil[util.matricule] = util
    return util

mapIdMono = {}
def SaisieMonospace():
    nom = input("Saisissez le nom du monospace: ")
    model = input("Saisissez le model du monospace: ")
    annee = input("Saisissez l'année du monospace: ")
    matricule = input("Saisissez le matricule du monospace: ")
    km = input("Saisissez le kilométrage du monospace: ")
    nbrplace = input("Saisissez le nombre de places du monospace: ")
    space = Monospace(nom,model,annee,matricule,km,nbrplace)
    mapIdMono[space.matricule] = space
    return space
    
mapIdCam = {}
def SaisieCamion():
    nom = input("Saisissez le nom du camion: ")
    model = input("Saisissez le model du camion: ")
    annee = input("Saisissez l'année du camion: ")
    matricule = input("Saisissez le matricule du camion: ")
    km = input("Saisissez le kilométrage du camion: ")
    tonnage = input("Saisissez le tonnage du camion: ")
    truck = Camion(nom,model,annee,matricule,km,tonnage)
    mapIdCam[truck.matricule] = truck
    return truck

mapIdLoc = {}
def SaisieLocation():
    code = input("Saisissez le code de la location: ")
    client = ChoosePers()
    vehicule = ChooseCar()
    loc = Location(code,client,vehicule)
    mapIdLoc[loc.code] = loc
    return loc


def ChoosePers():
    print("ID"+"\t"+"Nom"+"\t"+"Prénom"+"\t"+"Date de naissance"+"\n"+
    "..........................................................")
    for i in mapIdPers:
        print(str(mapIdPers[i].id)+"\t"+mapIdPers[i].nom+"\t"+mapIdPers[i].prenom+"\t"+str(mapIdPers[i].naissance))
    client1 = input("Veuillez séléctionner l'ID du client: ")
    return mapIdPers[str(client1)]


def ChooseCar():
    mapIdVehic = { **mapIdVoit, **mapIdMono, **mapIdUtil, **mapIdCam}
    print("Les voitures disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Nbr places"+"\n"+
    "..............................................................................................")
    for i in mapIdVoit:
        print(mapIdVoit[i].nom+"\t"+mapIdVoit[i].model+"\t"+str(mapIdVoit[i].annee)+"\t"+mapIdVoit[i].matricule+"\t"+
        str(mapIdVoit[i].km)+"\t"+str(mapIdVoit[i].nbrplace))
    
    print("Les monospaces disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Nbr places"+"\n"+
    "..............................................................................................")
    for i in mapIdMono:
        print(mapIdMono[i].nom+"\t"+mapIdMono[i].model+"\t"+str(mapIdMono[i].annee)+"\t"+mapIdMono[i].matricule+"\t"+
        str(mapIdMono[i].km)+"\t"+str(mapIdMono[i].nbrplace))
    
    print("Les utilitaires disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Volume"+"\n"+
    "..............................................................................................")
    for i in mapIdUtil:
        print(mapIdUtil[i].nom+"\t"+mapIdUtil[i].model+"\t"+str(mapIdUtil[i].annee)+"\t"+mapIdUtil[i].matricule+"\t"+
        str(mapIdUtil[i].km)+"\t"+str(mapIdUtil[i].volume))
    
    print("Les camions disponibles à la location: "+"\n"+"Marque"+"\t"+"model"+"\t"+"Année"+"\t"+"Matricule"+"\t"+"Kilométrage"+"\t"+"Tonnage"+"\n"+
    "..............................................................................................")
    for i in mapIdCam:
        print(mapIdCam[i].nom+"\t"+mapIdCam[i].model+"\t"+str(mapIdCam[i].annee)+"\t"+mapIdCam[i].matricule+"\t"+
        str(mapIdCam[i].km)+"\t"+str(mapIdCam[i].tonnage))

    vehicule1 = input("Veuillez saisir le matricule du véhicule: ")
    
    return mapIdVehic[vehicule1]


mapClass = {
   "personne.txt" :{
    "className" : Personne
    },
   "voiture.txt" :{
    "className" :Voiture
    },
    "monospace.txt" :{
    "className" :Monospace
    },
    "utilitaire.txt" :{
    "className" :Utilitaire
    },
    "camion.txt":{
    "className" :Camion
    }
}


def fileToObject(fileName:str ) :
    f = open(savedFilesDirName+fileName,"r")
    lignes = f.readlines()
    for ligne in (lignes):
        ligne = ligne[0:-1] 
        instance = mapClass[fileName]["className"].load(ligne)
        if type(instance) == Personne:
            mapIdPers[str(instance.id)] = instance
        if type(instance) == Voiture:
            mapIdVoit[instance.matricule] = instance
        if type(instance) == Utilitaire:
            mapIdUtil[instance.matricule] = instance
        if type(instance) == Monospace:
            mapIdMono[instance.matricule] = instance
        if type(instance) == Camion:
            mapIdCam[instance.matricule] = instance
    f.close()


def loadLocation() :
    mapIdVehic = { **mapIdVoit, **mapIdMono, **mapIdUtil, **mapIdCam}
    try:
        os.path.exists(savedFilesDirName+"location.txt")
        f = open(savedFilesDirName+"location.txt","r")
        lignes = f.readlines()
        for ligne in (lignes):
            ligne = ligne[0:-1]
            locList = ligne.split('\t')
            pers = mapIdPers[str(locList[1])]
            vehi = mapIdVehic[locList[2]]
            loc = Location(locList[0],pers,vehi)
            mapIdLoc[loc.code] = loc
        f.close()
    except:
        pass 


def existFile(fileName:str):
    try:
        os.path.exists(savedFilesDirName+fileName)
        fileToObject(fileName)
    except:
        pass 
    

existFile("personne.txt")
existFile("voiture.txt")
existFile("monospace.txt")
existFile("utilitaire.txt")
existFile("camion.txt")

loadLocation()


def checkLoc():
    mapIdVehic = { **mapIdVoit, **mapIdMono, **mapIdUtil, **mapIdCam}
    if len(mapIdPers)!=0 and len(mapIdVehic)!=0:
        return True

    
def displayMsg():
    print("Saisissez A pour ajouter un client."+"\n"+"Saisissez B pour ajouter une voiture."+"\n"+
            "Saisissez C pour ajouter un monospace."+"\n"+"Saisissez D pour ajouter un utilitaire."+"\n"+
            "Saisissez E pour ajouter un camion.")
    if checkLoc():
        print("Saisissez F pour ajouter une location.")


def save(fileName :str, map:dict):
    if fileName == "location.txt":
        f = open(savedFilesDirName+fileName,"a",encoding='utf-8')
        for i in map:
            f.write(map[i].stringify())
        f.close()
    else:
        f = open(savedFilesDirName+fileName,"w",encoding='utf-8')
        for i in map:
            f.write(map[i].stringify())
        f.close()           

print("Bienvenue au menu d'enregistrement de l'agence  :")

while True:
    displayMsg()
    x = input("Veuillez faire votre saisie, ou ok pour quitter: ")
    if x == "ok":
        save("personne.txt",mapIdPers)
        save("voiture.txt",mapIdVoit)
        save("utilitaire.txt",mapIdUtil)
        save("monospace.txt",mapIdMono)
        save("camion.txt",mapIdCam)
        save("location.txt",mapIdLoc)
        break
    if x != "A" and x != "B" and x != "C" and x != "D" and x != "E" and  x != "F":
        print("Votre choix n'est pas sur la liste !")
        continue
    if x == "F" and not checkLoc() : 
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

#displayArray(mapIdPers)
#displayArray(mapIdVoit)
#displayArray(mapIdUtil)
#displayArray(mapIdMono)
#displayArray(mapIdCam)
#displayArray(mapIdLoc)
#displayArray(mapIdVehic)







