#  create a dictionary containing details of employees 
employee={"name":"vandna","branch":"CSE","salary":45000,"designation":"software engineer"}
print("name")
print("branch")
print("salary")
print("designation")
# to add the following detalis email and phone number
employee={"name":"amit","department":"CSE","salary":45000}
employee["email"]="amit@gmail.com"
employee["phone number"]="7894561235"
print(employee) 
# to update the salary of employee
employee={"name":"vandna","salary":45000}
print(employee)
employee["salary"]=52000
print(employee)
# to remove a specific key and last inserted item
a={"name":"radha","branch":"CSE","age":20,"marks":85}
a.pop("age")
print(a)
a.popitem()
print(a)
# # dictionary me data key value pair me hota hai aur dictionary curly braces me likh te hai
student={"name":"vandna","age":20,"branch":"CSE"}
print(student["name"])
print(student["age"])
print(student["branch"])
# agar kisi key ki value ko change karna ho to
student={"name":"vandna","age":20,"branch":"CSE"}
student["age"]=23
# print(student["age"])
print(student)
# how to add new key in the dictionary
student={"name":"vandna","age":20,"branch":"CSE"}
student["city"]="ghaziabad"
print(student)
# dictionary se koi key delete karne ka tarika
student={"name":"vandna","age":20,"branch":"CSE"}
# del(student["age"])
student.pop("age")
print(student)
# dictionary se sari keys ,values aur items yani key value pair nikalne ka tarika
student={"name":"vandna","age":20,"branch":"CSE"}
print(student.keys())
print(student.values())
print(student.items())
# to find key exist or not
a={"roll":101,"name":"sita"}
key=input("enter key:")
if key in a:
    print("key found")
else:
    print("not found")
# dictionary to empty karna
a={"name":"vandan","age":20}
print(a)
a.clear()
print(a)
# dictionary ko copy karna
a={"name":"vandan","age":20}
b=a.copy()
print(b)
# create nested dictionary and display some thing
students={"s1":{"name":"radha","branch":"CSE","CGPA":8.5},"s2":{"name":"mishti","branch":"CSE","CGPA":8.6}}
print(students["s2"]["name"])
print(students["s2"]["branch"])
# create nested dictionary for each departement ofRDEC contain HOD name, number of faculty and number of student
department={"CSE department":{"HOD name":"luv dixit","faculty member":23,"no. of sstudents":256},"ECE department":{"HOD name":"rajendra","faculty member":20,"students number":65}
            ,"ME department":{"HOD name":"hariom","faculty member":12,"no. of students":35}}
print(department["ECE department"]["HOD name"])
print(department["CSE department"]["no. of students"])
print(department["ME department"]["faculty member"])
department["CIVIL"]={"HOD name":"dr. gupta","faculty":10,"students":36}
print(department.keys())
print(department)