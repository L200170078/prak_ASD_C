"""(NO 1)"""
def cetakSiku(x):
    i=1
    while i <= x:
        print("*"*i)
        i+=1
cetakSiku(5)
"""(NO 2)"""
def gambarlahPersegiEmpat(x):
    l=x[1]
    p=x[0]
    jarak=l-4
    i=1
    while i <=l:
        if i==1:
            print("@"*l)
        elif i==l:
            print("@"*l)
        else:
            print("@",(" "*jarak),"@")
        i+=1
gambarlahPersegiEmpat((8,10))
"""(NO 3)"""
"""3a"""
def jumlahHurufVokal(x):
	vokal="AIUEOaiueo"
	jmlhuruf=len(x)
	jmlvokal=0
	for karakter in x:
		if karakter in vokal:
			jmlvokal+=1
	return (jmlhuruf, jmlvokal)
k=jumlahHurufVokal("Surakarta")
print(k)
"""3b"""
def jumlahHurufVokal(x):
	vokal="AIUEOaiueo"
	jmlhuruf=len(x)
	jmlkonsonan=0
	for karakter in x:
		if karakter not in vokal:
			jmlkonsonan+=1
	return (jmlhuruf, jmlkonsonan)
k=jumlahHurufVokal("Surakarta")
print(k)

"""(NO 4)"""
def rerata(x):
	"""Hitung Rata Rata dari List"""
	jml=0
	banyak=0
	for angka in x:
		jml+=angka
		banyak+=1
	return jml/banyak
print(rerata([1,2,3,4,5]))

"""(NO 5)"""
from math import sqrt as sq
def apakahPrima(n):
	n=int(n)
	assert n>=0
	primaKecil=[2,3,5,7,11]
	bukanPriKecil=[0,1,4,6,8,9,10]
	if n in primaKecil:
		return True
	elif n in bukanPriKecil:
		return False
	else:
		# angka=[]
		hasil=[]
		for i in range(2,int(sq(n))+1):
			if i in primaKecil:
				hasil.append(True) 
			elif i in bukanPriKecil:
				hasil.append(False)
			# angka.append(i) 
		return hasil
print(apakahPrima(20))


"""(NO 6)"""
def cetakbilanganprima():
    prim=list()
    for i in range(2,100):
        a = True
        for x in prim:
            if(i%x==0):
                a=False
                break
        if(a):
            print(i)
            prim.append(i)
cetakbilanganprima()

"""(NO 7)"""
def faktorprima(n):
    prim=list()
    for i in range(2,n):
        a = True
        for x in prim:
            if(i%x==0):
                a=False
                break
        if a and n%i==0:
            prim.append(i)
    return prim
print(faktorprima(200))

"""(NO 8)"""
def apakahTerkandung(a,b):
    return a in b
print(apakahTerkandung("db","abcdcdsqwedb"))
print(apakahTerkandung("abd","abc"))

"""(NO 9)"""
for x in range(1,100):
	if x%3==0:
		print("PYTHON")
	elif x%5==0:
		print("UMS")
	else:
		print(x)


"""(NO 10)"""
from math import sqrt as akar 
def selesaikanABC(a, b, c):
	a=float(a)
	b=float(b)
	c=float(c)
	D=(b**2) - (4*a*c)
	if D<0:
		return "Determinannya negatif. Persamaan tidak mempunyai akar real"
	else:
		x1=(-b + akar(D))/2*a
		x2=(-b - akar(D))/2*a
		hasil=(x1, x2)
		return hasil

print(selesaikanABC(1,-5,6))

"""(NO 11)"""
thn=1900
if thn%4==0:
	if thn%400==0:
		print(thn,"Tahun Kabisat Habis dibagi 400")
	elif thn%100==0:
		print(thn,"Bukan Tahun Kabisat")
	else:
		print(thn,"Tahun Kabisat Habis dibagi 4")
elif thn%400==0:
	print(thn,"Tahun Kabisat habis dibagi 400")
else:
	print(thn, "Bukan Tahun Kabisat")

"""(NO 12)"""
import random
jawaban=random.randint(1,100)

print("Permainan Tebak Angka")
print("Saya menyimpan angka bulat antara 1 sampai 100. coba tebak")
live=1
while live <= 7:
	inputan=int(input("Masukkan tebakkan ke-"+str(live)+":>"))
	if inputan==jawaban:
		print("Ya. Anda Benar")
		break;
	elif inputan<jawaban:
		print("Itu terlalu kecil")
	elif inputan>jawaban:
		print("Itu terlalu Besar")
	live+=1
print("Jawbannya :", jawaban)


"""(NO 13)"""
def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])

print(katakan(12450000))

"""(NO 14)"""
def formatRupiah(a):
    struang=str(a)
    dataFinal=""
    x=-1
    while x >= -len(struang):
    	if(x+1)%3==0 and (x+1)!=0:
    		dataFinal="."+dataFinal
    	dataFinal=struang[x]+dataFinal
    	x-=1
    return "Rp. "+dataFinal+",-"
print(formatRupiah(123123))
