class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def details(self):
        print(f"my name is {self.name} and my age is {self.age}")
person1 = person("Jerry",18)
print(person1.name,person1.age)
person1.details()

class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def details(self):
        print(f"my salary is {self.salary}")
person_2 = Employee("Roro",35,485000)
person_2.details()