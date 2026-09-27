def is_binary_palindrome(number): # визначаємо функцію, яка перевіряє, чи є число паліндромом у двійковій системі числення
    binary_str = f"{number:08b}"
    return binary_str == binary_str[::-1] 


num = int(input("Введіть число: ")) # запитуємо користувача ввести число

result = is_binary_palindrome(num) # викликаємо функцію та зберігаємо результат у змінній result

print(result) # виводимо результат на екран
