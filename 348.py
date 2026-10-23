
n = int(input("Введіть кількість прапорців: "))

line1 = ""
line2 = ""
line3 = ""
line4 = ""

for i in range(1, n + 1):
    line1 += "+___ "
    line2 += f"|{i} / "
    line3 += "|__\\ "
    line4 += " |   "

print(line1.rstrip())
print(line2.rstrip())
print(line3.rstrip())
print(line4.rstrip())
