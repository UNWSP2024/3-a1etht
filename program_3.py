#Programmer: Alethea Lo
#Date: 2/6/25

#Asking the user to input the weight of the package
weight=float(input("Enter the weight of the package in pounds:"))

#Calculating the shipping cost based on the weight
if weight <=2:
    shipping_cost=weight*1.50
elif weight <=6:
    shipping_cost=weight*3.00
elif weight <=10:
    shipping_cost=weight*4.00
else:
    shipping_cost=weight*4.75

#Display the total shipping cost
print(f"The total shipping charge is: ${shipping_cost:.2f}")