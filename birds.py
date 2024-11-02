correctTries = 0
time = 0
birds = []

while(True):
    user_input = input()
    if(user_input == "-1"):
        break
    
    entries = user_input.split(" ")
    min = int(entries[0])
    birdType = entries[1]
    correction = entries[2]
    

    if(correction == "right"):
        correctTries+=1
        time += min
        time += (birds.count(birdType) * 20)
        birds = [item for item in birds if item != birdType]

    else:
        birds.append(birdType)
    
print(f"{correctTries} {time}")