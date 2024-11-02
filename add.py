x = input()

for i in range(int(x)):
    strinput = input()
    listInput = strinput.split('+')
    numA = listInput[0]
    numB = listInput[1]
    print(int(numA)+int(numB))