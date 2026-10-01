numbers = [7, 2, 9, 1, 5]

if not numbers:
    print("列表不能为空。")
else:
    minimum = numbers[0]
    maximum_difference = 0

    for number in numbers[1:]:
        difference = number - minimum
        if difference > maximum_difference:
            maximum_difference = difference
        if number < minimum:
            minimum = number

    print("列表：", numbers)
    print("A[b] - A[a] 的最大值：", maximum_difference)
