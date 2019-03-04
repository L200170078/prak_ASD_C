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