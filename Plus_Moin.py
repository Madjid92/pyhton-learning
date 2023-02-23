from random import randrange



print('Cliquez sur entrer pour choisir un nombre aléatoire entre 0 et 50: ')
p = randrange(start= 0, stop=50)
print(p)

'''t = int(input('Entrez un numéro: '))
if t == p:
    print('Bravo, du premier coup !')
else:
    c = 1
    while True:
        c = c+1
        if t > p:
            print("==========")
            t = int(input('mauvaise réponse, essayez une valeur inférieure :'))
        else:
            print("-------------")
            t = int(input('mauvaise réponse, essayez une valeur supérieure :'))
        if t == p:
            print('bravo ! vous avez réussis en', c, 'tentatives') 
            break

'''
c = 0
while True :
    try:
        t = int(input('Entrez un numéro: '))
        c+=1
        if t > p :
            print('Mauvaise réponse, essayez une valeur inférieure')
            continue
        if t < p: 
            print('Mauvaise réponse, essayez une valeur supérieure')
            continue
        print('Bravo ! vous avez réussis en', c, 'tentatives')
        break
    except:
        print('La valaure doit étre un nombre')