# 棋盘共 64 个格子
# 第 1 格 1 粒，第 2 格 2 粒，第 3 格 4 粒……
# 使用列表推导式生成每格米粒数，再用 sum 求和

grains = [2 ** i for i in range(64)]

total = sum(grains)

print("第 64 个格子中的米粒数：")
print(grains[-1])

print("64 个格子总共需要的米粒数：")
print(total)