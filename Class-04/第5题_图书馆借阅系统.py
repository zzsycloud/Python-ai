class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.__is_borrowed = False

    def borrow(self):
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        if not self.__is_borrowed:
            return False
        self.__is_borrowed = False
        return True

    @property
    def is_borrowed(self):
        return self.__is_borrowed


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if any(item.isbn == book.isbn for item in self.book_list):
            print("添加失败：ISBN已存在")
            return
        self.book_list.append(book)

    def borrow_book(self, isbn):
        book = self._find_book(isbn)
        if book is None:
            print("借书失败：图书不存在")
        elif book.borrow():
            print(f"借书成功：{isbn}")
        else:
            print("借书失败：该书已被借出")

    def return_book(self, isbn):
        book = self._find_book(isbn)
        if book is None:
            print("还书失败：图书不存在")
        elif book.return_book():
            print(f"还书成功：{isbn}")
        else:
            print("还书失败：该书未借出")

    def show_all_books(self):
        print("=====馆藏图书列表=====")
        for book in self.book_list:
            status = "已借出" if book.is_borrowed else "可借阅"
            print(f"ISBN:{book.isbn},书名:{book.title},状态:{status}")

    def _find_book(self, isbn):
        return next((book for book in self.book_list if book.isbn == isbn), None)


library = Library()
library.add_book(Book("Python编程", "978001"))
library.add_book(Book("面向对象程序设计", "978002"))
library.add_book(Book("数据结构", "978003"))
library.show_all_books()
library.borrow_book("978001")
library.borrow_book("978001")
library.return_book("978001")
library.return_book("978001")
