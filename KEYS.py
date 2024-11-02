number = input()
count = 0
valid = True
for digit in number:
    if digit != '4' and digit != '7':
        valid = False
        break
    count += 1

if count % 2 == 0:
    valid = False

print('YES' if valid else 'NO')