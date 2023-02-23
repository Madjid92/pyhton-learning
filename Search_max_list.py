from Max_Min import max


def userListInput():
    liste = []
    while True:
        x = input("Saisir un nombre entier  sinon ok pour quiter :")
        if x == 'ok':
            break
        try :
            x = int(x)
            liste.append(x)
        except :
            print('le nombre que vous avez saisie n\'est pas un entier')
    return liste

userList = userListInput()
print(userList)
print("Max: ",max(userList))

