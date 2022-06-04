
is_male = False
is_tall = False

if is_male and is_tall :    # or ,and
    print("You are a tall male")  
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not male")
else:
    print("You are neither a male nor tall")

def max_no (a,b,c):
    if a >= b and a >=c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

max_no(30,400,5)