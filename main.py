'''12/04/24 - Taylah Wright  (-.'3'.)-
Assessment for L2 CompSci.'''

#Defining important variables/lists
delivery_fee = 2.50
pizza_menu = []
pizza_orders = [[]]
order_number = 0

#Main menu ui
def mainmenu():
  choice = input("\n---Main Menu---\n\n 1. Create Order\n 2. Kitchen Screen\n 3. Management Summary\n 4. Exit\n\n>>> ").strip()
  return choice

#Order ui
def pizza_order():
  while True:
    choice = input("\n---Order---\n\n 1. Delivery\n 2. Pick-up\n 3. Exit\n\n>>> ").strip()
    if choice == "1":
      print("a")
    elif choice == "2":
      print("e")
    elif choice == "3":
      break
    else:
      print("Invalid input")
#Kitchen screen ui
def kitchen_screen():
  print("a")

#Management summary ui
def management_summary():
  print("a")

'''Main routine'''
while True:
  user_choice = mainmenu()
  if user_choice == "1":
    pizza_order()
  elif user_choice == "2":
    kitchen_screen()
  elif user_choice == "3":
    management_summary()
  elif user_choice == "4":
    print("Bye")
    break
  else:
   print("Invalid input")