
def count_numbers(n):
    if n < 1 or n > 27:
        return 0

    count = 0
    num = 100

    while num <= 999:
        a = num // 100
        b = (num // 10) % 10
        c = num % 10

        digit_sum = a + b + c

        if digit_sum == n:
            count += 1

        num += 1

    return count


if __name__ == "__main__":
    try:
        n = int(input("Введіть ціле число n: "))

        if 1 <= n <= 27:
            result = count_numbers(n)
            print("Кількість трицифрових чисел:", result)
        else:
            print("Помилка! Число повинно бути від 1 до 27.")

    except ValueError:
        print("Помилка! Потрібно ввести ціле число.")
