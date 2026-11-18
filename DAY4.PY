#Dictionaries in Python

birthday={
    "pallavi":"05-06-2006",
    "nayana":"07-05-2004",
    "harshitha":"25-04-2002"

}


# Accessing Dictionary Elements
print(birthday["pallavi"])
print(birthday.get("Shivakumar", "Not Found")) 

#Adding and Updating Dictionary Elements


#Adding an Item
birthday["Shivakumar"] = "01-01-1999"
print(birthday)


#Updating an Item
birthday["pallavi"] = "05-07-2009"


#Removing Elements from a Dictionary
dates = birthday.pop("nayana")  #pop()
print(dates)  

del birthday["pallavi"]  #del

birthday.clear() #clear


#Dictionary Methods
print(birthday.keys())  #keys()

print(birthday.values())  #values()

print(birthday.items()) #items()

new_dates={"anu":"10-10-2010"}  #update()
birthday.update(new_dates)



         




