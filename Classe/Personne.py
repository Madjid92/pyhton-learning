from datetime import datetime
from Serialize import Serialize
class Personne(Serialize):
    count = 0
    name = "personne"
    def __init__(self, nom : str = '', prenom :str = '', naissance : str ='1-1-1900'):
        Personne.count = Personne.count+1
        self.id = Personne.count
        self.nom = nom
        self.prenom = prenom
        self.naissance = datetime.strptime(naissance, '%d-%m-%Y').date()

    def load(persStr :str):
        pertList = persStr.split('\t')
        pers = Personne(pertList[1],pertList[2],pertList[3])
        pers.id = int(pertList[0])
        return pers
        

        
    def __str__(self):
        return ("ID: "+str(self.id) + "\n" + "Nom: "+self.nom + "\n" + "Prénom: "+self.prenom + "\n" + "Date de naissance: "+str(self.naissance))
   
    def stringify(self):
        strDate = str(self.naissance.day)+"-"+str(self.naissance.month)+"-"+str(self.naissance.year)
        return (str(self.id)+"\t"+self.nom+"\t"+self.prenom+"\t"+strDate+"\n")
  

if __name__ == '__main__':
    client1 = Personne( nom="Imzi",prenom="Lyes", naissance='23-02-1992')
    print(client1)
    print(client1.stringify())

