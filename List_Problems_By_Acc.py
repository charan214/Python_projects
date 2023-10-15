#If the item in List-b present in List-a maultiply item*constant else multiply with -(constant)
'''a=[2,3,5,7]
b=[3,5,3,4]
c=int(input("Constant:"))
s=0
for i in b:
    if(i in a):
        s=s+(i*c)
    else:
        s=s+(i*(-c))
print(s)'''
#The integer items in list.return count which the item is sum of[item power of 2 and item power of 3]
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
c=0
for j in l:
    for k in l:
        m_p=(j**2)+(k**3)
        if(m_p in l):
            c=c+1
print(c)
             
