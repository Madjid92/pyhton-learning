from Vehicule import Vehicule
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


"""
if __name__ == '__main__':
    
    client = Personne('test','test',"23-02-1992")
    voiture = Voiture('test', 'test',  "2010",'test', 200000, 4)
    loc1 = Location("adhgcf",client,voiture)
    print(loc1)
"""