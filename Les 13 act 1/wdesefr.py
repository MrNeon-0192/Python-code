string=input("Enter a word: ")

char=input("Enter a character: ")

i=0
count=0
while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
print("The number of times the character appears in the string is: ", count)