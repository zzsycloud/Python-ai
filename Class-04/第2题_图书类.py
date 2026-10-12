class Book:
    total_count = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.total_count += 1

    def discount(self, rate):
        self.price *= rate


book1 = Book("Python编程", "张老师", 100)
book2 = Book("面向对象程序设计", "李老师", 80)
book3 = Book("数据结构", "王老师", 120)
book1.discount(0.8)
book2.discount(0.9)
book3.discount(0.7)

print(f"图书总数：{Book.total_count}")
print(book1.price)
