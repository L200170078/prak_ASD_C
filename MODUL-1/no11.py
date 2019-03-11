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
