'''12/04/24 - Taylah Wright  (-.'3'.)-
Assessment for L2 CompSci.'''

# Defining important variables/constants/lists
DELIVERY_FEE = 2.50
MAX_PIZZAS = 5
total_profit = 0.00
order_number = 0
pizzas_ordered = 0
pizza_orders = []
pizza_menu = {
  1:["Beef & Onion", 8.50],
  2:["Extra Cheese", 8.50],
  3:["Garlic Cheese", 8.50],
  4:["Hawaiian", 8.50],
  5:["Italian", 8.50],
  6:["Pepperoni", 8.50],
  7:["Vegeterian", 8.50],
  8:["Gourmet Vegeterian", 13.50],
  9:["Margherita", 13.50],
  10:["Meatlovers", 13.50],
  11:["Pepperoni Supreme", 13.50],
  12:["Spicy Supreme", 13.50],
}

# Creating the price calculator function
def price_calculator(order_cost, price):
  '''Calculates the new price of something using the current price stored and adding any extra costs to it.'''
  # Adding the price of whatever is added to the order to the order's total cost
  cost = order_cost + price
  # Making the order cost a global variable to be used outside of this function
  return cost


'''Main Menu'''
# Creating the main menu function
def main_menu():
  '''Displays the main menu and allows the user to chose what they want to do.
  Returns their choice to be used outside of this function.
  '''
  # Taking input from the user as to what they want to do
  choice = input("\n---Main Menu---\n\n 1. Create Order\n 2. Kitchen Screen\n 3. Management Summary\n 4. Exit\n\n>>> ").strip()
  # Making choice a global variable to be used outside of this function
  return choice


'''Ordering'''
# Creating the main order function
def pizza_order():
  '''Allows the user to place their delivery or pick-up order.
  Returns their pizza order to be used outside of this function.
  '''
  # Making sure the program knows the order number variable is global and not local
  global order_number
  order_cost = 0.00
  customer_order = []
  # Creating a loop to allow the user to create multiple pizza order
  while True:
    # Taking input from the user as to what they want to do
    choice = input("\n---Order---\n\n 1. Delivery\n 2. Pick-up\n 3. Exit\n\n>>> ").strip()

    # Checking to see if the user wants to create a delivery order
    if choice == "1":
      print("\nDelivery Selected")
      # Increasing the order number by 1 so each order number is unique and ordered
      order_number += 1
      # Taking the name for the pizza order and storing it in a variable
      name = input("\nWho is this order for?\n>>> ").strip().title()
      # Taking the phone number for the pizza order and storing it in a variable
      phone_number = input("\nWhat is the customer's phone number?\n>>> ").strip()
      # Taking the address for the pizza order and storing it in a variable
      address = input("\nWhat is the address for this order?\n>>> ").strip().title()
      # Adding the delivery fee to the order cost
      order_cost = price_calculator(order_cost, DELIVERY_FEE)
      # Adding the order number, name, phone number and address to the customer's current order list
      customer_order.extend([order_number, name, phone_number, address])
      break

    # Checking to see if the user wants to create a pick-up order
    elif choice == "2":
      print("\nPick-up Selected")
      # Increasing the order number by 1 so each order number is unique and ordered
      order_number += 1
      # Taking the name for the pizza order and storing it in a variable
      name = input("\nWho is this order for?\n>>> ").strip().title()
      # Adding the order number and name to the customer's current order list
      customer_order.extend([order_number, name])
      break

    # Checking to see if the user wants to exit the order UI
    elif choice == "3":
      print("\nReturning to the Main Menu...")
      # Breaking the order UI loop
      break

    # Checking to see if the user entered an invalid option
    else:
      # Printing an error message
      print("\nError: Invalid option!")

  # Creating a loop to allow the user to  
  while True:
    # Checking to see if the user wanted to return to the main menu
    if choice == "3":
      # Breaking the loop so that the user can actually go back to the main menu
      break
    # Getting the returned values from the menu_order function and storing them in variables
    pizza_order, cost, pizza_amount = menu_order()
    # Making sure the program knows the pizzas_ordered and total_profit variables are global and not local
    global pizzas_ordered
    global total_profit
    # Adding the number of pizzas ordered here to the amount ordered all day
    pizzas_ordered += pizza_amount
    # Adding the value of the current order to the amount of each order all day
    total_profit += cost
    # Adding the cost of the selected pizzas to the total
    order_cost = price_calculator(order_cost, cost)
    # Adding their chosen pizzas to their order
    customer_order.extend(pizza_order)
    # Printing an order confirmation message
    print("\nOrder Confirmed!")
    # Checking to see if the user chose to create a delivery order
    if choice == "1":
      # Printing the order number, name, phone number and address of the customer
      print("{}. {} - {}\n{}".format(customer_order[0], customer_order[1], customer_order[2], customer_order[3]))
    # Checking to see if the user chose to create a pick-up order
    elif choice == "2":
      # Printing the order number and name of the customer
      print("{}. {}".format(customer_order[0], customer_order[1]))
    # Using a for loop to run through each pizza the customer ordered
    for pizzas in pizza_order:
      # Using a for loop to run through each pizza in the pizza menu
      for key, value in pizza_menu.items():
        # Checking to see if the current pizza is the same as the one the customer ordered
        if pizzas in value:
          # Storing the pizza ID (the dicitonary key) in a variable
          id = key
          # Printing the name and price of each pizza
          print("{} - ${:.2f}".format(pizzas, pizza_menu[id][1]))
          # Ending the loop since the pizza has been found
          break
    # Printing the total cost of the order
    print("Total: ${:.2f}".format(order_cost))
    # Returning the customer_order list to be used outside of this function
    return customer_order


