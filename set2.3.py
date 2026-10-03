# 1 to 50 ke even and odd numbers separately print karna
even=[]
odd=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even )
print(odd)
# 1to 100 me3 aur 5 dono se divisible numbers ka sum
sum=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        sum=sum+i
print(sum)
# 10 numbers me positive,negative aur zero count karna
num=int(input("enter a number:"))
for i in range(10):
    if num>0:
        positive+=1
        print("positive")       
    elif num<0:
        negative+=1
        print("negative")
    else:
        zero+=1
    print("zero")
# armstrong number check karna
num=int(input("enter a number:"))
temp=num
sum=0
digits=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**digits
    temp=temp//10
if sum==num:
    print("armstrong number")
else:
    print("not a armstrong number")
# 1 to 5 multiplication tables,sirf even multiples
for i in range(1,6):
    print(i)
    for j in range(1,11):
        result=i*j
        if result%2==0:
            print(i,"*",j,"=",result)   
# pattern 
for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print((i,j))
# same (i,j) pairs-sumeven
for i in range(1,6):
    for j in range(1,6):
        if(i+j)%2==0:
            print("(",i,",",j,")")
# 1 to 10 print karo number 5 par pass use karo
for i in range (1,11):
    if i==5:
        pass
    print(i)
# number repeatedly accept karo,0 enter karne par break
while True:
    num=int(input("enter a number:"))
    if num==0:
        break 
    print("you entered:",num)
print("loop terminated")
# 1 to 20 print karo multiples of 3 skip using continue
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
# tables 2 to 5 mutliples 1 to 10 sirf 3 se divisible multiples
for i in range(2,6):
    print(i)
    for j in range(1,11):
        result=i*j
        if result%3==0:
            print(i,"*",j,"=",result)

