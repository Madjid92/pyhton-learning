nbr=int(input("Entrez un nombre pour calculer son factoriel: "))
"""fact=nbr
for i in range(nbr-1):
    fact = fact*(i+1)
print(fact)

fact = 1
while nbr!= 0 :
    fact = fact*nbr
    nbr = nbr-1
print(fact)"""

def fact(nbr):
    if(nbr == 1):
        return 1
    return nbr * fact(nbr-1)
        
print(fact(nbr))



