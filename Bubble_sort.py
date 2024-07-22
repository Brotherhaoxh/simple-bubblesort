numbers = [4,3,1,2,5,7,6,9,8]
length = len(numbers)

for i in range(length):
    # print(numbers)
    for j in range(length-1):
        if numbers[j] > numbers[j + 1]:
            tmp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = tmp

print(numbers)