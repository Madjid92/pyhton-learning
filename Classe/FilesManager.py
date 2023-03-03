from Personne import Personne
from Vehicule import Vehicule
from Voiture import Voiture
from Utilitaire import Utilitaire
from Monospace import Monospace
from Camion import Camion
from Location import Location
import os

savedFilesDirName = "./savedFiles/"

class FileManager :
    
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

    mapIdPers = {}
    mapIdVoit = {}
    mapIdUtil = {}
    mapIdMono = {}
    mapIdCam = {}
    mapIdLoc = {}


    def fileToObject(fileName:str ) :
        f = open(savedFilesDirName+fileName,"r")
        lignes = f.readlines()
        for ligne in (lignes):
            ligne = ligne[0:-1] 
            instance = FileManager.mapClass[fileName]["className"].load(ligne)
            if type(instance) == Personne:
                FileManager.mapIdPers[str(instance.id)] = instance
            if type(instance) == Voiture:
                FileManager.mapIdVoit[instance.matricule] = instance
            if type(instance) == Utilitaire:
                FileManager.mapIdUtil[instance.matricule] = instance
            if type(instance) == Monospace:
                FileManager.mapIdMono[instance.matricule] = instance
            if type(instance) == Camion:
                FileManager.mapIdCam[instance.matricule] = instance
        f.close()

    def loadLocation() :
        mapIdVehic = { **FileManager.mapIdVoit, **FileManager.mapIdMono, **FileManager.mapIdUtil, **FileManager.mapIdCam}
        try:
            os.path.exists(savedFilesDirName+"location.txt")
            f = open(savedFilesDirName+"location.txt","r")
            lignes = f.readlines()
            for ligne in (lignes):
                ligne = ligne[0:-1]
                locList = ligne.split('\t')
                pers = FileManager.mapIdPers[str(locList[1])]
                vehi = mapIdVehic[locList[2]]
                loc = Location(locList[0],pers,vehi)
                FileManager.mapIdLoc[loc.code] = loc
            f.close()
        except:
            pass 

    def existFile(fileName:str):
        try:
            os.path.exists(savedFilesDirName+fileName)
            FileManager.fileToObject(fileName)
        except:
            pass 

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

    def checkLoc():
        mapIdVehic = { **FileManager.mapIdVoit, **FileManager.mapIdMono, **FileManager.mapIdUtil, **FileManager.mapIdCam}
        if len(FileManager.mapIdPers)!=0 and len(mapIdVehic)!=0:
            return True

    def loadAllFiles() :
        FileManager.existFile("personne.txt")
        FileManager.existFile("voiture.txt")
        FileManager.existFile("monospace.txt")
        FileManager.existFile("utilitaire.txt")
        FileManager.existFile("camion.txt")

        FileManager.loadLocation()

    def saveAllFiles():
        FileManager.save("personne.txt",FileManager.mapIdPers)
        FileManager.save("voiture.txt",FileManager.mapIdVoit)
        FileManager.save("utilitaire.txt",FileManager.mapIdUtil)
        FileManager.save("monospace.txt",FileManager.mapIdMono)
        FileManager.save("camion.txt",FileManager.mapIdCam)
        FileManager.save("location.txt",FileManager.mapIdLoc)
        

