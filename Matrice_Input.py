def SplitStringToList(m, separtor = ','):
    liste = [] 
    lastindex = 0
    for i in range(len(m)):
        if m[i] == separtor:
            liste.append(m[lastindex:i])
            lastindex = i+1
        if i == len(m)-1:
            liste.append(m[lastindex:len(m)])
    return liste


def scoresnotes(eleves,cours):
    notes_eleves = []
    for j in range(len(eleves)):
        note = []
        for i in range(len(cours)):
            note.append(input("insérez la note de "+eleves[j]+" en "+cours[i]+" :"))
            
        notes_eleves.append(note)
    return notes_eleves



def Moyenne_Ele(notes_eleves):
    Moyennes = []
    for i in range(len(notes_eleves)):
        SommeNote = 0
        for j in range(len(notes_eleves[i])):
            SommeNote = SommeNote+int(notes_eleves[i][j])
        m = SommeNote/len(notes_eleves[i])
        Moyennes.append(m)
    return Moyennes

def Moyenne_Mat(mat):
    s  = [0 for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            s[j] = s[j] + int(mat[i][j])
    return  [s[i]/len(mat) for i in range(len(mat[0]))]


def lessons(cours):
    Matière = ""
    for i in range(len(cours)):
        Matière = Matière+"\t"+cours[i]+"    "
    Matière = Matière+"\t"+"Moyenne/El"
    return Matière



def matricescores(notes_eleves,Moyennes):
    strMatrice = ""
    for j in range(len(notes_eleves)) : 
        noteeleve = ""
        for i in range(len(notes_eleves[j])) :     
            noteeleve = noteeleve + "\t" + str(notes_eleves[j][i]) + "\t"
        strMatrice = strMatrice + eleves[j] + noteeleve + "\t" +str(Moyennes[j])+" \n"
    return strMatrice

    


m = input("Insérez les matières séparées d'une virgule :")
cours = SplitStringToList(m)
m = input("Insérez les éléves séparés d'une virgule :")
eleves = SplitStringToList(m)
print(cours)
print(eleves)

notes_eleves = scoresnotes(eleves,cours)
print(notes_eleves)


Moyennes = Moyenne_Ele(notes_eleves)



tableaucours = lessons(cours)
print(tableaucours)

print("---------------------------------------------------------------------")

print(matricescores(notes_eleves,Moyennes))

Moyennes_mat = Moyenne_Mat(notes_eleves)

display_moy_mat = "AVG \t"
for i in  range(len(Moyennes_mat)) :
    display_moy_mat = display_moy_mat+str(Moyennes_mat[i])+"\t\t"
print(display_moy_mat)
