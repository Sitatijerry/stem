# file = open("roles.txt","r")
# words = file.read()
# file.close
# print(words)

file= open("roles.txt","a")
file.write("\t i love python")   #\n= new line ... \t= same line
file.close()

# #append
# file= open("roles.txt","a")
# file.append("i also love gaming")
# file.close