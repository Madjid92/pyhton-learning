
def modulo(x,y):
    if(x > y): 
        return None
    z = y//x
    m = y - (z*x)
    return m 

if __name__ == '__main__':
    x = None
    y = None

    while True :
        print("La première valeur doit étre inférieure à la deuxième")
        x = int(input("Entrez la première valeur:"))
        y = int(input("Entrez la deuxième valeur:"))
        if(y > x): 
            break
    print(modulo(x,y))
