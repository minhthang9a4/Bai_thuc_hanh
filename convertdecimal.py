import math
from ham_cd_nguyen import phannguyen
from ham_cd_le import phanle
n=float(input("nhap vao so thap phan :"))
if n < 0 :
    exit()
a=[]
a=(math.modf(n))
x=int(a[1])
print("phan nguyen cua so thap phan da nhap la : %d" %(x))
y=float(a[0])
print("phan le cua so thap phan da nhap la : %d" %(y))
binary={}
e={}
o={}
bnreven=phannguyen(x)
bnrodd=phanle(y)
even='phan nguyen binary'
odd='phan le binary'
e={even:bnreven}
o={odd:bnrodd}
binary.update(e)
binary.update(o)
print(binary)
