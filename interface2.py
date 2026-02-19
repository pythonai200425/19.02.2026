
'''
class interface ArnonaPay-- def payArnona()
class interface RentPay-- def payRent()
class Person -- id, name  __str__  __init__
class Tenant inherits Person implements ArnonaPay, RentPay
         data -- arnona, rent, address  __str__ __init__
create a Tenant and execute pay_rent, pay_arnona
'''

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

class Bat(Animal, Flyable):
    @override
    def move(self):
        print(f"{self.name} crawls")

'''
Animal (abstract)
│
├── Eagle --------┐
├── Bat   --------│
│                 └── Flyable (interface)
├── Dog
└── Penguin
'''