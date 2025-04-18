N=int(input("Enter a number: "))

if N<=1:
    print("Negative numbers can't be defined as prime numbers")
elif N == 2:
    print("Its a prime number")
else:
    for i in  range (2,N):
        if N%i==0:
            print("Its Not a prime number")
            break
    else:
        print("Its a Prime number")