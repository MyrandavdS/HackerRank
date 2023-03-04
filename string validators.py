s = input()
answer = False

for char in s:
    if char.isalnum():
        answer = True
print(answer)
answer = False

for char in s:
    if char.isalpha():
        answer = True
print(answer)
answer = False

for char in s:
    if char.isdigit():
        answer = True
print(answer)
answer = False

for char in s:
    if char.islower():
        answer = True
print(answer)
answer = False

for char in s:
    if char.isupper():
        answer = True
print(answer)
answer = False



