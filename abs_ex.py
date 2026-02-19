
from abc import ABC, abstractmethod
from typing_extensions import override

class Animal(ABC):

    def __init__(self, name, size):
        self.__name = name
        self.size = size

    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        return f"Animal {self.name}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @override
    def make_sound(self):
        print('**haw haw**')

class Cat(Animal):
    @override
    def make_sound(self):
        print('**miau miau**')

class chiwawa(Dog):
    pass

# donkey = Animal('donkey')
rexy = Dog('rex')
rexy.make_sound()
mizzy = Cat('mizzy')
mizzy.make_sound()

chiw = chiwawa('chiw')

print(chiw)