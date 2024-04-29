'''12/04/24 - Taylah Wright  (-.'3'.)-
Assessment for L2 CompSci.'''

#Defining important variables/constants/lists
delivery_fee = 2.50
order_cost = 0.00
order_number = 0
pizza_orders = [[]]
pizza_menu = {
  "Beef & Onion" : 8.50,
  "Extra Cheese" : 8.50,
  "Garlic Cheese" : 8.50,
  "Hawaiian" : 8.50,
  "Pepperoni" : 8.50,
  "Vegeterian" : 8.50,
  "" : 8.50,
  "Gourmet Vegeterian" : 13.50,
  "Margherita" : 13.50,
  "Meatlovers" : 13.50,
  "Pepperoni Supreme" : 13.50,
  "" : 13.50,
}

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
      #Adding the delivery fee to the order cost
      order_cost = price_calculator(delivery_fee)
      print("a")
      #Making the order cost a global variable to be used outside of this function
      return order_cost

    #Checking to see if the user wants to create a pick-up order
    elif choice == "2":
      print("e")

    #Checking to see if the user wants to exit the order UI
    elif choice == "3":
      #Breaking the order UI loop
      break

    #Checking to see if the user entered an invalid option
    else:
      #Printing an error message
      print("Invalid input")

'''Kitchen Screen UI'''
#Creating the kitchen screen function
def kitchen_screen():
  print("a")

'''Management Summary UI'''
#Creating the management summary function
def management_summary():
  print("a")

#Price calculator
def price_calculator(price):
  #Adding the price of whatever is added to the order to the order's total cost
  cost = order_cost + price
  #Making the order cost a global variable to be used outside of this function
  return cost

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
    print("Bye")
    break
  #Checking to see if the user entered an invalid option
  else:
    #Printing an error message
   print("Invalid input")