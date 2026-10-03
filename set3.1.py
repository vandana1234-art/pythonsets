# create a list of your 5 favourite movies and display the list
a=["jumanji","dhamal","khiladi","3 idiot","bhagwan"]
print(a)
# create a list containing 10 numbers and display :first,last,middle element
a=[12,34,5,6,7,9,4,6,9,0]
print(a[0])
print(a[-1])
print(a[5])
# create a list of five cities and print the list in reverse orderr using slicing
a=["Delhi","London","Amritsar","Jaipur","Ghaziabad"]
print(a)
print(a[ : :-1])
# create two list of five numbers each and combine them
a=[1,4,5,6,7]
b=[6,7,8,9,4]
print(a+b)
# create a list and display it three times
n=[4,6,7]
print(n*3)
# create a list of five fruits and add one more fruit. Now,insert your favorite color at the second position of the list.
c=["mango","banana","papaya","guava","pineapple"]
print(c)
c.append("grapes")
print(c)
c.insert(2,"pink")
print(c)
# create two list & combine them using extend() now, remove the lat element
a=[4,5,6]
b=[9,8,7]
a.extend(b)
print(a)
a.pop()
print(a)
# create a list of numbers and find the maximum and minimum value
a=[3,3,4,5,6,6,6,7,5,5,4,33,7]
print(max(a))
print(min(a))
# create a list of numbers and sort it in ascending order and descending order
a=[4,5,6,3,2,8,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# reverse a list using reverse() method
a=[5,4,6,7,8,9]
a.reverse()
print(a)
#  create a copy of a list using copy() and print both list
a=[2,5,9,7]
print(a)
b=a.copy()
print(b)
# create a list containing duplicate values and count the occurrence of a particular value using count()
a=[3,4,5,3,5,6,7,8,8]
print(a)
print(a.count(3))
# find the index off a given number using insex()
a=[2,7,8,9]
print(a.index(7))
print(a)
# create a nested list respresenting a 3*3 matrix and print it
a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
# prform some slicing operation
a=[1,2,3,4,5,6,7,8,9,10]
print(a[0:4])
print(a[ :-5:-1])
print(a[0:11:2])
print(a[ : :-1])