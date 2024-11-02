inputs: list[str] = [str(char) for char in input().split(" ")]
nums: list[int] = []

for i in range(len(inputs)):
    if inputs[i].isdigit():
        nums.append(int(inputs[i]))

ARRAY: list[int] = nums
LIS = [1] * len(ARRAY)

for i in range(len(ARRAY)):
    for j in range(i):
        if ARRAY[i] > ARRAY[j] and LIS[i] < LIS[j] + 1:
            LIS[i] = LIS[j] + 1

print(max(LIS))