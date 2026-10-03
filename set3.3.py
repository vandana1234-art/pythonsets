# slicing of string
A="python"
print(A[0:3])
print(A[2:6])
print(A[ :4])
print(A[3: ])
print(A[-4:-1])
print(A[ : : ])
print(A[0:7])
B="java"
print(B)
print(B[0:3])
print(B[1:4])
print(B[0:4])
C="vandna"
print(C)
print(C[0:6])
print(C[1:4])
print(C[0:5])
print(C[2:6])
print(C[0:7])
print(C[ : : ])
D="Vanshika"
print(D[1:5])
print(D[0:7])
# indexing of string
A="python"
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[5])
print(A[-1])
print(A[-2])
print(A[-3])
print(A[-4])
print(A[-5])
print(A[-6])
# input a string from the user and display original string,length and data type
a=input("enter the sentence:")
print(a)
print(len(a))
print(type(a))
# to print the slicing
a=input("enter a atring:")
print(a[0:5])
print(a[0:5:-1])
print(a[3:11])
print( a[: :2])
print(a[ : :-1])
# counts the number
a=input("enter a string:")
uppercase=0
lowercase=0
digits=0
spaces=0
special=0
for ch in a:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        special+=1
print(uppercase)
print(lowercase)
print(digits)
print(spaces)
print(special)
# to check a string is palindrome or not
a=input("enter a string:")
reverse=a[ : :-1]
if a==reverse:
    print("palindrome")
else:
    print("not pLindrome")
# to replace every space with (-) hyphen by both replace and join
a=input("enter a string:")
b=a.replace(" ","-")
print(b)
# by joint
a=input("enter a string:")
b="-".join(a.split())
print(b)
# to check two string are anagrams or not
a=input("enter first string:")
b=input("enter second string:")
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not amagram")
# to find frequency of a character in a given string
a=input("enter a string:")
ch=input("enter the character to count:")
count=0
for i in a:
    if i==ch:
        count+=1
        print(count)
# to count number of vowels and consonents
a=input("enter a string:")
vowels=0
consonents=0
for i in a:
    if i.lower()in "aeiou":
        vowels+=1
    elif i.isalpha():
        consonents+=1
print(vowels)
print(consonents)
# to count number of words
a=input("enter a string:")
words=a.split()
print(len(words))
# remove duplicate characters from a string
a=input("enter a string:")
result=" "
for ch in a :
    if ch not in result:
        result=result+ch
print(result)
# find the longest word in a sentence
a=input("enter a sentence:")
words=a.split()
longest=words[0]
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)
# perform some operation
a=input("enter a string:")
print(a.split())
print(a.swapcase())
b=input("enter a word to replace:")
c=input("enter a new word:")
print(a.repalce(b,c))
