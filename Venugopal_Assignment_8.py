#Assignment 8
timestamp={
    'Alice':[8, 9, 7],
    'Bob':[10, 5, 6]
}

def add_emp():
    name=input("Add new Employee")
    hr=list(map(int,input("Add Working hours:").split()))
    timestamp[name]=hr

add_emp()

max=0
for name in timestamp:
    t=sum(timestamp[name])
    if max<t:
        max=t
        x=name


print(f"Total hour for {x} : {max}")
print(f"Most Hardworking: {x}")








