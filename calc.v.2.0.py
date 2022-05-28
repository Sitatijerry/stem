
try:
    x= float(input("enter 1st no :"))
    y= float(input("enter 2nd no :"))
except:
    print("invalid input")

op=input("insert operator")
if op=="*":
    print(x*y)
elif op== "-":
    print(x-y)
elif op== "+":
     print(x+y)
elif op== "/":
    print(x/y)
else:
    print("invalid operator")
# x=float(input("insert first no"))
# op = input("insert operator")
# y= float(input("insert second no"))
# if op=="*":
#     print(x*y)
# if op=="+":
#     print(x+y)
# if op=="-":
#     print(x+y)