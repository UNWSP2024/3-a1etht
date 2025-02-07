#Programmer: Alethea Lo
#Date: 2/7/25

#Contestants for the prices of hot dogs
HOT_DOG_PRICE= 3.50
CHILI_DOG_PRICE=4.50
CHEESE_PRICE=0.50
PEPPERS_PRICE=0.75
ONIONS_PRICE=1.00
TAX_RATE=0.07

#Function on how to get the type of hot dog
def get_hot_dog():
    print("Choose the type of hot dog:")
    print("1. Hot Dog ($3.50)")
    print("2. Chili Dog ($4.50)")
    choice=input("Enter 1 for Hot Dog or 2 for Chili Dog:")
    if choice == '1':
        return HOT_DOG_PRICE
    elif choice == '2':
        return CHILI_DOG_PRICE
    else:
        print("Invalid choice. Defaulting to Hot Dog.")
        return HOT_DOG_PRICE

#Function on how to get toppings and how to calculate their total
def get_toppings():
    total_toppings_cost = 0
    print("Choose toppings (Enter 'no' to skip):")
    cheese = input("Do you want cheese? ($0.50): ").lower()
    if cheese == 'yes':
        total_toppings_cost += CHEESE_PRICE
    peppers = input("Do you want peppers? ($0.75): ").lower()
    if peppers == 'yes':
        total_toppings_cost += PEPPERS_PRICE
    onions = input("Do you want grilled onions? ($1.00): ").lower()
    if onions == 'yes':
        total_toppings_cost += ONIONS_PRICE
    return total_toppings_cost

#Function on how to get the total cost of the hotdog and toppings
def calculate_total_cost(hot_dog_cost, toppings_cost):
    subtotal=hot_dog_cost+toppings_cost
    tax=subtotal*TAX_RATE
    total_cost=subtotal+tax
    return subtotal, tax, total_cost

#Main programming for hot dogs
def main():
    hot_dog_cost = get_hot_dog()
    toppings_cost = get_toppings()

    subtotal, tax, total_cost = calculate_total_cost(hot_dog_cost, toppings_cost)

    #Display results
    print("\nReceipt:")
    print(f"Hot Dog Cost: ${hot_dog_cost:.2f}")
    print(f"Toppings Cost: ${toppings_cost:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

