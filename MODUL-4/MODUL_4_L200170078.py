#1

class bikinArray(object):
    """docstring for bikinArray"""
    def __init__(self):
        self.index = 11*[None]

    def __getitem__(self, item):
        getData=self.index[item]
        return getData

    def __setitem__(self, key, value):
        self.index[key]=value
        

class MhsTIF(object):
    """docstring for MhsTIF"""
    def __init__(self, nama, nim, kota, uangS):
        self.nama=nama
        self.nim=nim
        self.kota=kota
        self.uangSaku=uangS

c=bikinArray()
c[0] = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c[1] = MhsTIF("Budi", 51, "Sragen", 230000)
c[2] = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c[3] = MhsTIF("Candra", 18, "Surakarta", 235000)
c[4] = MhsTIF("Eka", 4, "Boyolali", 240000)
c[5] = MhsTIF("Fandi", 31, "Salatiga", 250000)
c[6] = MhsTIF("Deni", 13, "Klaten", 245000)
c[7] = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c[8] = MhsTIF("Janto", 23, "Klaten", 245000)
c[9] = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c[10] = MhsTIF("Khalid", 29, "Purwodadi", 210000)


def cariMhs(key):
    final=[]
    maxLenDaftar=len(c.index)
    for x in range(0,maxLenDaftar):
        if c[x].kota is key:
            final.append(x)
    if not final:
        return None
    else:
        return final

def cariUangKecil():
    final=[None,None]
    sebelum=0
    x=0
    maxLenDaftar=len(c.index)-1
    while x <= maxLenDaftar:
        try:
            sebelum=c[x]
            nextarray=x+1
            if sebelum.uangSaku <= c[nextarray].uangSaku:
                sebelum=c[x]
                final[0]=c[x].nama
                final[1]=c[x].uangSaku
            x+=1
        except IndexError:
            break
        
    return final

#2

class MhsTIF(object):
    """docstring for MhsTIF"""
    def __init__(self, nama, nim, kota, uangS):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangS

class my_Array(object):
    """docstring for bikinArray"""
    def __init__(self):
        self.index = 11*[None]
    def __getitem__(self, item):
        getData = self.index[item]
        return getData
    def __setitem__(self, key, value):
        self.index[key] = value

c = my_Array()

c[0] = MhsTIF("Bintang", 10, "Solo", 240000)
c[1] = MhsTIF("Budi", 51, "Sragen", 230000)
c[2] = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c[3] = MhsTIF("Candra", 18, "Surakarta", 235000)
c[4] = MhsTIF("Eka", 4, "Boyolali", 240000)
c[5] = MhsTIF("Fandi", 31, "Salatiga", 250000)
c[6] = MhsTIF("Deni", 13, "Klaten", 245000)
c[7] = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c[8] = MhsTIF("Janto", 23, "Klaten", 245000)
c[9] = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c[10] = MhsTIF("Khalid", 29, "Purwodadi", 210000)

def cariUangKecil():
    final = [None,None]
    sebelum = 0
    x = 0
    l = len(c.index) - 1
    while x <= l:
        try:
            sebelum = c[x]
            nexta = x + 1
            if sebelum.uangSaku <= c[nexta].uangSaku:
                sebelum = c[x]
                final[0] = c[x].nama
                final[1] = c[x].uangSaku
            x += 1
        except IndexError:
            break	
return final

#3

class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Bintang", 10, "Solo", 240000)
c1 = MhsTif("Budi", 51, "Sragen", 230000)
c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("Eka", 4, "Boyolali", 240000)
c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
c6 = MhsTif("Deni", 13, "Klaten", 245000)
c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTif("Janto", 23, "Klaten", 245000)
c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariUSTerkecil(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

a = cariUSTerkecil(Daftar)
print(a)

#4

class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Bintang", 10, "Solo", 240000)
c1 = MhsTif("Budi", 51, "Sragen", 230000)
c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("Eka", 4, "Boyolali", 240000)
c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
c6 = MhsTif("Deni", 13, "Klaten", 245000)
c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTif("Janto", 23, "Klaten", 245000)
c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariUSKurang250k(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

a = cariUSKurang250k(Daftar)
for i in a:
print(i.nama)

#5

def cariLinkedList(head, target):
    temp = head
    while temp.data != None:
        if temp.data == target:
            return temp
return -1

#6

class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Bintang", 10, "Solo", 240000)
c1 = MhsTif("Budi", 51, "Sragen", 230000)
c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("Eka", 4, "Boyolali", 240000)
c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
c6 = MhsTif("Deni", 13, "Klaten", 245000)
c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTif("Janto", 23, "Klaten", 245000)
c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(binSe(kumpulan, 5))

#7

class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangsaku

c0 = MhsTif("Bintang", 10, "Solo", 240000)
c1 = MhsTif("Budi", 51, "Sragen", 230000)
c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("Eka", 4, "Boyolali", 240000)
c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
c6 = MhsTif("Deni", 13, "Klaten", 245000)
c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTif("Janto", 23, "Klaten", 245000)
c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 6))
