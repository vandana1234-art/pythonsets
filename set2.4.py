# jab tak condition true hai, tab tak code repeat hoga
i=1
while i<=5:
    print(i)
    i=i+1
# how to print 1 to 10 number by while loop
i=1
while i<=10:
    print(i)
    i=i+1
#  reverse me print karo number
i=10
while i>=1:
    print(i)
    i=i-1
#  print 1 to 20 even numbers
j=1
while j<=20:
    if j%2==0:
        print(j)
    j=j+1
# print odd numbers
r=1
while r<=20:
    if r%2!=0:
        print(r)
    r=r+1
#  numbers ka sum nikalna
a=1
sum=0
while a<=10:
    sum=sum+a
    a=a+1
print(sum)
# print the sum of squares of numbers
b=1
sum=0
while b<=10:
    sum=sum+b*b
    b=b+1
print(sum)
# number ke square print karo
g=1
while g<=10:
    print(g*g)
    g=g+1
# factorial nikalne ka trika
q=1
fact=1
while q<=5:
    fact=fact*q
    q=q+1
print(fact)
# kisi bhi number ka fact torial find karne ke liye
n=int(input("enter a number"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)