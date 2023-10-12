#Key to Character in a string uaisg dictionary
d={}
name=input("Enter:")
length=len(name)
for i in range(0,length):
    new=d.update({i:name[i]})
print(d)    
