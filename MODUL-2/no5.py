class Manusia(object):
	""" Class Manusia dengan inisial nama"""
	keadaan="lapar"	
	def __init__(self, nama):
		self.nama=nama

	def ucapkanSalam(self):
		print("Salam, Namaku ", self.nama)

	def makan(self, s):
		print("Saya baru saja makan ", self.s)
		keadaan="kenyang"

	def olahraga(self, k):
		print("Saya baru saja latihan ", k)
		keadaan="lapar"

	def mengalikanDenganDua(self, n):
		return n*2

class Mahasiswa(Manusia):
	"""docstring for Mahasiswa"""
	listkuliah=[]
	def __init__(self, nama, nim, kota, us):
		"""Metode inisiai ini menutupi metode inisiasi class di atas"""
		self.nama=nama
		self.nim=nim
		self.kota=kota
		self.uangSaku=us

	def __str__():
		s=self.nama + ", NIM " + nim \
		+  ". Tinggal di "+ self.kota \
		+  ". Uang Saku Rp " +str(self.uangSaku) \
		+ " tiap bulannya"

		return s

	def ambilNama(self):
		return self.nama

	def ambilNim(self):
		return self.nim

	def ambilUangSaku(self):
		return self.uangSaku

	def ambilKotaTinggal(self):
		return self.kota

	def makan(self, s):
		""" Metode ini Menutupi metode makannya class manusia"""
		print("Saya baru saja makan ", s, " Sambil Belajar")
		self.keadaan='kenyang'

	def perbaruiKotaTinggal(self, kotaBaru):
		self.kota=kotaBaru

	def tambahUangSaku(self, tmbhUang):
		if type(tmbhUang) is not int: raise ValueError("Data Harus INT")
		self.uangSaku+=tmbhUang

	def ambilKuliah(self, kuliah):
		self.listkuliah.append(kuliah)
		return self.listkuliah

	def hapusKuliah(self, indexing):
		self.listkuliah.append(indexing, None)

mahasiswa=Mahasiswa("Bintang", "L200170078", "Boyolali", 100000)
print(mahasiswa.listkuliah)

mahasiswa.ambilKuliah("Teknik Informatika")
mahasiswa.ambilKuliah("Komunikasi")
print(mahasiswa.listkuliah)
print("Data dihitung dari kiri,\nperhitungan mulai dari 0")
mahasiswa.hapusKuliah(0)
print(mahasiswa.listkuliah)
