file=input()

try:
    with open(file,'r') as f:
        concept=f.read()
        words=concept.split()
        print(len(words))

except FileNotFoundError:
    print("File not found.")