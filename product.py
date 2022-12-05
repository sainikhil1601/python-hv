product1=int(input("quantity of product1="))
product2=int(input("quantity of product2="))
product3=int(input("quantity of product3="))
product1Price=40
product2Price=80
product3Price=90
if product1<=0:

    print("enter correct quantity")
    break

total=product1*product1Price+product2*product2Price+product3*product3Price
print(total)