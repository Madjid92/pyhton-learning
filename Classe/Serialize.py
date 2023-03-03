class Serialize:
    name :str = None

    def stringify(self):
        pass

    @classmethod
    def load(parseStr:str):
        pass
    '''def stringifyvoiture(self):
        f = open("TxtVoitures","a")
        f.write(self.nom+"\t"+"\t"+self.model+"\t"+"\t"+self.annee+"\t"+"\t"+self.matricule+"\t"+"\t"+str(self.km)+"\t"+"\t"+str(self.nbrplace)+"\n")
        f.close()
        return self.stringify()+"\t"+str(self.nbrplace)
    def stringifyutilitaire(self):
        f = open("TxtUtilitaires","a")
        f.write(self.nom+"\t"+self.model+"\t"+self.annee+"\t"+self.matricule+"\t"+str(self.km)+"\t"+str(self.volume)+"\n")
        f.close()
        return self.stringify()+"\t"+str(self.volume)
    def stringifycamion(self):
        f = open("TxtCamions","a")
        f.write(self.nom+"\t"+self.model+"\t"+self.annee+"\t"+self.matricule+"\t"+str(self.km)+"\t"+str(self.tonnage)+"\n")
        f.close()
        return self.stringify()+"\t"+str(self.tonnage)
    def stringifymonospace(self):
        f = open("TxtMonospaces","a")
        f.write(self.nom+"\t"+self.model+"\t"+self.annee+"\t"+self.matricule+"\t"+str(self.km)+"\t"+str(self.nbrplace)+"\n")
        f.close()
        return self.stringify()+"\t"+str(self.nbrplace)
'''