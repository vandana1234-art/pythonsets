# declare one variable of each numerical data type and print their values and data type
a=12
b=56.5
c= 2+3j
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
# convert an interger into a float and complex number
a=12
print(float(a))
print(complex(a))
# create complex no. by comp-lex notation and print real and imaginery part
a=complex(4,5)
print(a)
print(a.real)
print(a.imag)
# calcualte average of three float numbers
a=12.5
b=86.5
c=89.6
print("average is :",(a+b+c)/3)
# demonstrate automatic type promotion using int,float and complex
a=5
b=2.5
c=3+2j
print(a+b)
print(type(a+b))
print(a+c)
print(type(a+c))
# wap to input an integer,a float and complex display their value and data type
a=int(input("enter a number:"))
b=float(input("enter a number:"))
c=complex(input("enter a number:"))
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
# wap that stores the following details using variables
basic_salary=58750
HRA=0.22*basic_salary
DA=0.15*basic_salary
professional_tax=2500
gross_salary=basic_salary+HRA+DA
net_salary=gross_salary-professional_tax
print(gross_salary)
print(net_salary)
# create a variable A=245,B=37,C=-128.75.WAP calculate A^2 using pow().find absolute value as c print the maximum and minimum among A,B,and abs(c)
# calculate the average of all three number . display the result
A=245
B=37
C=-128.75
absolute_c=abs(C)
print(absolute_c)
print(pow(A,2))
avg=A+B+C/3
print(avg)
average=A+B+absolute_c/3
print(average)
print(max(A,B,C))
print(min(A,B,C))
# Create two complex variable :c1=6+9j,c2=4-7j. wap to add the two number multiply them , fnd the magnitude of each complex number
# ,print their data type and memory address
c1=6+9j
c2=4-7j
magnitude_c1=abs(c1)
magnitude_c2=abs(c2)
print(magnitude_c1)
print(magnitude_c2)
print(type(c1))
print(type(c2))
print(id(c1))
print(id(c2))
print(c1+c2)
print(c1*c2)
print(c1.real)
print(c2.real)
print(c1.imag)
print(c2.imag)
# print student profile
a=input("enter your name:")
b=int(input("enter your age:"))
c=input("enter your course:")
d=input("enter your university:")
e=input("enter your city:")
print("na,me=",a)
print("age=",b)
print("course=",c)
print("university=",d)
print("city=",e)