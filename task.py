#create a single function that:
    #for a range of integers between 0 and n(inclusive)
    #if the number is an even number,
        #Half it
    #if the number is an odd number 
        #double it
    

    #for the output generated in the previous function,
    #write the result to a file named    'results.txt'

def print_num(n):
    for num in range (n +1):
        if num %2 ==0:
            print(num/2)
        elif num%2 != 0:
            print(num *2)
ans = print_num(10)
print(ans)

f = open("results.txt","w")
f.write(str(ans))

f.close()