n = int(input("Введіть число №1 : "))
b = int(input("Введіть число №2 : "))
c = int(input("Введіть число №3 : ")) #умова при якій буде виводитись запит для користувача 


if n >= b and n >= c: # умова до знаходження максимального числа 
    maximum = n

elif b >= n and b >= c: 
    maximum = b

else:
    maximum = c


if n <= b and n <= c: # умова для знаходження мінімального числа 
    minimum = n

elif b <= n and b <= c:
    minimum = b

else:
    minimum = c


if n == b: # та знаходження того шо уже лишилось 
    remaining = c

elif n == c:
    remaining = b

elif b == c:
    remaining = n

else:
    if n != maximum and n != minimum:
        remaining = n

    elif b != maximum and b != minimum:
        remaining = b

    else:
        remaining = c

print(maximum)
print(minimum)
print(remaining)