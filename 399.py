
s = input("Введіть рядок: ")
result = ""
count = 1
i = 0

while i < len(s):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        if count > 1:
            result += str(count)
        result += s[i]
        count = 1
    i += 1

print(result)
