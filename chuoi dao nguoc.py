m=int(input("Nhap so phan tu: "))
b=[]
for j in range(0,m):
    y=int(input("Nhap phan tu thu %d: " %(j)))
    b.append(y)
print("chuoi da nhap la: ")
print(b)
print("chuoi dao nguoc la: ")
print(list(reversed(b)))
