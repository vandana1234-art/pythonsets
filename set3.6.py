# # write a function greet() that prints "welcome to python programming"
# def greet():
#     print("welcome to python programming")
# b=greet()
# print(b)
# # write a function square(n) that accepts a number and return its square
# def square(n):
#     b=n*n
#     return(b)
# n=int(input("enter a number"))
# print(square(n))
# # write a function is_even(n) that returns true if the number is even,otherwise false
# def is_even(n):
#     if n%2==0:
#         return("true")
#     else:
#         return("false")
# n=int(input("enter a number"))
# print(is_even(n))
# # maximum(a,b) function banao jo do numbers me se bada number return kare
# def maximum(a,b):
#     if a>b:
#         return(a)
#     else:
#         return(b)
# n=int(input("enter a number"))
# m=int(input("enter second number"))
# print(maximum(n,m))
# # calculate_area(radius) function banao jo circle ka area calulate karke return kate
# def calculate_area(radius):
#     b=3.14*radius*radius
#     return(b)
# n=int(input("enter a number:"))
# print(calculate_area(n))
# # calculate(a,b) function banao jo sum,difference,product and division return kare
# def calculate(a,b):
#     sum=a+b
#     difference=a-b
#     product=a*b
#     division=a/b
#     return(sum,difference,product,division)
# n=int(input("enter a number:"))
# m=int(input("enter second number:"))
# print(calculate(n,m))
# # student_result(marks) function banao jo marks ki list accept kare aur total marks, average marks,highest marks and lowest marks return kare
# def student_result(marks):
#     sum=0
#     count=0
#     for i in marks:        
#         count=count+1
#         sum=sum+i
#         total_marks=sum
#         average_marks=sum/count
#         highest_marks=max(marks)
#         lowest_marks=min(marks)
#     return(total_marks,average_marks,highest_marks,lowest_marks)
# n=[80,70,90,60,85]
# print(student_result(n))
# # count_vowels(text) function banao jo string mein vowels ki counting karke return vowels a,e,i,o,u
# def count_vowels(text):
#     vowels=0
#     for i in text:
#         if i in "aeiou":
#             vowels=vowels+1
#     return(vowels)
# n=input("enter a string:")
# print(count_vowels(n))    
# # reverse_number(n) function banao jo number ko reverse karke return kare
# def reverse_number(n):
#     b=str(n)
#     return(b[ : :-1])
# n=int(input("enter a number:"))
# print(reverse_number(n))
# # factorial(n) function number ka factorial return kare
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return(fact)
# n=int(input("enter a number:"))
# print(factorial(n))
# # write check_prime(n ) function
# def check_prime(n):
#     if n<=1:
#         return(False)
#     for i in range(2,n):
#         if n%i==0:
#             return(False)
#     return True
# n= int (input("enter a number"))
# if check_prime(n):
#     print("prime")
# else:
#     print("not")
# # write a function print_table(n) that prints the multiplication table of n
# def print_table(n):
    
#     for i in range(1,11):
#         table=n*i
#         print(table)
# n= int (input("enter a number"))
# print(print_table(n))
# # write a function sum_of_digits(n) that returns the sum of digits of a number
# def sum_of_digits(n):
#     sum=0
#     while n>0:
#         digits=n%10
#         sum=sum+digits
#         n=n//10
#     return sum
# n=int(input("enter a number"))
# print(sum_of_digits(n))
# # write a function count_numbers(n) that accepts a list and returns the count of positive number
# def count_numbers(n):
#     positive=0
#     negative=0
#     zero=0
#     for i in n:
#         count=count+1
#         if i >0:
#             positive+=1
#         elif i<0:
#             negative+=1
#         else:
#             zero+=1
#     return positive,negative,zero
# n=[5,-2,0,8,-1,0]
# print(count_numbers(n))
# # write a function get_grande(marks) that returns the grade according to:
# def get_grade(marks):
#     if marks>=90:
#         return'a'
#     elif marks>=80:
#         return'b'
#     elif marks >=70:
#         return'c'
#     elif marks>=60:
#         return' d'
#     else:
#         return False

