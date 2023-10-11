print("  WELCOME TO RC HOTEL   ")
Rice={"Veg-Biriyani":60,"Chicken-Biriyani":100,"Mutton-Biriyani":200,"Full-meals":110,"Half-meals":80}
Fries={"Chicken-fry": 65,"Fish-fry": 80,"Prawns-fry": 120,"scrab-fry": 100}
Icecream={"Vennela": 50,"Chocolate": 70,"Strawberry": 80,"Mogal": 90,"Drynut": 100,"Butter-scotch": 60,"Family-pack": 240}
Drinks={"Coco-cola": 40,"Orange": 50,"Mango" :60,"Apple": 70,"Fruit-mix": 80}
shakes={"Chocolate": 50,"Strawberry": 60,"Vennela": 40}
l=["1.Rice","2.Fries","3.Icecream","4.Drinks","5.Shakes"]
def order_placing():
    print("Please select your choice")
    for i in l:
        print(i)
    print("")
    menu=int(input("Enter option:"))
    if(menu>=len(l) or menu<=0):
        order_placing()
    sum=0
    if(menu==1):
        for j in Rice:
            print(j   ,"----->",  Rice[j])
        order=input("Order please:")
        if(order in Rice):
            sum=sum+Rice[order]
        else:
            print("choose valid item")
    if(menu==2):
        for j in Fries:
            print(j   ,"----->",  Fries[j])
        order=input("Order please:")
        if(order in Fries):
            sum=sum+Fires[order]
        else:
            print("choose valid item")
    if(menu==3):
        for j in Icecream:
            print(j   ,"----->",  Icecream[j])
        order=input("Order please:")
        if(order in Icecream):
            sum=sum+Icecream[order]
        else:
            print("choose valid item")
    if(menu==4):
        for j in Drinks:
            print(j   ,"----->",  Drinks[j])
        order=input("Order please:")
        if(order in Drinks):
            sum=sum+Drinks[order]
        else:
            print("choose valid item")
    if(menu==5):
        for j in shakes:
            print(j   ,"----->",  shakes[j])
        order=input("Order please:")
        if(order in shakes):
            sum=sum+shakes[order]
        else:
            print("choose valid item")
    take=input("continue to Display or Drop:")
    if(take=="Drop"):
        print("Total:",sum)
        print("Thank you for order")
    else:
        order_placing()
order_placing()

            

