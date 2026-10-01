steps = 15
ways = [0] * (steps + 1)
ways[0] = 1

for current in range(1, steps + 1):
    ways[current] = ways[current - 1]
    if current >= 3:
        ways[current] += ways[current - 3]

print(f"上到第{steps}个台阶的方法数：", ways[steps])
