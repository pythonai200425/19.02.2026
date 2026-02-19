
class Animal:
    def __init__(self, name, breed):
        print("Animal __init__ called")
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"name {self.name} {self.breed}"

class Dog(Animal):
    def __init__(self, name, breed, pure_breed):
        super().__init__(name, breed)
        print("Dog __init__ called")
        self.pure_breed = pure_breed

    def __str__(self):
        return f"Dog {super().__str__()} pure breed {self.pure_breed}"


bunny = Animal('Bugs Bunny', 'Bunny')
print(bunny)

rex = Dog("Rex", "Golden Retriever", True)
print(rex)