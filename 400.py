
s = input("Введіть рядок: ")

left = 0
right = len(s) - 1
palindrome = True

while left < right:
    if not s[left].isalpha():
        left += 1
    elif not s[right].isalpha():
        right -= 1
    elif s[left].lower() != s[right].lower():
        palindrome = False
        break
    else:
        left += 1
        right -= 1

if palindrome:
    print("Yes")
else:
    print("No")
