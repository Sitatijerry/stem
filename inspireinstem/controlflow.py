# if statements 
x=4
if x>=1:
   print("hey im still here")
   x-=1   
   print(x)
   print("done")

#else statements
x=4
if x==10:
   print(x)
else :
    print("not 10")

#elif to create grading system
grade = int(input("write studets score:"))
if grade > 80 and grade<=100:
    print("student got an A")
elif grade >=70 and grade<80:
    print("student got a B")
elif grade >=60 and grade<=69:
    print("student got a C")
elif grade >=50 and grade<=59:
    print("student got a D")
elif grade >=0 and grade<=49:
    print("student got a E")
    