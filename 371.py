
text = input("Введіть текст: ")
symbol = input("Введіть символ: ")

if symbol in text:
    first = text.find(symbol)
    last = text.rfind(symbol)

    if first == last:
        print(first)
    else:
        print(first, last)


