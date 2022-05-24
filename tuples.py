# listmethods
# lists(allow changes,duplicate values,order)
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

# tuples(doesnt aloow changes)
fruits_4= ("apples","oranges","bananas")
print(fruits_4)
print(fruits_4[1])

new_list= list(fruits_4)
new_list.append("tomato")
fruits_4= tuple(new_list)
print(fruits_4)

# sets(dont allow redundancy/duplicate values)
fruits_5={"apple","oranges","oranges","oranges"}
print(fruits_5)