# n=int(input("enter marks"))
# print(get_grade(n))
# # student marks program
# def input_marks():
#     marks=[]
#     for i in range(5):
#         m=int(input("enter marks"))
#         marks.append(m)
#     return marks
# print(input_marks())
# def calcualte_total(marks):
#     total=sum(marks)
#     return total
# def calculate_average(total):
#     average=total/5
#     return average
# def display_result(total,average):
#     print(total)
#     print(average)
#     if average>=40:
#         print("pass")
#     else:
#         print("fail")
# total=calcualte_total(marks)
# average=calculate_average(total)
# display_result(total,average)
# # simple calculatot usinf multiple function
# def add(a,b):
#     return(a+b)
# def subtract(a,b):
#     return(a-b)
# def mutliply(a,b):
#     return(a*b)
# def divide(a,b):
#     return(a/b)
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# op=input(" enter a operation")
# if op=='+':
#     print(add(a,b))
# elif op=='-':
#     print(subtract(a,b))
# elif op=='*':
#     print(mutliply(a,b))
# else:
#     print(divide(a,b))
# # electricity bill
# def get_units():
#     units=int(input("enter a unit:"))
#     return units
# def calculate_bill(units):
#     if units<=100:
#         bill=units*3
#     elif units<=300:
#         bill=100*3+(units-100)*5
#     elif units<=500:
#         bill=100*3+200*5+200*7.5+(units-500)*10
#     return bill
# def display_bill(bill):
#     print(bill)
# units=get_units()
# bill=calculate_bill(units)
# display_bill(bill)
# # shopping bill
# def input_items():
#     price=float(input("enterr items"))
#     quantity=int(input("enter quantity"))
#     return price,quantity
# def calculate_total(price,quantity):
#     total=price*quantity
#     return total
# def calculate_discount(total):
#     if total>=1000:
#         discount=total*10/100
#     else:
#         discount=0
#     return discount
# def generated_bill(total,discount):
#     final_amount=total-discount
#     print(total)
#     print(discount)
#     print(final_amount)
# price,quantity=input_items()
# total=calculate_total(price,quantity)
# discount=calculate_discount(total)
# generated_bill(total,discount)
# # number analysis program
# def input_number():
#     n=int(input("enter a number:"))
#     return(n)
# def check_even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return"odd"
# def check_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return "prime"
# def find_factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return(fact)
# def display(n,even_odd,prime,factorial):
#     print(n)
#     print(even_odd)
#     print(prime)
#     print(factorial)
# n=int(input("enter a number"))
# even_odd=check_even_odd(n)
# prime=check_prime(n)
# factorial=find_factorial(n)
# display(n,even_odd,prime,factorial)
# # convert program into function
# def input_data():
#     name=input("enter name:")
#     marks=[]
#     for i in range(5):
#         marks.append(int(input("enter marks:")))
#     return name,marks
# def calculate_total(marks):
#     return sum(marks)
# def calculate_average(total):
#     return total/5
# def determine_result(average):
#     if average>=40:
#         return"pass"
#     else:
#         return"fail"
# def display(name,total,average,result):
#     print(name)
#     print(total)
#     print(average)
#     print(result)
# name,marks=input_data()
# total=calculate_total(marks)
# average=calculate_average(total)
# result=determine_result(average)
# display(name,total,average,result)
# # function using return
# def calculate(n):
#     square=n*n
#     cube=n*n*n
#     return(cube,square)
# n=int(input("enter a number"))
# square,cube=calculate(n)
# print(square)
# print(cube)
# # function to find largest of three number
# def largest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# a= int(input("enter a number:"))
# b= int(input("enter a number:"))
# c= int(input("enter a number:"))
# result=largest(a,b,c)
# print(result)
# # function to reverse a string
# def reverse_string(text):
#     return[ : : -1]
# text=input("enter a string:")
# result=reverse_string(text)
# print(result)
# # function to check palindrome number
# def is_palindrome(text):
#     if text==text[ : :-1]:
#         return"palindrome"
#     else:
#         return"not palindrome"
# text=input("enter a string:")
# result=is_palindrome(text)
# print(result)
# 