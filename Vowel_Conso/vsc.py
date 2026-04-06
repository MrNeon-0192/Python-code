o=input("Enter a sentence: ")
vowel=0
consonant=0
spaces=0

for i in o:
    if i == " ":
        spaces=spaces+1
    elif i.lower() in ("a","e","i","o","u"):
        vowel=vowel+1
    else:
        consonant=consonant+1

print("\nVowels: ",vowel)
print("\nConsonants: ",consonant)
print("\nSpaces: ",spaces)
