name=input("enter the name")

list='''
rice   rs 20/kg
salt   rs 30/kg
suger  rs 40/kg
oil    rs 50/liter
paneer rs 100/kg
maggi  rs  10/kg
boost  rs 100/kg
colagte rs 20/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items 
items={'rice':20,'salt':30,'suger':40,'oil':50,'paner':100,'maggi':10,'boosr':100,'colgate':20}
option=int(input("for list of items press 1"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exits:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("enter your quantity"))
        if item in items.key():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price  
            ilist.append(itsm)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterd item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the item yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","jagadeesh supermarket",5*"=")
            print(25*"=","sharma")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ' , 8*' ',ilist[i],3*' ' , qlist[i],plist[i])
                print(75*"-")
                print(50*" ",'totalamount:','rs',totalprice)
                print("gst amount",50*" ", 'rs',gst)
                print(75*"-")
                print(50*" ",'finalamount:','rs',finalamount)
                print(75*"-")
                print(50*" ",'Thanks for visiting' )
                print(75*"-")