class Voiture:
	def __init__(self,nom : str, annee : int, model : str ):
		self.nom : str = nom
		self.annee : int = annee
		self.model : str = model

	
	def __str__(self) -> str:
		return ( "/"+self.nom + '/'+self.model + '/'+str(self.annee))

class Pers:
		def __init__(self,nom , prenom):
			self.nom = nom
			self.prenom = prenom
		def __str__(self) -> str:
			return self.nom+"/"+self.prenom+"/"

class Prop(Pers): 
	def __init__(self,nom , prenom,voiture :Voiture):
		super().__init__(nom , prenom)
		self.voiture = voiture
	def __str__(self) -> str:
		return Pers.__str__(self)+str(self.voiture)


ma_voiture = Voiture(nom = "Ferrari", annee="1970", model="A")
prop = Prop("A", "B",ma_voiture)


print(ma_voiture)
print(prop)