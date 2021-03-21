celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit: ")
print(fahrenheit)
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in celsius: ")
print(celsius)
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))