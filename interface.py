
from abc import ABC, abstractmethod
from typing_extensions import override

class Animal(ABC):
    def __init__(self, name):
        self.name = name

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Dog(Animal):
    @override
    def move(self):
        print(f"{self.name} runs")

class Penguin(Animal):
    @override
    def move(self):
        print(f"{self.name} waddles")

class Bat(Animal, Flyable):
    def move(self):
        print(f"{self.name} crawls")

    @override
    def fly(self):
        print(f"{self.name} flies at night")

class Eagle(Animal, Flyable):
    def move(self):
        print(f"{self.name} walks and hops")

    def fly(self):
        print(f"{self.name} soars high in the sky")

'''
Animal (abstract)
│
├── Eagle --------┐
├── Bat   --------│
│                 └── Flyable (interface)
├── Dog
└── Penguin
'''