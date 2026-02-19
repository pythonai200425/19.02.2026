

class Watch:

    def __init__(self, datetime):
        self.__datetime = datetime

    def get_time(self):
        return self.__datetime  # --> current timezone

class Person:

    def __init__(self, age):
        self.__age = age  # bypass setter
        self.age = age  # setter

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        else:
            self.__age = value

    def __str__(self):
        return f"Person {self.age} {self.__age}"

p = Person(20)
print(p.age)
p.age = -20

print()

# class
# init
# str
# repr
# __magic__
# abstract
# inheritance, override
# interface
# encapsulation
# static
# object