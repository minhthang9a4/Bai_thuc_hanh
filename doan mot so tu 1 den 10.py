import random
def guess():
    num = random.randint(1,10)
    return num
done = False
while not done:
    val=int(input(" Nhap mot so: "))
    num = guess()
    if val >= 11:
        print("Sai roi dit con me !!")
        exit()
    if val == num:
      print("Doan dung roi !! ")
      done = True
