import random

fox_hole = random.randint(0, 4)
days = 0

while True:
    try:
        guess = int(input("请输入要抓捕的洞口编号（0-4）："))
    except ValueError:
        print("请输入 0 到 4 之间的整数。")
        continue

    if guess not in range(5):
        print("洞口编号必须是 0、1、2、3 或 4。")
        continue

    days += 1
    if guess == fox_hole:
        print(f"抓到了狐狸！共用了 {days} 天。")
        break

    print("这里没有狐狸，明天再来。")
    if fox_hole == 0:
        fox_hole = 1
    elif fox_hole == 4:
        fox_hole = 3
    else:
        fox_hole += random.choice((-1, 1))
