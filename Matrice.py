matier = ['math','Français','physique', 'chimie']
eleves = ['Lyes','Dahman','Madjid','Amine', 'Syphax']
m = [[10,11,2,5],[13,16,4,8],[13,9,11,2],[7,18,10,4],[7,7,18,10]]

cours = ""
for i in range(len(matier)):
    cours = cours+"\t"+matier[i]+"    "
print(cours)
print("----------------------------------------------------------------")


'''eleve = 0
noteeleve = ""
while True:
    eleve < len(eleves)
    for i in range(len (m[i])) :     
        noteeleve = noteeleve + "\t" + str(m[eleve][i]) + "\t"
    print(eleves[eleve],noteeleve)
    eleve = eleve+1
    if eleve > len(eleves):
        break
print("----------------------------------------------------------------")'''





for j in range(len(m)) : 
    noteeleve = ""
    for i in range(len(m[j])) :     
        noteeleve = noteeleve + "\t" + str(m[j][i]) + "\t"
    print(eleves[j],noteeleve)




