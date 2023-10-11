#Using functions reversing ASCII of Character in String and returing character count
def rev(a):
    for i in a:
        y=len(i)-1
        while(y>=0):
            print(i[y],end="")
            if(y==0):
                print("")
            y-=1

def counting(x):
    l=list(x)
    l1=len(l)
    c=[l.count(i)for i in l]
    d=dict(zip(l,c))
    print(d)

def main():
    r=" "
    b=[]
    s=input("Enter:")
    for i in range(0,len(s)):
        r=r+s[i]
        c=ord(s[i])
        c1=str(c)
        b.append(c1)
    print(r)
    print(b)
    rev(b)
    counting(s)
main()



        
