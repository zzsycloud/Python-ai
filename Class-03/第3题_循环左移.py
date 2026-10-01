import random


numbers = [random.randint(1, 50) for _ in range(20)]
print("原始列表：")
print(numbers)

for _ in range(5):
    first = numbers.pop(0)
    numbers.append(first)

print("循环左移5个元素后的列表：")
print(numbers)
