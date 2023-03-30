from Vehicule import Vehicule

class Utilitaire (Vehicule):
    name = "utilitaire"
    def __init__(self, nom = "", model = "", annee = "", matricule = "", km = 0, volume = 0):
        self.volume = volume
        super().__init__(nom, model, annee, matricule,km)
    def __str__(self):
        return super().__str__()+"\n"+"Volume: "+str(self.volume)+" m3"
    def stringify(self):
        return super().stringify()+"\t"+str(self.volume)+"\n"
    
    def load(utilitaireStr):
        utilitaireList = utilitaireStr.split("\t")
        util = Vehicule.load(utilitaireStr)
        return Utilitaire(util.nom,util.model,util.annee,util.matricule,util.km,utilitaireList[5])
    

if __name__ == '__main__':
    U = Utilitaire("Mercedes-Benz","Sprinter","2019","MB10RDXQ7","210000",17)
    print(U)