x = input()

inputList = x.split(" ")
numA = int(inputList[0])
numB = int(inputList[1])

if(numB >= numA):
    if(numB-numA == 1):
        print(f"He will have {numB-numA} sandwich left over")
    else:
        print(f"He will have {numB-numA} sandwiches left over")
else:
    if(numA-numB == 1):
        print(f"He needs {numA-numB} more sandwich")
    else:
        print(f"He needs {numA-numB} more sandwiches")