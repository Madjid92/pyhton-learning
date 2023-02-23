from Serialize import Serialize

class Vehicule(Serialize):
    def __init__(self, nom, model, annee, matricule, km):
        self.nom = nom
        self.model = model
        self.annee = annee
        self.matricule = matricule
        self.km = km
    def __str__(self) -> str:
        return ("Marque: "+self.nom +"\n"+"Model: "+self.model+"\n"+"Année: "+self.annee+"\n"+
        "Matricule: "+self.matricule+"\n"+"Kilométrage: "+str(self.km)+" km")
    def stringify(self):
        return (self.nom +"\t"+self.model+"\t"+self.annee+"\t"+self.matricule+"\t"+str(self.km))

    def load(vehiculeStr :str):
            vehiculetList = vehiculeStr.split('\t')
            vehic = Vehicule(vehiculetList[0],vehiculetList[1],vehiculetList[2],vehiculetList[3],vehiculetList[4])
            return vehic
    
    def searchVehic(matricule:str) :
        f = open("utilitaire.txt","r")
        lignes = f.readlines()
        for ligne in (lignes):
            ligne = ligne[0:-1]
            ligne = ligne.split('\t')
            if ligne[3] == str(matricule):
                Vehic = Vehicule(ligne[0],ligne[1],ligne[2],ligne[3],ligne[4])
                return Vehic



   
