def upperlower(a):
    up=0
    lw=0
    for i in a:
        if i.isupper():
            up+=1
        elif i.islower():
            lw+=1
    print("No. of Upper case characters :",up)
    print("No. of Lower case Characters :",lw)
a='The quick Brow Fox'    
upperlower(a)    