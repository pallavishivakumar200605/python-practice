#Lists in python
items=["bru","sugar","milk","jaggry"]
print(items)

#list methods
 
items.pop()
items.pop(0)
items.append("mom's magic")
items.remove("sugar")
items.insert(1,"spoon")
items.clear()


#Slicing Lists

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  
print(numbers[:4])  
print(numbers[2:])  
print(numbers[::2])  

#List Functions 
print(len(items))  #len

#sorted(list)
numbers = [5, 2, 9, 1]
print(sorted(numbers))  
print(numbers)  

#sum(list)
numbers = [1, 2, 3, 4]
print(sum(numbers))  


#Common Methods

#count(element)
numbers = [1, 2, 3, 1, 1]
print(numbers.count(1)) 

#reverse()
items.reverse()
print(items)  

#sort()
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers) 

#Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  
print(matrix[1][1])  


#Tuples in Python
my_tuple = ("apple", "banana", "cherry")
numbers_tuple = (1, 2, 3, 4)

#Accessing Tuple Elements
fruits = ("apple", "banana", "cherry")
print(fruits[0])  
print(fruits[-1])  

# Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  

#uple Repetition
repeated_tuple = (1, 2) * 3
print(repeated_tuple)  

#Checking Membership
print("apple" in fruits)  

#Tuple Methods
#count()
my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1)) 

#index()
my_tuple = ("apple", "banana", "cherry")
print(my_tuple.index("banana"))  

#Sets in Python
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

#Set Operations
#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 

#Intersection
intersection_set = set1 & set2 

#Difference
difference_set = set1 - set2  

#Symmetric Difference
sym_diff_set = set1 ^ set2 

#Set Methods
#add()
fruits_set.add("orange")
print(fruits_set)  

#remove()
fruits_set.remove("banana")
print(fruits_set)  

#discard()
fruits_set.discard("banana")  

#pop()
fruits_set.pop()

#clear()
fruits_set.clear()