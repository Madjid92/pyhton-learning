from Vehicule import Vehicule
from Serialize import Serialize

class Camion (Vehicule):
    def __init__(self, nom = "", model = "", annee = "", matricule = "", km = 0, tonnage  = 0):
        self.tonnage = tonnage
        super().__init__(nom, model, annee, matricule, km)
    def __str__(self):
        return super().__str__()+"\n"+"Tonnage: "+str(self.tonnage)+" T"
    def stringify(self):
        return super().stringify()+"\t"+str(self.tonnage)+"\n"

    def load(camionStr):
        camionList = camionStr.split("\t")
        truck = Vehicule.load(camionStr)
        return Camion(truck.nom,truck.model,truck.annee,truck.matricule,truck.km,camionList[5])

if __name__ == '__main__':
    C = Camion("Volvo","FH16","2020","HIY230KY","120000",275)
    print(C)