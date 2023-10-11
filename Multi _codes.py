#sum of two numbers & multiply two numbers
'''number1=30
number2=20
sum=number1+number2
mul=number1*number2
print("sum of",number1,"and",number2,"is",sum)
print("multiplication of",number1,"and",number2,"is",mul)'''
#sum of two numbers & multiply two numbers if product is low or equal to 1000 else print sum
'''number1=30
number2=20
sum=number1+number2
mul=number1*number2
if(mul<=1000):
    print("multiplication of",number1,"and",number2,"is",mul)

else:
    print("sum of",number1,"and",number2,"is",sum)'''
#Print current & previous number sum range(10)
'''j=0
print("current number",j,"previous number",0,j+j)
for i in range(1,10):
    sum=i+(i-1)
    print("current number",i,"previous number",i-1,sum)'''
#print characters from user string at even index position
'''u_s=input("Enter:")
for i in range(0,len(u_s),2):
    print(u_s[i])'''
#Remove n characters from string zero upto n
'''s=input()
r=int(input())
for i in range(r,len(s)):
    print(s[i])
#or use slicing.'''
#checking first and last number of list is eqal or not
'''list1=[10,20,30,40,20]
l1=len(list1)
list2=[10,20,30,40]
l2=len(list2)
def check(a,b):
    if(a[0]==a[b-1]):
        print("True")
    else:
        print("False")
check(list1,l1)
check(list2,l2)'''
#print numbers divisible by 5-0.021sec
'''numbers=[10,20,21,15,30]
for i in numbers:
    if(i%5==0):
        print(i)'''
#palindrome or not
'''n=int(input())
n1=str(n)
r=n1[::-1]
r1=int(r)
if(r1==n):
    print("it is palidrome")
else:
    print("it is not palindrome")'''
#without slicing check palindrome
'''def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(222)'''
#To form a new list contain odd numbers from one list and even numbers from another list
'''l1=[10,21,30,55,44]
l2=[21,33,54,63,97]
l3=[]
for i in l1:
    if(i%2==0):
        l3.append(i)
for j in l2:
    if(j%2!=0):
        l3.append(j)
print(l3)'''

#print tables
'''for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("")'''
#patterns(Triangle)
'''n=5
for i in range(n):
    for j in range(i,n):
        print('',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()'''








