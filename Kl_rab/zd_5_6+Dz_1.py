"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""
import random

""" 
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""

class Animal:
    def __init__(self, name:str=None, breed:str='unknow', age:int=0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'



class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknow', comands:list[str]='unknow'):
        # self.name = name
        # self.breed = breed
        super().__init__(name, breed)
        self.comands = comands

    def print_specific(self):
        return f'{self.comands}'


class Fish(Animal):
    def __init__(self, name:str=None, breed:str='unknow', count_fins:int=0):
        # self.name = name
        # self.breed = breed
        super().__init__(name, breed)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'


class Bird(Animal):
    def __init__(self, name:str=None, breed:str='unknow', count_fligths:int=0):
        # self.name = name
        # self.breed = breed
        super().__init__(name, breed)
        self.count_fligths = count_fligths

    def print_specific(self):
        return f'{self.count_fligths}'


# if __name__=='__main__':
#     dog = Dog('Bim', 'Tacsa', ['Голос', 'Сидеть', 'Фас'])
#     fish = Fish('Nemo', 'Gold Fish', 3)
#     bird = Bird('Kesha', 'Попугай', 2)
#     animal = Animal('Franken', 'Zombi', 7)
#     print(animal.print_specific())
#     print(dog.print_specific())
#     print(fish.print_specific())
#     print(bird.print_specific())

"""
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.

"""



_DOGS = [['Шарик', 'Дворянин', ['Сидеть', 'Лежать', 'Фас']],
         ['Рекс', 'Овчарка', ['Сидеть', 'Фу', 'Брысь']],
         ['Бобик', 'Спаниель', ['Сидеть', 'Летать', 'Кусать']]]

_FISHS = [['Карл', 'Карп', 2],
          ['Восетр', 'Осетр', 3],
          ['Щукарь', 'Щука', 4]]

_BIRDS = [['Кар_Кар', 'Ворон', 2],
          ['Кеша', 'Попугай', 3],
          ['Летунья', 'Ласточка', 4]]


class Meat_factory:
    def __init__(self):
        pass

    def gen_meat(self, type_meat) -> Animal:

        animal = None
        if type_meat.lower() == 'dog':
            animal = self._gen_dog()
            return animal

        if type_meat.lower() == 'fish':
            animal = self._gen_fish()
            return animal

        if type_meat.lower() == 'bird':
            animal = self._gen_bird()
            return animal


    def _gen_dog(self) -> Dog:
        dog = random.choice(_DOGS)
        return dog

    def _gen_fish(self) -> Fish:
        fish = random.choice(_FISHS)
        return fish

    def _gen_bird(self) -> Bird:
        bird = random.choice(_BIRDS)
        return bird


if __name__ == '__main__':
    anim_1 = Meat_factory()
    print(anim_1.gen_meat('dog'))
    print(anim_1.gen_meat('fish'))
    print(anim_1.gen_meat('bird'))

