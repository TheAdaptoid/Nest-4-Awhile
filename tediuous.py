caseCOunt = int(input())

wordDict: dict[str, int] = {}

for case in range(caseCOunt):

    line: str = input()
    splitLine: list[str] = line.split(" ")
    words: list[str] = splitLine[1:]

    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

sorted(wordDict.items(), key=lambda item: item[1])

print(wordDict)
