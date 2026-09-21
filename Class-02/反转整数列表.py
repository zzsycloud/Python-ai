import ast

# 输入示例：[1, 2, 3, 4, 5]
s = input("请输入一个包含若干整数的列表，例如 [1, 2, 3, 4, 5]：")

lst = ast.literal_eval(s)

# 翻转列表
reversed_lst = lst[::-1]

print("翻转后的列表：")
print(reversed_lst)