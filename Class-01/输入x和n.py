def series_sum():
    print("\n--- 数列求和 ---")
    try:
        x = int(input("请输入数字 x: "))
        n = int(input("请输入项数 n: "))
        
        total_sum = 0
        current_term = 0
        
        for i in range(n):
            current_term = current_term * 10 + x # 生成 x, xx, xxx...
            total_sum += current_term
            
        print(f"sum = {total_sum}")
        
        # （可选）打印展开式方便核对
        # 例如生成 "2+22+222" 这种字符串展示
        terms_str = []
        temp_term = 0
        for i in range(n):
            temp_term = temp_term * 10 + x
            terms_str.append(str(temp_term))
        print(f"展开式: {' + '.join(terms_str)} = {total_sum}")
        
    except ValueError:
        print("请输入有效的整数！")

# 运行
series_sum()