from Personne import Personne
from Vehicule import Vehicule
from Voiture import Voiture
from Utilitaire import Utilitaire
from Monospace import Monospace
from Camion import Camion
from Location import Location
from DataManger import DataManager
import os

savedFilesDirName = "./savedFiles/"

class FileManager(DataManager) :
    
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

    typetoMap = {
        Personne : mapIdPers,
        Voiture : mapIdVoit,
        Utilitaire : mapIdUtil,
        Camion : mapIdCam,
        Monospace : mapIdMono,
        Location : mapIdLoc
    } 

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

    def saveOnFile(fileName :str, map:dict):
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
        
    def init():
        FileManager.existFile("personne.txt")
        FileManager.existFile("voiture.txt")
        FileManager.existFile("monospace.txt")
        FileManager.existFile("utilitaire.txt")
        FileManager.existFile("camion.txt")

        FileManager.loadLocation()

    def getAll(dataType) :
        return FileManager.typetoMap[dataType]
    

    def saveAll():
        classes = list(FileManager.typetoMap.keys())
        for i in range(len(classes)) :
            currentClass= classes[i]
            currentDataMap = FileManager.typetoMap[currentClass]
            if(len(currentDataMap) == 0) :
                continue
            FileManager.saveOnFile(currentClass.name+".txt",currentDataMap)
    
    def save(data):
        typeData = type(data) 
        idattrName = 'id' if typeData == Personne else 'code' if typeData == Location else 'matricule'
        idVal = getattr(data, idattrName)
        dataMap = FileManager.typetoMap[typeData]
        dataMap[idVal] = data
    
    def getById(id, dataType):   
        data = FileManager.typetoMap[dataType][id]
        return data
        

