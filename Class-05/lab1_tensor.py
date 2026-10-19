import torch

# 创建常量张量
tensor_const = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# 创建普通张量
tensor_var = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# 创建全零张量和全一张量
tensor_zeros = torch.zeros((2, 3))
tensor_ones = torch.ones((3, 2))

print("常量张量:\n", tensor_const)
print("变量/普通张量:\n", tensor_var)
print("全零张量:\n", tensor_zeros)
print("全一张量:\n", tensor_ones)

#基本运算
tensor_a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
tensor_b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

add_result = tensor_a + tensor_b
sub_result = tensor_a - tensor_b
mul_result = tensor_a * tensor_b
div_result = tensor_a / tensor_b
matmul_result = torch.matmul(tensor_a, tensor_b)

print("加法结果:\n", add_result)
print("减法结果:\n", sub_result)
print("逐元素乘法结果:\n", mul_result)
print("除法结果:\n", div_result)
print("矩阵乘法结果:\n", matmul_result)

#索引切片
tensor = torch.tensor([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

element = tensor[1, 2]      # 第二行第三列
row = tensor[1, :]          # 第二行
col = tensor[:, 2]          # 第三列
sub_tensor = tensor[0:2, 1:3]

print("单个元素:", element)
print("第二行:", row)
print("第三列:", col)
print("子张量:\n", sub_tensor)

#形状变换
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

reshaped_tensor = tensor.reshape(3, 2)
transposed_tensor = tensor.transpose(0, 1)

print("原始张量:\n", tensor)
print("改变形状后的张量:\n", reshaped_tensor)
print("转置后的张量:\n", transposed_tensor)