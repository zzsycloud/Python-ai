import math


class ShapeNotImplementError(Exception):
    pass


class Shape:
    def get_area(self):
        raise ShapeNotImplementError("图形面积计算未实现")

    def get_perimeter(self):
        raise ShapeNotImplementError("图形周长计算未实现")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("半径必须大于0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("三边无法构成三角形")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2
        return math.sqrt(
            half_perimeter
            * (half_perimeter - self.a)
            * (half_perimeter - self.b)
            * (half_perimeter - self.c)
        )

    def get_perimeter(self):
        return self.a + self.b + self.c


def print_info(shape):
    shape_name = "圆形" if isinstance(shape, Circle) else "三角形"
    print(
        f"图形类型：{shape_name}，面积：{shape.get_area():.2f}，"
        f"周长：{shape.get_perimeter():.2f}"
    )


print_info(Circle(5))
print_info(Triangle(3, 4, 5))

try:
    Circle(0)
except ValueError as error:
    print(f"参数异常：{error}")

try:
    Triangle(1, 2, 5)
except ValueError as error:
    print(f"参数异常：{error}")
