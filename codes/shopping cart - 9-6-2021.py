cart = {}
while True:
    print("1.Add item\n2.remove\n3.View\n4Exit")
    ch = int(input("Enter the your choice:"))
    if(ch == 1): # ADD Item
        name = str(input("Enter the product name"))
        if name in cart.keys(): # to check the given name is in the list
            input('The item is already there if you want to make change \n 1.add few more \n 2. remove few\n')
            option = int(input('Enter your option:'))
            if (option == 1):#option is to add some quantity
                print("the existing Quantity in the cart is: ",quantity)
                newquantity = int(input("Enter the quantity of the item:"))
                quantity += newquantity
                total = price * quantity
                cart[name] = [price,quantity,total]
            elif(option == 2):#option is to remove quantity
                newquantity = int(input("Enter the quantity of the item you want to reduce:"))
                if (newquantity == 0): #it is to check the quantity is 0 then pop the item
                    print('The quantity value is 0 so it is removed from the cart list')
                    cart.pop(name)
                else: # minimize the quantity
                    quantity -= newquantity
                    if quantity == 0: 
                        print('The item is removed from the list')
                        cart.pop(name)
                    else:
                        print('The quantity has been changed')
                        total = price * quantity
                        cart[name] = [price,quantity,total]
        else: #if it is not in the list this block is used to add the item 
             price = int(input("Enter the prduct price:"))
             quantity = int(input("Enter the quantity of the item:"))
             total = price * quantity
             cart[name] = [price,quantity,total]
    elif(ch == 2): #this is used to remove a item form the list
        remove_item = str(input("Enter the item you want to remove:"))
        if remove_item in cart.keys():
            cart.pop(remove_item)
        else:
            print("The specified item is not in the cart")
    elif(ch == 3): #it is used to view the list
        print(cart)
        print("Item\tPrice\tQuantity\tTotal")
        for i in cart.keys():
            print(i,end="    ")
            for j in cart[i]:
                print(j,end="\t\t")
            print()
    elif(ch==4):
        break;
    else:
        print('Give a valid option.')
            
