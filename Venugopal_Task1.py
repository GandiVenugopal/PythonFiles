# 1. What are the standard data types in Python?
print("--------1---------")
a=5
b=5.7
c="python" #c='c'
d=True
L=[1,2,3]# (1, 2, 3) - tuple,
S={1,2,3}
print("Data Types")
print(type(a),type(b),type(c),type(d),type(L),type(S))

# 2. What is the difference between mutable and immutable data types?
print("\n--------2---------")
#Two types objects that can changed after creation
print("Mutable - Objects that can be changed after creation Ex:- List,dict,set")
print(type(L),type(S))

print("Immutable: Objects that cannot be changed after creation. Ex:- int,float,str,tuple")
print(type(a),type(b),type(c))


# 3. What is the difference between a list and a tuple?
print("\n--------3---------")
print("List=[1,2,3] Syntax -[], can be changed")
print("Tuple=(1,2,3) Syntax -(), cann't be changed")

# 4. How do you define a dictionary in Python?
print("\n--------4---------")
print("A dictionary is defined using curly braces {}")
my_dict = {"name": "Venu", "age": 26}
print(my_dict)

# 5. What is the difference between int and float data types?
print("\n--------5---------")
print("Int stores the whole number, 5,7,10..")
print("Float store the decimal numbers, 5.5, 3.4,7.9..")

# 6. What is the output of type(10) and type(10.0)?
print("\n--------6---------")
print(type(10))
print(type(10.0))

# 7. What is the difference between is and == in Python?
print("\n--------7---------")
print("== its checks values in variable same or not, is - checks variable memory location same or not")

# 8. How do you convert one data type to another in Python? Give an example.
print("\n--------8---------")
print("By doing type casting int(x)")
x='123'
print(type(x))
y=int(x)
print(type(y))

# 9. How do you check the data type of a variable in Python?
print("\n--------9---------")
print("we can check the data type by type() syntax")

#10. What is a set in Python? How is it different from a list?
print("\n--------10---------")
print("Set is collection of unique elements, where as list store duplicate elements")

# 11. Can you store different data types in a Python list?
print("\n--------11---------")
print("Yes, Python lists can hold elements of different data types.")
lt=[1,3.5,'L','List',True,[1,4],"The is list"]
print(lt)

#12. What is type casting? How does it work in Python?
print("\n--------12---------")
print("Type casting is the process of converting one data type to another.")
print("You can use built-in functions like int(), float(), str()")

# 13. What happens when you add an int and a str in Python?
print("\n--------13---------")
print("You get a TypeError, because Python doesn’t allow implicit conversion between int and str.")

# 14. What is a list in Python?
print("\n--------14---------")
print("List is a ordered collection that can hold a mix of data types")

# 15. How do you create a list in Python? Give an example.
print("\n--------15---------")
print("You can create a list using square brackets [].")
fruit=['Apple','Grape','Orange']
print(fruit)

# 16. How do you access elements in a list using indexing?
print("\n--------16---------")
print(fruit[0])
print(fruit[1])
print(fruit[2])

# 17. What is negative indexing in lists? Give an example.
print("\n--------17---------")
print("Negative indexing lets you access elements from the end of the list.")
print(fruit[-1])
print(fruit[-2])

# 18. How do you add elements to a list? Explain append(), extend(), and insert().
print("\n--------18---------")
print("append- adds a single item at the end.")
print("extend - it is used to add multiple items to the end ")
print("insert - it is used to insert an element at a specific position.")

# 19. How do you remove elements from a list? Explain remove(), pop(), and del.
print("\n--------19---------")
print("remove() - it removes the required element from the list")
print("pop(index) - it removes and returns the item at the given index ")
print("del is used to delete the element by index or to delete entire list ")

# 20. What happens if you try to access an index that is out of range?
print("\n--------20---------")
print("if we try to access an index that is out of range, it will give a IndexError")

# 21. How do you reverse a list in Python?
print("\n--------21---------")
my_list=[1,2,3,4,5]
my_list.reverse()
print(my_list)

# 22. How do you find the index of an element in a list?
print("\n--------22---------")
idx=fruit.index("Orange")
print(idx)

# 23. How do you iterate through a list using a for loop?
print("\n--------23---------")
for i in my_list:
    print(i)

# 24. What is the syntax of an if statement in Python?
print("\n--------24---------")
x=5
if x==5:
    print("It is equal to 5")

# 25. How does the if-else statement work? Give an example.
print("\n--------25---------")
if x<3:
    print("It is less than 3")
else:
    print("It is greater than 3")

# 26. What is the role of the elif statement?
print("\n--------26---------")
print("elif is used if we have more than 1 condition to check")

x=5
if x<5:
    print("It is less than 5")
elif x==5:
    print("It is equal to 5")
else:
    print("It is greater than 5")

# 27. How do you check if a number is divisible by both 3 and 5 using if-else?
print("\n--------27---------")
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

# 28. Write a Python program to check whether a person is eligible to vote (age ≥ 18).
print("\n--------28---------")
age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 29. What happens if you don’t use indentation properly in an if-else statement?
print("\n--------29---------")
print("Python will raise a indentation error")


# 30. Write a Python program to compare two numbers and print the larger one.
print("\n--------30---------")
a=5
b=9
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")

#31. How can you use an if statement without an else?
print("\n--------31---------")
x=5
if x==5:
    print("It is equal to 5")

# 32. Write a program to check if a given year is a leap year or not.
print("\n--------32---------")
year=2024       #year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400!=0):
    print(year ,"It is a leap year")
else:
    print(year ,"Not a leap year")

# 33. How do you use a nested if statement? Provide an example.
print("\n--------33---------")
marks=85
if marks>80:
    if marks>90:
        print("First class")
    elif marks<90:
        print("Second class")
else:
    print("Third class")

#34. Write a program to check if a character is a vowel or consonant.
print("\n--------34---------")
s='e' # vowels are a,e,i,o,u
if s in "aeiou":
    print(s+"-is a vowel")
else:
    print(s+"-is not a vowel")


#35. How can you check if a given number is within a specific range (e.g., 10–50)?
print("\n--------35---------")
n=30 #n = int(input("Enter a number: "))
if 10<=n<=50:
    print("Number is in range 10-50")
else:
    print("Number is not in range 10-50")