class Pesan(object):
	"""docstring for ClassName"""
	def __init__(self, p):
		self.pesan=p

	def apakahTerkandung(self, cari):
		if cari in self.pesan:
			return True
		else:
			return False
p9=Pesan("Indonesia adalah negeri yang indah")
print(p9.apakahTerkandung("ege")) # True
print(p9.apakahTerkandung("eka")) # False
