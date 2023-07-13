"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.

"""


class Rectangle:
    def __init__(self, long, width=0):
        self.long = long
        self.width = width

    def perimeter(self):
        if not self.width:
            perim = self.long * 4
        else:
            perim = self.long * 2 + self.width * 2

        return perim

    def plosh(self):
        if not self.width:
            return self.long ** 2
        else:
            return self.long * self.width


rect = Rectangle(2)
pl = Rectangle(2)

print(rect.perimeter())
print(pl.plosh())
