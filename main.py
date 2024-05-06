'''12/04/24 - Taylah Wright  (-.'3'.)-
Assessment for L2 CompSci.'''

#Defining important variables/constants/lists
delivery_fee = 2.50
order_cost = 0.00
order_number = 0
pizza_orders = []
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

#Price calculator
def price_calculator(price):
  #Adding the price of whatever is added to the order to the order's total cost
  cost = order_cost + price
  #Making the order cost a global variable to be used outside of this function
  return cost

#
def menu_order():
  print("\n  -Pizza Menu-  \n")
  for number, pizza in pizza_menu.items():
    print("{}. {}{}".format(number, pizza[0], pizza[1]))
  while True:
    amount = input("\nHow many pizzas would you like to order?\n>>> ").strip()
    if amount.isdigit:
      pizza_amount = int(amount)
      if pizza_amount > 0 <= 5:
        break
      else:
        print("\nSorry, we have an order limit of 5 pizzas.")
    else:
      print("\nError: Please enter a number!")
  number_of_pizzas = 0
  pizza_order = []
  cost = 0.00
  while True:
    if number_of_pizzas < pizza_amount:
      choice = input("\nPlease select your pizza.\n>>> ").strip()
      if choice in pizza_menu:
        pizza_order.append(choice[0])
        cost = cost + choice[1]
        number_of_pizzas += 1
      else:
        print("\nError: Invalid option!")
    elif number_of_pizzas == pizza_amount:
      break
  return pizza_order, cost
  
'''Main Menu UI'''
#Creating the main menu function
def main_menu():
  #Taking input from the user as to what they want to do
  choice = input("\n---Main Menu---\n\n 1. Create Order\n 2. Kitchen Screen\n 3. Management Summary\n 4. Exit\n\n>>> ").strip()
  #Making choice a global variable to be used outside of this function
  return choice

'''Order UI'''
#Creating the order function
def pizza_order():
  #Creating a loop to allow the user to create multiple pizza order
  while True:
    #Taking input from the user as to what they want to do
    choice = input("\n---Order---\n\n 1. Delivery\n 2. Pick-up\n 3. Exit\n\n>>> ").strip()
 
    #Checking to see if the user wants to create a delivery order
    if choice == "1":
      print("\nDelivery Selected")
      #Running the delivery order function
      #delivery_order()

    #Checking to see if the user wants to create a pick-up order
    elif choice == "2":
      print("\nPick-up Selected")
      #Running the pick-up order function
      #pick_up_order()

    #Checking to see if the user wants to exit the order UI
    elif choice == "3":
      print("\nReturning to the Main Menu")
      #Breaking the order UI loop
      break
      
    #Checking to see if the user entered an invalid option
    else:
      #Printing an error message
      print("\nInvalid input")

def user_order():
  global order_number
  customer_order = []
  order_number += 1
  customer_order.append(order_number)
  
'''#Creating the pick-up order function
def pick_up_order():
  #Making sure the program knows the order number variable is global and not local (it is used outside of the function, and not just inside.)
  global order_number
  #Increasing the order number by 1 so each order number is unique and ordered
  order_number +=1
  #Adding the order number into a new list containing the order info
  pizza_orders.append([order_number])
  #Taking the name for the pizza order and storing it in a variable
  name = input("\nWho is this order for?").strip().title()
  #Adding the name the order is being made under into the new list
  pizza_orders[-1].append(name)
  #Running the menu order function
  menu_order()

#Creating the delivery order function
def delivery_order():
  #Making sure the program knows the order number variable is global and not local (it is used outside of the function, and not just inside.)
  global order_number
  #Increasing the order number by 1 so each order number is unique and ordered
  order_number +=1
  #Adding the order number into the list containing the order info
  pizza_orders.append([order_number])
  #Adding the delivery fee to the order cost
  order_cost = price_calculator(delivery_fee)
  
  #Taking the name for the pizza order and storing it in a variable
  name = input("\nWho is this order for?\n>>> ").strip().title()
  #Adding the name the order is being made under into the new list
  pizza_orders[-1].append(name)
  #Taking the address for the pizza order and storing it in a variable
  address = input("\nWhat is the address for this order?\n>>> ").strip().title()
  #Adding the address for the order into the new list
  pizza_orders[-1].append(address)
  #Taking the phone number for the pizza order and storing it in a variable
  phone_number = input("\nWhat is the customer's phone number?\n>>> ").strip()
  #Adding the phone number for the order into the new list
  pizza_orders[-1].append(phone_number)

  #Running the menu order function
  menu_order()
  #Printing an order confirmation message
  print("\nYour delivery order has been confirmed!")
  print(pizza_orders[order_number-1])
  #Making the order cost a global variable to be used outside of this function
  return order_cost'''
    
'''Kitchen Screen UI'''
#Creating the kitchen screen function
def kitchen_screen():
  print("a")

'''Management Summary UI'''
#Creating the management summary function
def management_summary():
  print("a")

'''Main routine'''
#Creating a loop to allow the user to seamlessly navigate the program
while True:
  #Running the main menu function and storing the result in a variable
  user_choice = main_menu()
  #Checking to see what the user wants to do and running the corresponding function
  if user_choice == "1":
    pizza_order()
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
   print("\nInvalid input")