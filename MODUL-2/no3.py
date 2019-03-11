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

def Menu():
	print("=======================")
	print("Menu Aplikasi Mahasiswa")
	print("=======================")
	print("[1] Input Data")
	print("[2] Edit  Data")
	print("[0] Keluar")
	print("=======================")

def MenuInput():
	print("=======================")
	print("Input Data Mahasiswa")
	print("=======================")

def MenuEdit():
	print("=======================")
	print("Edit Data Mahasiswa")
	print("=======================")	
keluar=0
data=None
while keluar != 1:
	Menu()
	menu=int(input("Pilih Menu :"))
	if menu is 1:
		print("\n")
		MenuInput()
		nama=str(input("Nama          :"))
		nim=str(input("NIM           :"))
		kota=str(input("Kota Tinggal  :"))
		uang=int(input("Uang saku     :"))

		data=Mahasiswa(nama, nim, kota, uang)
		tampil=str(input("Data Berhasil di Inputkan.\nTampilkan (y/n) :"))
		if tampil is "y" or "Y":
			print("\n")
			print("=======================")
			print("Data Mahasiswa")
			print("=======================")
			print("Nama          :", data.ambilNama())
			print("NIM           :", data.ambilNim())
			print("Kota Tinggal  :", data.ambilKotaTinggal())
			print("Uang saku     :", data.ambilUangSaku())
			print("=======================")
			lanjut=str(input("Lanjut Program ?(y/n)"))
			if lanjut is "y":
				""""""
				print("\n")
			elif lanjut is "n":
				print("Keluar..")
				keluar=1
	elif menu is 2:
		if data is None:
			print("Belum Input Data...")
			print("\n")
		print("\n")
		MenuEdit()
		print("EDIT KOTA & TAMBAH UANG SAKU")
		print("Ganti Kota Tinggal dan\nIsi Uang saku bila ingin menambah uang saku")		
		kota=str(input("Kota Tinggal  :"))
		uang=int(input("Uang saku     :"))

		data.perbaruiKotaTinggal(kota)
		data.tambahUangSaku(uang)
		tampil=str(input("Data Berhasil di Perbarui.\nTampilkan (y/n) :"))
		if tampil is "y" or "Y":
			print("\n")
			print("=======================")
			print("Data Mahasiswa")
			print("=======================")
			print("Nama          :", data.ambilNama())
			print("NIM           :", data.ambilNim())
			print("Kota Tinggal  :", data.ambilKotaTinggal())
			print("Uang saku     :", data.ambilUangSaku())
			print("=======================")
			lanjut=str(input("Lanjut Program ?(y/n)"))
			if lanjut is "y":
				""""""
				print("\n")
			elif lanjut is "n":
				print("Keluar..")
				keluar=1
	elif menu is 0:

		print("Keluar...")
		keluar=1