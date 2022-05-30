class person :
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age =age
        self.height = height
        self.weight = weight
    def details(self):
        print(f"My name is {self.name} , i am {self.age} years old. I weigh {self.weight}kilos and am {self.height} metres tall")
person1 = person("Jerry",18,1.7,70)
person1.details()

class student(person):
    def __init__(self,name,age,height,weight,level,subject):
        super().__init__(name,age,height,weight)
        self.level = level
        self.subject = subject
    def details(self):
        print(f"My name is {self.name} i am a {self.level} and i love {self.subject}")
person2 = person(name="Jim",17,1.2,64,"form4","biology")
person2.details()

class teacher(person):
    def __init__(self,name,age,height,weight,subj,salary):
        super().__init__(name,age,height,weight)
        self.subj = subj
        self.salary = salary
    def details(self):
        print(f"My name is {self.name} i teach {self.subject} and i earn {self.salary} euros ")
person3 = person("Maina",49,1.1,69,"Maths",38500)
person3.details()