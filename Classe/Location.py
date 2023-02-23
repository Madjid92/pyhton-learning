from Vehicule import Vehicule
from Voiture import Voiture
from Personne import Personne
from Serialize import Serialize
import datetime

class Location(Serialize):
    def __init__(self, code, client: Personne, vehicule: Vehicule):
        self.code = code
        self.client = client
        self.vehicule = vehicule
    def __str__(self)->str:
        return ("Code location: "+self.code + "\n" +str(self.client)+ "\n" + str(self.vehicule)) 

    def stringify(self):
        return (self.code + "\t" +str(self.client)+ "\t" + str(self.vehicule)+"\n")
    
    def load(locStr :str):
        locList = locStr.split('\t')
        loc = Location(locList[0],Personne.searchPers(locList[1]),Vehicule.searchVehic(locList[2]))
        return loc


if __name__ == '__main__':
    
    client = Personne('test','test',"23-02-1992")
    voiture = Voiture('test', 'test',  "2010",'test', 200000, 4)
    loc1 = Location("adhgcf",client,voiture)
    print(loc1)
