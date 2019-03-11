class Pesan(object):
	"""docstring for ClassName"""
	def __init__(self, p):
		self.pesan=p

	def apakahTerkandung(self, cari):
		if cari in self.pesan:
			return True
		else:
			return False
	def hitungKonsonan(self):
		jml=0
		vokal="AaIiUuEeOo"
		for huruf in self.pesan:
			if huruf not in vokal:
				jml+=1
		return jml

	def hitungVokal(self):
		jml=0
		vokal="AaIiUuEeOo"
		for huruf in self.pesan:
			if huruf in vokal:
				jml+=1
		return jml

p9=Pesan("Surakarta")
#print(p9.hitungKonsonan()) # 5
print(p9.hitungVokal()) # 5
