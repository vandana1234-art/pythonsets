#  set ek collection hota hai jisme duplicate value nhi hoti aur isko bhi curly brases me likh te hai
a={10,20,30}
print(a)
print(type(a))
# set me number add karne ke liye hum add() aur update ka use karte hai. Agar ek number add karna ho to add() karege aur agar multiple numbers add karne ho to update use karege
a={10,20,30}
a.add(40)
print(a)
a.update([50,60,70])
print(a)
# set se koi number remove karne ke liye hum remove() or discard() ka use akrte hai agar number set me nhi hai to remove errro dega lekin discard error nhi dega
a={10,20,30}
a.remove(20)
print(a)
a={10,20,30}
a.discard(70)
print(a)
# sets ka union aur intersection kaise lete hai
A={2,3,4,5,}
B={2,5,6,4,7,8}
print(A.union(B))
print(A.intersection(B))
print(A-B)
print("symmetric difference",A^B)
# set ka difference kaise karte hai
A={2,3,4,5,}
B={2,5,6,4,7,8}
print(A.difference(B))
print(B.difference(A))
# SET KA SUBSETS KAISE FIND KARE aur disjoint kaise pta karte hai
a={2,3,4,5}
b={2,3,4,5,6,7,8}
print(a.issubset(b))
print(b.issubset(a))
if A.isdisjoint(B):
    print("sets are disjoint")
else:
    print("not disjoint")
# duplicate values ko remove karna
a=[10,0,30,10,20,40,30]
unique_numbers=set(a)
print(a)
print(unique_numbers)
# do students ka common subject find karna
a={"python","java","html"}
b={"java","css","java script"}
print(a&b)
# check two sets are equal or not
a={1,2,3,4}
b={1,2,3,4}
if a==b:
    print("sets are equal")
else:
    print("not equal")
# one set is superset of another set
a={2,3,4,5}
b={2,3,4,5,6,7,8}
if a.issuperset(b):
    print("yes")
else:
    print("no")
# set ki length find karna
b={2,3,4,5,6,7,8}
print(len(b))
# set ko list banana
b={2,3,4,5,6,7,8}
c=list(b)
print(c)
# set se maximum aur minimum element find karna
b={2,3,4,5,6,7,8}
print(max(b))
print(min(b))
# set me element present hai ki nhi
a={2,3,4,5}
c=6
if c in a:
    print("present")
else:
    print("not present")
# set ke element ko loop se print karna
a={2,3,4,5}
for i in a:
    print(i)
# set ko empty karna
a={2,3,4,5}
a.clear()
print(a)
# set ki copy banana
a={2,3,4,5}
b=a.copy()
print(a)
print(b)
# set me multiple elements add karna
a={2,3,4,5}
a.update({6,7,8,9})
print(a)
# set ko frozen set convert karna ye ek immutable set bna deta hai
a={2,3,4,5}
b=frozenset(a)
print(b)
# check set is proper subset aur proper super set  ko another set
a={2,3,4,5}
b={2,3,4,5,6,7,8}
if a<b:
    print("a is proper subset of b")
else:
    print("a is not proper subset of b")
if a>b:
    print("a is proper super set of b")
else:
    print("not proper super set")
# to find sum of set elements
a={2,3,4,5}
b=sum(a)
print(b)