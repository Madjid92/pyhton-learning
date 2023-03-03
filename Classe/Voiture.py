from Vehicule import Vehicule
from Serialize import Serialize

class Voiture (Vehicule):
    name="voiture"
    def __init__(self, nom, model, annee, matricule, km, nbrplace):
        self.nbrplace = nbrplace
        super().__init__(nom, model, annee, matricule, km)

    def __str__(self):
        return super().__str__()+"\n"+"Nombre de places: "+str(self.nbrplace)

    def stringify(self):
        return super().stringify()+"\t"+str(self.nbrplace)+"\n"

    def load(voitureStr):
        voitureList = voitureStr.split("\t")
        voit = Vehicule.load(voitureStr)
        return Voiture(voit.nom,voit.model,voit.annee,voit.matricule,voit.km,voitureList[5])
    

if __name__ == '__main__':
    V = Voiture("Renault","Twingo","2010","ZTF15MP", "21000", 4)
    print(V)

