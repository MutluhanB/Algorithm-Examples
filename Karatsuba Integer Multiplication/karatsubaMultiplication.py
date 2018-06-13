"""

Mutluhan Boz 13.06.2018
-Karatsuba integer multiplication-
https://en.wikipedia.org/wiki/Karatsuba_algorithm

"""
def karatsuba(x:int,y:int)-> int:
    if(len(str(x))<=2 and len(str(y))<=2):
        return x*y
    xlen=len(str(x))
    ylen=len(str(y))
    maxlen=max(xlen,ylen)
    maxlen2=maxlen//2
    a=int(((x-(x%(10**maxlen2)))/10**maxlen2))
    b=int(x-(a*10**maxlen2))
    print("a :"+ str(a))
    print("b :" + str(b))
    c = int(((y-(y%(10**maxlen2)))/10**maxlen2))
    d = int(y - (c * 10 ** maxlen2))
    print("c :" + str(c))
    print("d :" + str(d))
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    abpcd=karatsuba(a+b,c+d)
    print(ac,abpcd,bd)
    print(maxlen)

    #Writing 2*maxlen2 is a trick for odd digit inputs
    return (10**(2*maxlen2)*ac)+(10**maxlen2*(abpcd-ac-bd))+bd

a=int(input("First number :"))
b=int(input("Second number :"))
print(str(a)+" times "+str(b)+" is "+str(karatsuba(a,b)))
