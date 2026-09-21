a = int(input("Введіть число 1 : "))
b = int(input("Введіть число 2 : "))
c = int(input("Введіть число 3 : ")) # виведення трьох чисел від користувача
smallest = min(a , b , c) # мінімальне
largest = max(a , b , c) # максимальне 
middle = (a + b + c) - smallest - largest # це карочо середнє число з трьох введених
print(smallest , middle , largest) # виводить числа від найменшого до найбільшого

