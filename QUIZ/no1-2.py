class Mahasiswa():
    def __init__(self, nama):
        self.nama = nama

    def __str__(self):
        return str(self.nama)

def mgshort(listData):
	if len(listData) > 1:
		tengah=len(listData)//2
		kiri=listData[:tengah]
		kanan=listData[tengah:]

		mgshort(kiri)
		mgshort(kanan)

		i=0
		j=0
		k=0

		while i < len(kiri) and j < len(kanan):
			if kiri[i].nama < kanan[j].nama:
				listData[k]=kiri[i]
				i=i+1
			else:
				listData[k]=kanan[j]
				j=j+1
			k=k+1

		while i < len(kiri):
			listData[k]=kiri[i]
			i=i+1
			k=k+1

		while j < len(kanan):
			listData[k]=kanan[j]
			j=j+1
			k=k+1
def tampilDaftar(listData):
	for i in listData:
		print(i.nama)

Mhs1=Mahasiswa("Agus")
Mhs2=Mahasiswa("Bagus")
Mhs3=Mahasiswa("Carrol")
Mhs4=Mahasiswa("Dani")
Mhs5=Mahasiswa("Edward")
Mhs6=Mahasiswa("Ferro")
Mhs7=Mahasiswa("Gusdur")
Mhs8=Mahasiswa("Halim")
Mhs9=Mahasiswa("Izwan")
Mhs10=Mahasiswa("Jali")


DaftarMahasiswa = [Mhs2,Mhs1,Mhs4,Mhs3,Mhs9,Mhs10,Mhs8,Mhs6,Mhs7,Mhs5]

# print("Sebelum di Merge\n")
# tampilDaftar(DaftarMahasiswa)
# print("\n")
# print("Setelah di Merge\n")
mgshort(DaftarMahasiswa)
# tampilDaftar(DaftarMahasiswa)


# NO 2
class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item=[]

	def isEmpty(self):
		return len(self)==0

	def __len__(self):
		return len(self.item)

	def peek(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.items[-1]

	def pop(self):
		assert not self.isEmpty(), "Stack is Empty"
		return self.item.pop()

	def push(self, data):
		self.item.append(data)
myStack=Stack()
myStack.push(DaftarMahasiswa[0])
myStack.push(DaftarMahasiswa[1])
myStack.push(DaftarMahasiswa[2])
myStack.push(DaftarMahasiswa[3])
myStack.push(DaftarMahasiswa[4])
myStack.push(DaftarMahasiswa[5])
myStack.push(DaftarMahasiswa[6])
myStack.push(DaftarMahasiswa[7])
myStack.push(DaftarMahasiswa[8])
myStack.push(DaftarMahasiswa[9])


# print(myStack.pop())
# print(myStack.item[8])
