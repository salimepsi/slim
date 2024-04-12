# (°F - 32) * 5/9
def TEMP(temp,type):
    if (type=="c"):
        a = (temp*9/5)+32 
        print(a)
    elif (type=="f"): 
        a=(temp-32)*5/9
        print(a)
    else:
        print ("veuillez entrer le type c ou f")
TEMP(1,'c')


