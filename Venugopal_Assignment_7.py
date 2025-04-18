import string

def clean(str):
    str = str.lower()
    for i in string.punctuation:
        str = str.replace(i,"")
    return str

def check(s1,s2):
    word1 = set(s1.split())
    word2 = set(s2.split())

    unq = word1 | word2
    com= word1 & word2

    percent=(len(com) / len(unq)) * 100
    if percent >0:
        print(f"Common Words: {com}")
        print(f"Similarity: {percent}")
    else:
        print("Zero 0% Plagiarism")


#s1 = "Machine learning is super powerful and useful."
#s2 = "Learning machines is very useful in data science."

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

s1=clean(s1)
s2=clean(s2)

check(s1,s2)

