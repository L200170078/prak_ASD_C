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