# Scenario:
#  Given a paragraph, write a program to calculate the frequency of each word (case-insensitive) and display the top 5 most frequent words.
import string

str=input()

def clean(str):
    str = str.lower()
    for i in string.punctuation:
        str = str.replace(i,"")
    return str

text=clean(str)

str_lt=text.split()

word_counts={}

for word in str_lt:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words[:5]:
    print(f"{word}: {count}")