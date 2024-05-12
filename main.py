'''12/04/24 - Taylah Wright  (-.'3'.)-
Assessment for L2 CompSci.'''

#Defining important variables/constants/lists
delivery_fee = 2.50
order_cost = 0.00
total_profit = 0.00
order_number = 0
pizzas_ordered = 0
pizza_orders = [[]]
pizza_menu = {
  1 : ["Beef & Onion", 8.50],
  2 : ["Extra Cheese", 8.50],
  3 : ["Garlic Cheese", 8.50],
  4 : ["Hawaiian", 8.50],
  5 : ["Italian", 8.50],
  6 : ["Pepperoni", 8.50],
  7 : ["Vegeterian", 8.50],
  8 : ["Gourmet Vegeterian", 13.50],
  9 : ["Margherita", 13.50],
  10 : ["Meatlovers", 13.50],
  11 : ["Pepperoni Supreme", 13.50],
  12 : ["Spicy Supreme", 13.50],
}

#Creating the price calculator function
def price_calculator(price):
  #Adding the price of whatever is added to the order to the order's total cost
  cost = order_cost + price
  #Making the order cost a global variable to be used outside of this function
  return cost

'''Main Menu'''
#Creating the main menu function
def main_menu():
  #Taking input from the user as to what they want to do
  choice = input("\n---Main Menu---\n\n 1. Create Order\n 2. Kitchen Screen\n 3. Management Summary\n 4. Exit\n\n>>> ").strip()
  #Making choice a global variable to be used outside of this function
  return choice

'''Ordering'''
#Creating the main order function
def pizza_order():
  #Making sure the program knows the order cost variable is global and not local (it is used outside of the function, and not just inside.)
  global order_cost
  #Making sure the customer order variable is bound
  customer_order = []
  #Creating a loop to allow the user to create multiple pizza order
  while True:
    #Taking input from the user as to what they want to do
    choice = input("\n---Order---\n\n 1. Delivery\n 2. Pick-up\n 3. Exit\n\n>>> ").strip()
 
    #Checking to see if the user wants to create a delivery order
    if choice == "1":
      print("\nDelivery Selected")
      #Running the order function
      customer_order = user_order()
      #Taking the address for the pizza order and storing it in a variable
      address = input("\nWhat is the address for this order?\n>>> ").strip().title()
      #Adding the delivery fee to the order cost
      order_cost = price_calculator(delivery_fee)
      #Adding the address to the current order
      customer_order.append(address)

    #Checking to see if the user wants to create a pick-up order
    elif choice == "2":
      print("\nPick-up Selected")
      #Running the order function
      customer_order = user_order()

    #Checking to see if the user wants to exit the order UI
    elif choice == "3":
      print("\nReturning to the Main Menu")
      #Breaking the order UI loop
      break
      
    #Checking to see if the user entered an invalid option
    else:
      #Printing an error message
      print("\nInvalid input")

    pizza_order, cost, pizza_amount = menu_order()
    global pizzas_ordered
    global total_profit
    pizzas_ordered = pizzas_ordered + pizza_amount
    total_profit = total_profit + cost
    order_cost = price_calculator(cost)
    customer_order.append(pizza_order)
    print("\nOrder Confirmed!")
    if choice == "1":
      print("{}. {} - {}\n{}".format(customer_order[0], customer_order[1], customer_order[2], customer_order[3]))
    elif choice == "2":
      print("{}. {} - {}".format(customer_order[0], customer_order[1], customer_order[2]))
    for pizzas in pizza_order:
      print(pizzas)
    print("Total: ${:.2f}".format(order_cost))
    return customer_order

#Creating the user order function
def user_order():
  #Making sure the program knows the order number variable is global and not local (it is used outside of the function, and not just inside.)
  global order_number
  #Creating a new list to store the current order in
  customer_order = []
  #Increasing the order number by 1 so each order number is unique and ordered
  order_number += 1
  #Taking the name for the pizza order and storing it in a variable
  name = input("\nWho is this order for?\n>>> ").strip().title()
  #Taking the phone number for the pizza order and storing it in a variable
  phone_number = input("\nWhat is the customer's phone number?\n>>> ").strip()
  #Adding the order number, name and phone number to the customer's current order list
  customer_order.append([order_number, name, phone_number])
  #Making customer_order a global list to be used outside of this function
  return customer_order

#Creating the menu/pizza ordering function
def menu_order():
  print("\n  -Pizza Menu-  \n")
  #Printing each menu item and its price until we reach the end of the dictionary
  for number, pizza in pizza_menu.items():
    print("{}. {}{}".format(number, pizza[0], pizza[1]))
  while True:
    #Asking the customer how many pizzas they want to order
    amount = input("\nHow many pizzas would you like to order?\n>>> ").strip()
    #Checking to see if a real number was entered
    if amount.isdigit:
      #Making the amount entered an integer
      pizza_amount = int(amount)
      #Checking to see if they ordered up to the order limit
      if pizza_amount > 0 <= 5:
        #Breaking the loop
        break
      else:
        #Printing an apology message
        print("\nSorry, we have an order limit of 5 pizzas.")
    else:
      #Printing an error message
      print("\nError: Please enter a number!")

  #Defining important local variables
  number_of_pizzas = 0
  pizza_order = []
  cost = 0.00

  while True:
    #Checking to see if they've ordered their selected amount of pizzas yet
    if number_of_pizzas < pizza_amount:
      #If they haven't, asking them for their order and storing it in a variable
      choice = input("\nPlease select your pizza.\n>>> ").strip()
      #Checking to see if they entered a real number
      if choice.isdigit:
        #Making the choice an integer
        choice_int = int(choice)
        #Checking to see if the entered number is a valid menu item
        if choice_int in pizza_menu:
          #Adding their chosen pizza into their order
          pizza_order.append(pizza_menu[choice_int][0])
          #Adding the price of the pizza to the order's total cost
          cost = cost + pizza_menu[choice_int][1]
          #Adding one to the number of pizzas ordered
          number_of_pizzas += 1
        else:
          #Printing an error message
          print("\nError: Invalid option!")
      else:
        #Printing an error message
        print("\nError: Please enter a number!")
    elif number_of_pizzas == pizza_amount:
      break
  return pizza_order, cost, pizza_amount

'''Kitchen Screen UI'''
#Creating the kitchen screen function
def kitchen_screen():
  print("\n  -Kitchen Screen-  \n")
  for i in range(len(pizza_orders)):
    print(pizza_orders[i][0:-2], sep = "")

'''Management Summary UI'''
#Creating the management summary function
def management_summary():
  print("\n  -Management Summary-  \n")
  print("Pizzas Sold: {}".format(pizzas_ordered))
  print("Total Sales: {:.2f}".format(total_profit))

'''Main routine'''
#Creating a loop to allow the user to seamlessly navigate the program
while True:
  #Running the main menu function and storing the result in a variable
  user_choice = main_menu()
  #Checking to see what the user wants to do and running the corresponding function
  if user_choice == "1":
    pizza_orders.append([pizza_order()])
  elif user_choice == "2":
    kitchen_screen()
  elif user_choice == "3":
    management_summary()
  elif user_choice == "4":
    #Printing a goodbye message and ending the loop and therefore the program if the user wants to exit
    print("\nThank you for choosing Crusty Pizza!")
    break
  #Checking to see if the user entered an invalid option
  else:
    #Printing an error message
   print("\nError: Invalid input")