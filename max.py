n=int(input("Nhap so phan tu="))
a=[]
for i in range(0,n):
    x=int(input("Nhap phan tu thu %d=" %(i)))
    a.append(x)
print("mang da nhap:")
print(a)
mx=max(a)
print("phan tu lon nhat la :")
print(mx)
