def chicken_rabbit():
    print("--- 鸡兔同笼问题 ---")
    try:
        heads = int(input("请输入头的个数: "))
        legs = int(input("请输入脚的个数: "))
        
        # 假设全是鸡，多出来的脚就是兔子的（每只兔子多2只脚）
        rabbits = (legs - 2 * heads) / 2
        chickens = heads - rabbits
        
        # 判断逻辑合法性：脚数必须为偶数，且兔子数和鸡数都不能为负数
        if legs % 2 != 0 or rabbits < 0 or chickens < 0:
            print("输入的数据有误，无解！")
        else:
            print(f"鸡有 {int(chickens)} 只，兔子有 {int(rabbits)} 只。")
    except ValueError:
        print("请输入有效的整数！")

# 运行
chicken_rabbit()