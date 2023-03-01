
from Voiture import Voiture
maptest = {}


voit = Voiture('test','test','1990','AAA-BBBB', 170, 7)

maptest[voit.matricule]= voit

print(maptest)
print(maptest['AAA-BBBB'])

print(type(voit) == int)