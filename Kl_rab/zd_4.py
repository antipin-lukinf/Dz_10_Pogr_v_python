"""
Задание №4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
import random

from Kl_rab.zd_3 import Men


class Employee(Men):

    def __init__(self, *args, **kwargs):
        self.id = random.randint(100000, 999999)

        super().__init__(*args, **kwargs)

    @property  # Защищает от изменения access_lvl, он вычисляется. Делает из метода атрибут
    def access_lvl(self):
        str_id = str(self.id)
        list_id_numbers = sum(list(map(int, str_id)))
        return list_id_numbers % 7

empl = Employee(36, 'Сталин', 'Иосиф', 12563)

print(f'{empl.id = }, {empl.access_lvl = }')
