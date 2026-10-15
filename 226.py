n = int(input("Enter a number: "))
suma = 0
for i in range(1, n + 1):
 suma += i ** 2
 print(f"The sum of squares from 1 to {n} is: {suma}")