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
from FilesManager import FileManager


def displayArray(map:dict) :
    for i in  map:
        print(map[i])

def SaisiePers():
    nom = input("Saisissez le nom de la personne : ")
    prenom = input("Saisissez le prénom de la personne : ")
    naissance = input("Saisissez la date de naissance de la personne : ")
    return Personne(nom,prenom,naissance)

def SaisieVoiture():
    nom = input("Saisissez le nom de la voiture: ")
    model = input("Saisissez le model de la voiture: ")
    annee = input("Saisissez l'année de la voiture: ")
    matricule = input("Saisissez le matricule de la voiture: ")
    km = input("Saisissez le kilométrage de la voiture: ")
    nbrplace = input("Saisissez le nombre de places de la voiture: ")
    return Voiture(nom,model,annee,matricule,km,nbrplace)

def SaisieUtilitaire():
    nom = input("Saisissez le nom de l'utilitaire: ")
    model = input("Saisissez le model de l'utilitaire: ")
    annee = input("Saisissez l'année de l'utilitaire: ")
    matricule = input("Saisissez le matricule de l'utilitaire: ")
    km = input("Saisissez le kilométrage de l'utilitaire: ")
    volume = input("Saisissez le volume de l'utilitaire: ")
    util = Utilitaire(nom,model,annee,matricule,km,volume)
    return util

def SaisieMonospace():
    nom = input("Saisissez le nom du monospace: ")
    model = input("Saisissez le model du monospace: ")
    annee = input("Saisissez l'année du monospace: ")
    matricule = input("Saisissez le matricule du monospace: ")
    km = input("Saisissez le kilométrage du monospace: ")
    nbrplace = input("Saisissez le nombre de places du monospace: ")
    mono = Monospace(nom,model,annee,matricule,km,nbrplace)
    return mono
    
def SaisieCamion():
    nom = input("Saisissez le nom du camion: ")
    model = input("Saisissez le model du camion: ")
    annee = input("Saisissez l'année du camion: ")
    matricule = input("Saisissez le matricule du camion: ")
    km = input("Saisissez le kilométrage du camion: ")
    tonnage = input("Saisissez le tonnage du camion: ")
    truck = Camion(nom,model,annee,matricule,km,tonnage)
    return truck

def SaisieLocation():
    code = input("Saisissez le code de la location: ")
    client = ChoosePers()
    vehicule = ChooseCar()
    loc = Location(code,client,vehicule)
    return loc

def ChoosePers():
    print("ID"+"\t"+"Nom"+"\t"+"Prénom"+"\t"+"Date de naissance"+"\n"+
    "..........................................................")
    mapIdPers = FileManager.getAll(Personne)
    for i in mapIdPers:
        print(str(mapIdPers[i].id)+"\t"+mapIdPers[i].nom+"\t"+mapIdPers[i].prenom+"\t"+str(mapIdPers[i].naissance))
    client1 = input("Veuillez séléctionner l'ID du client: ")
    return mapIdPers[str(client1)]

def ChooseCar():
    mapIdVoit = FileManager.getAll(Voiture)
    mapIdMono = FileManager.getAll(Monospace)
    mapIdUtil = FileManager.getAll(Utilitaire)
    mapIdCam = FileManager.getAll(Camion)
    mapIdVehic = { **FileManager.getAll(Voiture), 
                  **FileManager.getAll(Monospace),
                **FileManager.getAll(Utilitaire),
                      **FileManager.getAll(Camion)}
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

def displayMsg():
    print("Saisissez A pour ajouter un client."+"\n"+"Saisissez B pour ajouter une voiture."+"\n"+
            "Saisissez C pour ajouter un monospace."+"\n"+"Saisissez D pour ajouter un utilitaire."+"\n"+
            "Saisissez E pour ajouter un camion.")
    if  FileManager.checkLoc():
        print("Saisissez F pour ajouter une location.")       

print("Bienvenue au menu d'enregistrement de l'agence  :")


def Saiasie( x) :
    if x == "A": 
       return SaisiePers()
    if x == "B":
        return SaisieVoiture()
    if x == "C":
        return SaisieMonospace()
    if x == "D":
        return SaisieUtilitaire()
    if x == "E":
        return SaisieCamion()
    if x == "F" :
        return SaisieLocation()

FileManager.init()

while True:
    displayMsg()
    x = input("Veuillez faire votre saisie, ou ok pour quitter: ")
    if x == "ok":
        FileManager.saveAll()
        break
    if x != "A" and x != "B" and x != "C" and x != "D" and x != "E" and  x != "F":
        print("Votre choix n'est pas sur la liste !")
        continue
    if x == "F" and not FileManager.checkLoc() : 
        print("Votre choix n'est pas sur la liste !")
        continue
    data = Saiasie(x)
    FileManager.save(data)
    

#displayArray(mapIdPers)
#displayArray(mapIdVoit)
#displayArray(mapIdUtil)
#displayArray(mapIdMono)
#displayArray(mapIdCam)
#displayArray(mapIdLoc)
#displayArray(mapIdVehic)







