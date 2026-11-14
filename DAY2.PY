#string repeatation
message="this is pallavi"
print(message*10)

#string methods(some)

print(message.upper())#UPPER
print(message.lower())#lower
print(message.strip())#strip

#replacing
print(message.replace("this is pallavi","hello"))


#multiline string
name=''' pallavi said "hello"
         nayana said "hi"
         '''


#string length
print(len(message))

#accessing string character

name1="pallavi"
print(name1[2])


#string slicing

print(name1[2:7])


#slicing backward

print(name1[-2])

#string step

print(name1[::2])


#escape sequence
 
s="pallavi \nis a good girl"  #using \n
print(s)
t="pallavi \tis a good girl"  #using \t


#operators
#1 Assignment Operators
x = 5  
x += 3  
x -= 2  
x *= 4  
x /= 6 

#2 Comparison Operators

a = 10
b = 20

print(a == b)  
print(a != b)  
print(a > b)  
print(a < b)  
print(a >= 10)  
print(b <= 25)  


# 3 Logical Operators

x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5) 

# or operator
print(x > 10 or z > 10)  
# not operator
print(not(x > 10)) 


# 4 Membership Operators

my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list)  
print(6 not in my_list)  
print("P" in my_string)  
print("z" not in my_string)  


# 5 Bitwise Operators

a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  

# Bitwise OR
print(a | b)  
# Bitwise XOR
print(a ^ b)  

# Bitwise NOT
print(~a)  

# Left shift
print(a << 1)  
# Right shift
print(a >> 1) 

