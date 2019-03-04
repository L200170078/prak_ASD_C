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

# for i in range(2,int(sq(18))+1):
# 	print(i)

