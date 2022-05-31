class Chef :
    
    def make_chicken(self):
        print("chef makes chicken")

    def make_salad(self):
        print("chef makes salad")

    def make_special_dish(self) :
        print("chef makes pasta")

class Chinese_chef :
    def make_chicken(self):
            print("chef makes chicken")

    def make_salad(self):
        print("chef makes salad")

    def make_special_dish(self) :
        print("chef makes fried rice")
    
    def make_tuna(self):
        print("makes tuna")

   
myChef = Chef()
myChef.make_chicken()

myChef.make_salad()

myChinese_chef = Chinese_chef()
myChinese_chef.make_special_dish()
