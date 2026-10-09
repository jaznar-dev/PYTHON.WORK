sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = 0
spaces = 0
digits = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch == " ":
        spaces += 1
    elif ch.isdigit():
        digits += 1

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)