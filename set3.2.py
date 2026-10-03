
#create a tuple 
a=(10,20,30,40,50)
print(a)
# create a tuple of five integers and print all elements. Accesss the first,last,and middle elements of a tuple
a=(1,2,3,4,5)
print(a[0])
print(a[-1])
print(a[2])
# count occurence of a specific value.Also,find the index of a given element.
a=(4,4,5,6,66,7,7,7,3)
print(a)
print(a.count(4))
print(a.index(4))
print(a.index(7))
# concatenate two tuples& display the result. Also repeate the tuple three times.
a=(3,4,5)
b=(5,6,7)
print(a+b)
print((a+b)*3)
# reverse a tuple using slicing,find the max,min,sum&averrage
a=(2,3,4)
print(a)
print(a[ : :-1])
print(max(a))
print(min(a))
print(sum(a))
average=sum(a)/len(a)
print(average)
print(len(a))
# convert a list into a tuple and tuple into a list 
a=[1,2,3]
b=tuple(a)
print(b)
b=(4,5,6)
a=list(b)
print(a)
# create a nested tuple and access the inner element
a=(3,5,(6,7,8),9,1)
print(a[2][2])
t=("ram",20,"CSE")
name,age,branch=t
print(name)
print(age)
print(branch)
print(t)
t=("radha",20,"CSE","ghaziabad")
name,*details=t
print(name)
print(details)
students=[("vandna",85),("radha",78),("priya",94)]
for name,marks in students:print(name,marks)
a=10
b=20
a,b=b,a
print(a)
print(b)
square=tuple(x*x for x in range(1,11))
print(square)