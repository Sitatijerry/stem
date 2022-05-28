lucky_no = [4,5,2,7,9,1]
friends = ["mosalah","kevin", "roro","foden","mane","silva","silva"]
friends.extend(lucky_no)
print(friends)

friends.append("origi")
friends.insert(1,"jota")
print(friends)

# friends.remove("origi")
# print(friends)
# friends.clear()
# print(friends)

friends.pop()
print(friends)
print(friends.pop())
print(friends.index("kevin"))
print(friends.count("silva"))

lucky_no.sort()
print(lucky_no)
lucky_no.reverse()
print(lucky_no)

friends2 = (friends.copy())
print(friends2)