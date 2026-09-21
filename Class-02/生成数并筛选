import random

n = int(input("请输入一个自然数 n："))

# 在 [1, 5n] 中随机生成 n 个不重复的自然数
nums = random.sample(range(1, 5 * n + 1), n)

print("随机生成的 n 个不重复自然数：")
print(nums)

# 只保留偶数
evens = [x for x in nums if x % 2 == 0]

print("其中所有的偶数：")
print(evens)