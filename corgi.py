# single corgie refules
# deposits 1 kilo per ship
# loses 1 kilo per mile moved

firstLine = input().split(" ")
amountOfFuel = int(firstLine[0])
numShipRefuel = int(firstLine[1])
remainLines = int((numShipRefuel*(numShipRefuel-1))/2)

uniqueShips = []
entries = []

for i in range(remainLines):
    user_input = input().split(" ")
    numA = int(user_input[0]) #ship identifier A
    numB = int(user_input[1]) #ship identifier B
    numC = int(user_input[2]) #distance between 2 ships miles

    entries.append([numA, numB, numC])
    if(not numA in uniqueShips):
        uniqueShips.append(numA)
    if(not numB in uniqueShips):
        uniqueShips.append(numB)

touchedEntries = [0]
sorted_entries = sorted(entries, key=lambda x: x[2])
paths = []

while len(touchedEntries) < len(uniqueShips):
    entries_to_look_at = []
    for item in sorted_entries: 
        if(item[0] in touchedEntries and not item in paths):
            entries_to_look_at.append(item)
    temp_sorted_entries = sorted(entries_to_look_at, key=lambda x: x[2])
    if(len(temp_sorted_entries) != 0):
        paths.append(temp_sorted_entries[0])
        touchedEntries.append(temp_sorted_entries[0][1])


totalFuelUsed = len(uniqueShips)
for item in paths:
    totalFuelUsed += item[2]

if(totalFuelUsed <= amountOfFuel):
    print('yes')
else:
    print('no')


