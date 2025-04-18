l=list(map(int,input("Enter the List: ").split()))
print(f"Original Scores: {l}")

new=int(input("Enter new number to append"))
l.append(new)
print(f"After appending {new}: {l}")

r=int(input("Enter the number to be removed"))
if r in l:
    l.remove(r)
    print(f"After removing {r}: {l}")
else:
    print(f"{r} is not in the list")

l.sort()
print(f"Sorted list: {l}")

print(f"Maximum : {max(l)}, Minimum : {min(l)}, Average : {sum(l)/len(l)}")

#print(f"Reversed: {l[::-1]}")
l.reverse()
print(f"Reversed list: {l}")