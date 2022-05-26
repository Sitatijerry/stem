#dictionaries
my_dict={ 
     "book" :" dynamics",
   " publisher" :"longhorn",
    "year": 2001,
    "authors":["mike","john"]
}

# accessing item
x= my_dict["year"]
print(x)

# accessing using get
y= my_dict.get("book")
print(y)

# all keys
x= my_dict.keys()
print(x)
# all values
x= my_dict.values()
print(x)
#  printing all items in a dict
x= my_dict.items()
print(x)
#checking if key exists
if "publisher" in my_dict:
    print ("publisher is on my list")