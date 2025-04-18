def Factor(n):
    if n==0:
        return 1
    else:
        return n*Factor(n-1)

def Sum(n):
    if n == 1 or n==0:
        return n
    else:
        return n + Sum(n - 1)


n=int(input("Enter the number"))

if n<0:
    print("Enter positive number")
else:
    F=Factor(n)
    S=Sum(n)

print(f"Factorial of {n} is {F} ")
print(f"Sum of {n} is {S}")