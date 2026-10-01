import random


numbers = [random.randint(1, 50) for _ in range(20)]
print("原始列表：")
print(numbers)

for index in range(1, len(numbers)):
    current = numbers[index]
    position = index - 1

    while position >= 0 and numbers[position] > current:
        numbers[position + 1] = numbers[position]
        position -= 1

    numbers[position + 1] = current

print("插入排序后的列表：")
print(numbers)
