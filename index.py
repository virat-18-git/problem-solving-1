# # 1.find min,max,sum:
list=[1,25,-5,18,36.5,-7,22]
max_num=list[0]
min_num=list[0]
sum=0
for i in range(0,len(list)):
    print(list[i])
    if list[i]>max_num:
     max_num=list[i]
    if list[i]<min_num:
       min_num=list[i]
    sum+=list[i]
print(max_num)
print(min_num)
print(sum)

# # 2.to find age of two members:
ramesh=input("enter the ramesh age")
suresh=input("enter suresh age")
if ramesh>suresh:
   print("ramesh is elder than suresh")
elif ramesh==suresh:
   print("botha are twins")
else:
   print("reamesh is younger than suresh")

#    if ages are not equal then we use terinary operator
# str='suresh is younger'if ramesh>suresh else 'suresh is elder'

 # to find the age of three members:
ramesh=input("enter the ramesh age")
suresh=input("enter suresh age")
naresh=input("enter naresh age")
if ramesh and suresh>naresh:
   print("naresh is younger")
elif ramesh>suresh:
   print("suresh is younger")
else:
   print("ramesh is younger")


# # 3.basic operations without and with functions:
x=6
y=3
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x//y)

def basic_operation(a,b):
   sum=a+b
   div=a/b
   sub=a-b
   mul=a*b
   exp=a**b
   return sum,div,sub,mul,exp
res=basic_operation(18,5)
print(res)

 # 4.to check leap year :
year=int(input("enter the year"))
if(year%100!=0 and year%4==0) or year%400==0:
   print("leap year")
else:
   print("non leap year")

# 5.if triangle sides are valid:
side1=int(input("enter the number"))
side2=int(input("enter the number"))
side3=int(input("enter the number"))
if(side1+side2>side3) and (side2+side3>side1) and(side1+side3>side2):
   print("TRIANGLE POSSIBLE") 
else:
   print("not possible")

# 6.program to check vowels,consonents or neither:
str=input("enter a single variable ").lower()
if len(str) > 1 or len(str) == 0:
   print("wont run code")
else:
 if str in 'aeiou':
   print("vowels")
 elif str.isalpha():
   print("consonents")

 else:
   print("Neitherr")