#  to calculate the average of first n natural numbers . when n is entered by user
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    average=sum/n
print(average)
# to print the multiplication table of n where n is to be entered by the user
n=int(input("enter a number:"))
mult=1
for i in range(1,11):
    mult=n*i
    print(mult)
# to calculate the factorial
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
# to calculate the power(x,n)
x=int(input("enter a number:"))
n=int(input("enter a number:"))
power=1
for i in range(n):
    power=power*x
print(power)
# sum of series
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+1/i
    print(sum)
# calendar of a month
a=input("enter days:")
b=int(input("enter no of day:"))
print("mon,tue,wed,thur,fri,sat,sun")
for i in range(1,a):
    print(" ",end="")
    for b in range(1,b+1):
        print("b",end=" ")
        if (a+b-1)%7==0:
            print()
# pattern question
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
n=4
num=0
for i in range(1,n+1):
    for j in range(i):
        print(num,end="")
        num=num+1
    print()
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()