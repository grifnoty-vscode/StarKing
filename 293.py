
n = int(input("Введіть число n: ")) # Вводимо число n

count = 0 # Лічильник паліндромів

for i in range(1, n + 1): # Перебираємо числа від 1 до n
    temp = i
    reverse = 0

    while temp > 0:  # Перевертаємо цифри числа
        reverse = reverse * 10 + temp % 10
        temp //= 10

    if i == reverse: # Перевіряємо, чи є число паліндромом
        count += 1

print(count) # Виводимо кількість паліндромів
