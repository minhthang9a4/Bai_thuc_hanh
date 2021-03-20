import random
def guess():
    num = random.randint(1,10)
    return num
done = False
while not done:
    val=int(input(" Nhap mot so: "))
    num = guess()
    if val == num:
      print("Doan dung roi !! ")
      done = True
    
