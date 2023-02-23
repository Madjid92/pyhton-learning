
lettres = input("Insérez une suite de letters séparées par une (,): ")
list=lettres.split(",")
print(list)
mot = input("insérez le mot que vous voulez composer: ")
print(mot)

find = True

for i in range(len(mot)):
    for j in range(len(list)):
        if(mot[i] == list[j]):
            break
        if( j == len(list)-1):
            find = False
            break

    if(not find):
        break

if(find):
    print("Mot trouver")
else :
    print("Mot non trouver")


"""

lettres = input("Insérez une suite de letters séparées par une (,): ")
list=lettres.split(",")
print(list)
mot = input("insérez le mot que vous voulez composer: ")
print(mot)
test=0
for i in range(len(mot)):
    for j in range(len(list)):
        if mot[i] == list[j]:
            test=test+1
        
print(test)
if test==len(mot):
    print("Bravo !")
else:
    print("Le mot ne peut être composé !")
"""
"""
lettres = input("Insérez une suite de letters séparées par une (,): ")
list=lettres.split(",")
print(list)
mot = input("insérez le mot que vous voulez composer: ")
print(mot)
test=0
for i in range(len(mot)-1):
    for j in range(len(list)-1):
        if mot[i] != list[j]:
            try:
                if j == len(list)-1:
                    print("HS")
                    break
            except:
                continue
        else:
            break
"""



            

            

            
        
            
        
                
            
        
    
        
        


