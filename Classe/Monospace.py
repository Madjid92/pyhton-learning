from Vehicule import Vehicule


class Monospace (Vehicule):
    name = "monospace"
    def __init__(self, nom, model, annee, matricule, km, nbrplace):
        self.nbrplace = nbrplace
        super().__init__(nom, model, annee, matricule, km)
    def __str__(self):
        return super().__str__()+"\n"+"Nombre de places: "+str(self.nbrplace)
    def stringify(self):
        return super().stringify()+"\t"+str(self.nbrplace)+"\n"

    def load(monospaceStr):
        monospaceList = monospaceStr.split("\t")
        mono = Vehicule.load(monospaceStr)
        return Monospace(mono.nom,mono.model,mono.annee,mono.matricule,mono.km,monospaceList[5])
    

if __name__ == '__main__':
    V = Monospace("Peugeot","5008","2018","A145HINO","230000",7)
    print(V)