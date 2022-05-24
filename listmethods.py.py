# listmethods
fruits= ["apple","orange","banana"]
fruits_2= ["pawpaw","plums"]
fruits.append("cherry")
fruits.append("mangoes")
print(fruits)
fruits.remove("cherry")

print(fruits)
my_fruits= fruits.pop(1)
print(fruits)
print(my_fruits)

fruits_3= fruits + fruits_2
print(fruits_3)

fruits.extend(fruits_2)
print(fruits)

fruits_2.clear()
print(fruits_2)