# Creating the menu/pizza ordering function
def menu_order():
  '''Prints out the pizza menu and allows the user to select how many and which pizza(s) they want to order.
  Returns their pizza choice(s) to be used outside of this function.
  '''
  print("\n---Pizza Menu---\n")
  # Printing each menu item and its price until we reach the end of the dictionary
  for number, pizza in pizza_menu.items():
    print("{}. {} ${:.2f}".format(number, pizza[0], pizza[1]))
  while True:
    # Asking the customer how many pizzas they want to order
    amount = input("\nHow many pizzas would you like to order?\n>>> ").strip()
    # Checking to see if a real number below the order limit was entered
    if amount.isdigit() and 0 < int(amount) <= MAX_PIZZAS:
      break
    else:
      # Printing an error message
      print("\nError: Please enter a number below our order limit of {}!".format(MAX_PIZZAS))

  # Defining important local variables
  pizzas_chosen = 0
  pizza_order = []
  cost = 0.00

  # Creating a while loop to run until the user has ordered each of their pizzas
  while pizzas_chosen < int(amount):
    # Asking which pizza they want to order
    choice = input("\nPlease select your pizza.\n>>> ").strip()
    # Checking to see if they entered a real number and valid menu item
    if choice.isdigit() and int(choice) in pizza_menu:
      pizzas_chosen += 1
      # Adding their chosen pizza into their order
      pizza_order.append(pizza_menu[int(choice)][0])
      # Adding the price of the pizza to the order's total cost
      cost += pizza_menu[int(choice)][1]
    else:
      # Printing an error message
      print("\nError: Please enter a valid pizza ID number!")

  # Returning the pizza order, cost and pizza amount to be used outside of this function
  return pizza_order, cost, int(amount)

'''Kitchen Screen UI'''
# Creating the kitchen screen function
def kitchen_screen():
  '''Displays all orders made so they can be prepared in the kitchen.'''
  # Printing the kitchen screen title
  print("\n---Kitchen Screen---")
  # Creating a for loop to run through each order that has been made
  for order in pizza_orders:
    # Printing the order number to seperate each order easily
    print("\n---Order {}---\n".format(order[0]))
    # Printing the contents of the order list neatly
    print(*order, sep=" ")


'''Management Summary UI'''
# Creating the management summary function
def management_summary():
  '''Displays the total profit and number of pizzas that have been ordered.'''
  # Printing the management summary title
  print("\n---Management Summary---\n")
  # Printing the number of pizzas ordered all day
  print("Pizzas Ordered: {}".format(pizzas_ordered))
  # Printing the total sales for the day
  print("Total Sales: ${:.2f}".format(total_profit))


'''Main routine'''
# Creating a loop to allow the user to seamlessly navigate the program
while True:
  # Running the main menu function and storing the result in a variable
  user_choice = main_menu()
  # Checking to see what the user wants to do and running the corresponding function
  if user_choice == "1":
    customer_order = pizza_order()
    pizza_orders.append(customer_order)
  elif user_choice == "2":
    kitchen_screen()
  elif user_choice == "3":
    management_summary()
  elif user_choice == "4":
    # Printing a goodbye message and ending the loop and therefore the program if the user wants to exit
    print("\nThank you for choosing Crusty Pizza!")
    break
  # Checking to see if the user entered an invalid option
  else:
    # Printing an error message
    print("\nError: Invalid option!")
