def add(a,b):
    print(f"\nThe addition of {a} and {b} is {int(a+b)}\n") # type convert result into INT
def sub(a,b):
    print("The subtraction of {} and {} is {}\n".format(a, b, a-b))  #used .format to print output
def multi(a,b):
    print(f"The multiplication of {a} and {b} is {int(a*b)}\n") # using f string to print output
def div(a,b):
    if b==0: # using if condition for zero division
        print(f"{a} Number cannot be divided by zero")
    else:
       print(f"The division of {a} and {b} is {a / b:.2f}")

# map(input().split()) to read two inputs a same time
# used float to covert input string into float as we can do any operation in float
n1,n2=map(float,input("Enter the u r numbers: ").split())

#created methods to each task
add(n1,n2)
sub(n1,n2)
multi(n1,n2)
div(n1,n2)


