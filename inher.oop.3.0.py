class person :
    def __init__(self,name,dob,height,weight):
        self.name = name
        self.age = dob
        self.height = height
        self.weight = weight

    def print_age(self):
        self.age= 2022-self.dob
   
        print(f"You are {self.age} years old.")
    def print_bmi(self):
        self.bmi= self.height/self.weight
        print("Your bmi is {self.bmi}")
person1 = person("Jerry",2003,1.7,"70kgs")
        

class student(person):
    def __init__(self,name,dob,height,weight,level,fav_food):
        super().__init__(name,dob,height,weight)
        self.level = level
        self.fav_food = fav_food
    def print_level(self):
        print(f"You are in {self.level}")

class teacher(person):
    def __init__(self,name,dob,height,weight,subj,salary):
        super().__init__(name,dob,height,weight)
        self.subj = subj
        self.salary = salary
    def salary(self):
        print(f"Your salary is{self.salary}")