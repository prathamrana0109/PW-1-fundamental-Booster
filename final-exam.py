print("==========Welcome to Inventory List Analyzer==========")
print(" ")

item_list = []
category_list = []
category_dict = {}
quantity_list = []

item=input("Enter the item name: ")
category=input("Enter the item category: ")
quantity=int(input("Enter the item quantity: "))

item_list.append(item)
category_list.append(category)
category_dict={"category":category}
quantity_list.append(quantity)

choice = input("Do you want to add another item? (yes/no): ")
if choice=="yes"or choice=="Yes" or choice=="YES" or choice=="y" or choice=="Y" or choice=="yEs" or choice=="yeS" or choice=="YeS" or choice=="yES" or choice=="YEs" or choice=="YeS" or choice=="YES":

        item=input("Enter the item name: ")
        category=input("Enter the item category: ")
        quantity=int(input("Enter the item quantity: "))
        item_list.append(item)
        category_list.append(category)
        category_dict={"category":category}
        quantity_list.append(quantity)
        choice = input("Do you want to add another item? (yes/no): ")
        
elif choice=="no" or choice=="No" or choice=="NO" or choice=="n" or choice=="N" or choice=="nO" or choice=="No" or choice=="nO": 
        print("Moving To Inventory Summary...")
else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
print("==========Inventory Summary==========")
print(" ")
count = 0
for i in range(len(item_list)):
    count += 1
print("Total number of items in the inventory: ",count)
total_quantity =sum(quantity_list)
print("Total quantity of items in the inventory:",total_quantity)
avg_quantity = total_quantity / count
print("Average quantity of items in the inventory:",avg_quantity)
print("Most Stocked Item:", item_list[quantity_list.index(max(quantity_list))])
print("Least Stocked Item:", item_list[quantity_list.index(min(quantity_list))]) 
print(" ")
print("Unique Categories in the Inventory:", set(category_list))
print(" ")
print(" ")
print("Items Sorted by Quantity (Descending):")
print(" ")
sort_quantity = sorted(quantity_list, reverse=True)
for i in sort_quantity:
    index = quantity_list.index(i)
    print(item_list[index], "-", i)
    print(" ")
print(" ")
print("Categories Sorted in Alphabetical Order:")
print(" ")
for i in sorted(set(category_list)):
    print(i)
    print(" ")



    



    
