
from typing_extensions import override

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def annual_raise(self):
        self.salary *= 1.1

    def __str__(self):
        return f"name:{self.name} salary:{self.salary}"

class Developer(Employee):
    def __init__(self, name: str, salary: int, language: str, master_ai: bool):
        super().__init__(name, salary)
        self.language = language
        self.master_ai = master_ai
        self.stocks = 0

    @override
    def annual_raise(self):
        self.stocks += 1000

    def __str__(self):
        return f"{super().__str__()} language:{self.language} master_ai:{self.master_ai}"

class Manager(Employee):
    def __init__(self, name: str, salary: int, mba_un: str, managing_division: str):
        super().__init__(name, salary)
        self.mba_un = mba_un
        self.managing_division = managing_division

    def __str__(self):
        return f"{super().__str__()} mba_un:{self.mba_un} managing_division:{self.managing_division}"

bill_gates = Developer('bill gates', 100_000, "c", False)
print(bill_gates)

tim_cook = Manager('Tim Cook', 200_000, "MIT", "APPLE Development")
print(tim_cook)

tim_cook.annual_raise()
bill_gates.annual_raise()

