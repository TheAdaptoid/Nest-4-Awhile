number = input()
count = 0
for digit in number:
    if digit != 4 and digit != 7:
        print("NO")
        break
    count += 1

if count % 2 == 0:
    print("No")
else:
    print("Yes")
