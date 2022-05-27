from asyncio import futures


class Dog:
    def __init__(self,no_of_eyes,colour,length_of_fur,no_of_legs):
        self.no_of_eyes = no_of_eyes
        self.colour = colour
        self.length_of_fur = length_of_fur
        self.no_of_legs = no_of_legs
    def barking(self):
        print("woof woof")
    def running(self): 
        print("fast")

german_shepherd = Dog(no_of_eyes=2,colour="grey",length_of_fur="long",no_of_legs=4)
dodger = Dog(no_of_eyes=1,colour="white",length_of_fur="long",no_of_legs=3) 
dobberman = Dog(2,"brown","short",3)
bulldog =  Dog(3,"brown","short",4)

print(german_shepherd.colour, german_shepherd.no_of_eyes)
print(dodger.no_of_eyes, dodger.colour)
print(bulldog.colour , bulldog.no_of_eyes)

dobberman.colour = "dark-brown"
print(dobberman.colour)
print(dobberman.no_of_eyes)
dobberman.barking()
bulldog.barking()

print(german_shepherd.length_of_fur, german_shepherd.no_of_legs)
print(bulldog.colour,bulldog.length_of_fur,bulldog.no_of_legs)
bulldog.running()
bulldog.barking()
print(dobberman.no_of_legs,dobberman.length_of_fur,dodger.length_of_fur)
dobberman.barking()
dobberman.running()
dodger.running()

print("here boy") 
dobberman.running()