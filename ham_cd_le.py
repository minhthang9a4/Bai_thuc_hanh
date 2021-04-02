def phanle(y):
    import math
    binNumberodd=''
    i=0
    c=[]
    while i < 3 :
        c=math.modf(y*2)
        j=int(c[1])
        k=c[0]
        binNumberodd=str(j)+binNumberodd
        y=k
        i=i+1
    return binNumberodd