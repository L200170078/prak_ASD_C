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
