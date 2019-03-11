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
