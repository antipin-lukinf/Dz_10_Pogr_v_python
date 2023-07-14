"""
Задание №3
📌 Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""

class Men:
    def __init__(self, age, name_1, name_2, name_3=None):
        self._age = age
        self.name_1 = name_1
        self.name_2 = name_2
        if name_3:
            self.name_3 = name_3

    def full_name(self):
        return f'{self._age}  {self.name_1}  {self.name_2}  {self.name_3}'

    def birthday(self):
        self._age += 1

    def men_age(self):
        return self._age


human = Men(28, 'Lenin ', 'Vladimir', 'Ilich')

print(human.full_name())

print(human.men_age())
human.birthday()
print(human.men_age())






