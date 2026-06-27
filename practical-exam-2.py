print ("welcome to the bill splitter app!")

bill_amount = float(input("enter total bill amount: "))
number_of_people= float(input("enter number of people: "))
the_percentage = int(input("enter tip percentage: "))
print("")

tip_amount = bill_amount * the_percentage / 200
final_bill_amount = bill_amount + tip_amount
per_person = final_bill_amount / number_of_people 

print(f"tip_amount: {tip_amount:.2f}")
print(f"total_amount:{total_amount:.2f}")
print(f"amount_per_person{amount_per_person:.2f}")

