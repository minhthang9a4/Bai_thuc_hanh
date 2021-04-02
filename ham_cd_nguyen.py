def phannguyen(x) :
    binNumber=''
    while x > 0 :
         binNumber=str(x%2)+binNumber
         x=x//2
    return binNumber