from locale import atoi


name = "jerry sitati"
#multiple line strings
msg = """QRS3SG confirmed you 
have received 1200 from henry safaricom cares for you"""
print(msg)
city = "nairobi"
#.upper()to convert to uppercase
print(city.upper())
print(name.upper())
uni = "JKUAT"
print(uni.lower())
fruit = "mango"
print (fruit[:2])
print(fruit[3:])
print (fruit[-3])
print(fruit[:-3])

#strip removes spaces between words
f_name ="jerry sitati"
print(f_name.strip())
j_name =" jerr ys its atoi"
print(j_name.strip())

f_name ="jerry"
s_name =" sitati"
full_name = f_name + s_name
print(full_name)

city ="malindi" 
print(len(city))
word = "abracadabra"
print(len(word))
word_2 = "deoxyrinonucleic"
print(len(word_2))

#if you want to convert an integer into a string
x=100
print(str(x))
print(x)
y= 3.14
print(int(y))
print(float(y))