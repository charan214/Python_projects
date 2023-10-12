print("")
print("                 Prime or Not using Recursion                ")
print("")
def number():
    num=int(input("Enter number:"))
    if num==0:
        print("Try again")
        number()
    else:
        prime(num)
def prime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if(count==2):
        print(num,"is Prime number")
    else:
        print(num,"is not a Prime")
    op=input("continue or quit:")
    if op=="quit":
        print("Thank You")
    elif op=="continue":
        number()

number()

