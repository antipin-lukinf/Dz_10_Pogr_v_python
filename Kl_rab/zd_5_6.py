"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""

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


if __name__=='__main__':
    dog = Dog('Bim', 'Tacsa', ['Голос', 'Сидеть', 'Фас'])
    fish = Fish('Nemo', 'Gold Fish', 3)
    bird = Bird('Kesha', 'Попугай', 2)
    animal = Animal('Franken', 'Zombi', 7)
    print(animal.print_specific())
    print(dog.print_specific())
    print(fish.print_specific())
    print(bird.print_specific())