#for loop
from re import X


mangoes="book"
for i in mangoes:
    print(i)
print ("done")

#for loops with lists
words= ["I","DID","A"]
for words in words:
    print(words + "I")

names =["jerry","dennis","stacey"]
for names in names:
    print("hey " + names + " welcome back")

#counting letters
str= "Hello guys welcome back to my class"
count= 0
for x in str:
    if (x=="o"):
        count+=1
print("the no of zero is:",count)

str= "Hello guys welcome back to my class"
count= 0
for x in str:
    if (x=="l"):
        continue
    else:
        print(x)


str= "Hello guys welcome back to my class"
outstr=""
for x in str:
    if x !="l":
        outstr += x
print(outstr)

# ass
str= "hello guys welcome to my lesson"
outstr =""
for x in str:
    if x !="l" and x!="e" and x!="u":
        outstr +=x
print(outstr)
