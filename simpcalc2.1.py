a = float((input("Enter first no :")))
op = (input("Enter operator :"))
b = float((input("Enter second no :")))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Invalid operator")
print("Done")