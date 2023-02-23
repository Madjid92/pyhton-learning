def max(liste):
    if type(liste) != type([]):
        raise Exception('La variable doit étre une liste')
    max = liste[0]
    i = 1
    while i < len(liste):
        if liste[i] > max:     
            max = liste[i]
        i=i+1
    return max

