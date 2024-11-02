line:str = input()
sessionCount: int = 0
userLogin: dict[str, int] = {}
userLogout: dict[str, int] = {}

while line != '':
    # New Session
    if line == "START":
        userLogin.clear()
        userLogout.clear()
        sessionCount += 1

    # Print output
    if line == "END":
        print(f"Session {sessionCount}")

        sorted(userLogout.items(), key=lambda item: item[1])

        for key, value in userLogout.items():
            print(f"{key} ${round(value * 0.01, 2)}")
        
        print()

        if not stdin.seekable():
            break

    splitLine = line.split(" ")
    if splitLine[0] == "LOGON":
        userLogin[splitLine[1]] = int(splitLine[2])
        
        # Add new users
        if splitLine[1] not in userLogout:
            userLogout[splitLine[1]] = 0

    elif splitLine[0] == "LOGOFF":
        userLogout[splitLine[1]] += (
            int(splitLine[2]) - userLogin[splitLine[1]]
        )

    line:str = input()