import random

# 生成 20 个随机数
nums = [random.randint(1, 100) for _ in range(20)]

print("原始列表：")
print(nums)

# 前 10 个元素升序排列
nums[:10] = sorted(nums[:10])

# 后 10 个元素降序排列
nums[10:] = sorted(nums[10:], reverse=True)

print("处理后列表：")
print(nums)