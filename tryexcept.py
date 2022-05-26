# try,except tocatch errors
try:
    div = 10/0
    value= int(input("enter a no : "))
    print(value)
except ValueError :
    print("invalid no entered")
except ZeroDivisionError :
     print("divided by zero")
     