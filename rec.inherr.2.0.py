class Chef :
    
    def make_chicken(self):
        print("chef makes chicken")

    def make_salad(self):
        print("chef makes salad")

    def make_special_dish(self) :
        print("chef makes pasta")
    
class ChineseChef(Chef):
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

