# wap to input two integers and display add,sub,multiply,division,floor division,modulus and exponentiation
a=int(input("enter a number:"))
b=int(input("enter second element:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
# wap that takes an interger as input apply the following operation +=10,-=5,*=2,/=3. display the value after each operation
a=int(input("enter a number:"))
a+=10
print(a)
a-=5
print(a)
a*=2
print(a)
a/=3
print(a)
# wap to input two numbers and check are they equal? are they not equal is first no. is greater aur is second no. is greater
a=int(input("enter a number:"))
b=int(input("enter second number:"))
print("equal",a==b)
print("not equal",a!=b)
print("a is greater",a>b)
print("b is greater",b>a)
# input the two subject marks 
a=int(input("enter the marks of first subject:"))
b=int(input("enter second subject marks:"))
print("pass",a>=35 and b>=35)
print("eligible for scholarship",a>=90 and b>=90)
print("fail",a<35 or b<35)
# input a sentence and a word check whether the word is present in the sentence using the operator
a=input("enter a sentence:")
b=input("enter a word:")
print(b in a)
# word not present in sentence
a=input("enter a sentence:")
b=input("enter a word:")
print(b not in a )
# check whether a is b. then create c and check whether a is c
a=int(input("enter element:"))
b=int(input("enter second element:"))
print("a is b",a is b)
c=int(input("enter a element:"))
print("a is c",a is c)
# bitwise and $or
a=int(input("enter first integer:"))
b=int(input("enter second element:"))
print("bitwise and",a&b)
print("bitwise or",a/b)
# input two interger display bitwise xor and bitwise not
a=int(input("enter a number:"))
b=int(input("enter second element:"))
print("bitwise xor",a^b)
print("bitwise not",~a)
# left shift and right shift
a=int(input("enter a number:"))
print("left shift",a<<2)
print("right shift",a>>2)
# input three numbers if second no. is greater than first and third no. is greater than fist display the result
a= int(input("enter first no.:"))
b=int(input("enter second no.:"))
c=int(input("enter third no.:"))
result=b>a and c>a
print(result)