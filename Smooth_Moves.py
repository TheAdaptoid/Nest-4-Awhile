value = 0
for i in range(5):
    row: list[str] = input().split(" ")
    for j in range(5):
        if row[j] == "1":
            value = abs(2 - i) + abs(2 - j)
print(value)