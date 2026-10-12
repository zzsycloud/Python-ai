class Student:
    def __init__(self, name, student_id, score):
        self.name = name
        self.id = student_id
        self.score = score

    def show_info(self):
        print(f"姓名：{self.name}，学号：{self.id}，成绩：{self.score}")


student1 = Student("张三", "2026001", 88)
student2 = Student("李四", "2026002", 92)
student1.show_info()
student2.show_info()
