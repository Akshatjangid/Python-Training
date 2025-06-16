# cafe management system

# define menu of restaurent
menu = {
    'pizza':140,
    'pasta':70,
    'burger':40,
    'salad':50,
    'coffee':70,
}



#great
print("Welcome To Python Cafe")
print("pizza: Rs140\npasta: Rs70\nburger: Rs40\nsalad: Rs50:\ncoffee: Rs70\n")

order_total = 0

item_1 =input("enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print (f"your item {item_1} has been adeded in your order" )
else:
    print(f"order item {item_1} is not availabel yet")

anotherorder = input("do you want to add another item ? (yes/No)")
if anotherorder == "yes":

        item_2 =input ("enter the name of second item")
        if item_2 in menu:
            order_total +=menu[item_2]
            print(f"order item {item_2} has been added in your order")

        else:
            print(f"orderd item {item_2} is not available!")

print(f"the total amount to pay for your order is {order_total}")            

            
