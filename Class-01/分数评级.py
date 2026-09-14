def score_rating():
    print("\n--- 分数评级 ---")
    try:
        score = float(input("请输入成绩分数（0-100）: "))
        
        if score < 0 or score > 100:
            print("输入的分数不合理，请输入0-100之间的数字！")
        elif score < 60:
            print("评级：不及格")
        elif score < 70:
            print("评级：差")
        elif score < 80:
            print("评级：中")
        elif score < 90:
            print("评级：良")
        else: # 90-100
            print("评级：优")
    except ValueError:
        print("请输入有效的数字！")

# 运行
score_rating()