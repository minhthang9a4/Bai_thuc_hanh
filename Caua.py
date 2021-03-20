try:
    n = int(input("Nhap n: "))
    if n <= 0:
        exit()
except:
    print('Phai nhap so tu nhien')
    exit()

a = []

for i in range(n):
    a.append(input('Nhap so thu %d: ' % (i+1)))

print(a)
