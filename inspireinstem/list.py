#lists
words = ["apples","love","people","!"]
print(words[0])
print(words[1])
print(words)
print(words[3])

#lists can store ant data types
numbers = [5,6,7,8]
print(numbers[2])

dat= ["a",1,"foo",6,7,"hey"]
print(dat)

#nested lists
m=[
    [5,7,8],#1st row
    [3,2,1] #2nd row
] 
print(m[1][2])
print(m)

#strings can also be included as lists
str = "hello class"
print(str[5])
print(str[6])
print(str[7-3])
print (str[8-1])


#list index can be readdressed
subjects = ["math","science","religous"]
subjects[2]="mechanics"
print(subjects)