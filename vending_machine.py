# THE SINGLE ELEMENT CLASS
class Snack:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

# THE CONTROLLER CLASS
class vending_machine:
  def __init__(self):
    self.products = []         # List to store Snack objects 
    self.total_money = 0.0     # Current credit inserted by the user

  # Adds money to the machine's total balance
  def insert_money(self, money):
    self.total_money += money

  # Displays all available products and their status
  def display_products(self):
    if not self.products:
            print("No products available.")
            return

    print("\nAvailable Products:")
    for index, snack in enumerate(self.products): 
        # Check if the product is in stock   
        if snack.quantity > 0:
            print(f"\t{index + 1}) {snack.name} - Price: ${snack.price:.2f} - Quantity: {snack.quantity}")
        else:
            print(f"\t{index + 1}) {snack.name} - [SOLD OUT]")
      
  # Handles the product purchasing logic
  def buy_product(self, user_index):
    task_index = user_index - 1       # Convert to Python's 0-based indexing
    # Convert to Python's 0-based indexing
    if task_index < 0 or task_index >= len(self.products):
      print("***ERROR*** Invalid product index")
      return
    
    # Get the specific snack object from the list
    snack = self.products[task_index]

    # 2. Check stock availability
    if snack.quantity == 0:
      print("Out of stock")
    
    # 3. Check if the user has enough credit
    elif snack.price > self.total_money:
      print("Insufficient funds")

    # 4. Process the successful purchase
    else:
      snack.quantity -= 1
      self.total_money -= snack.price
      print(f"You have bought {snack.name} for ${snack.price:.2f}")
    

# Initialize the vending machine object
machine = vending_machine()

# Populate the inventory with initial products
machine.products.append(Snack("Chips", 1.50, 5))
machine.products.append(Snack("Chocolate Bar", 2.00, 3))
machine.products.append(Snack("Soda", 1.20, 0))
machine.products.append(Snack("Cookies", 2.20, 2))
machine.products.append(Snack("M&M's", 1.80, 6 ))
#...

# THE USER INTERFACE (MAIN LOOP)
while True:
  print("\n-------------------------------------------------------------")
  print("Welcome to the vending machine!")
  machine.display_products()
  print(f"Total Money: ${machine.total_money:.2f}")
  print("-------------------------------------------------------------")
  print("What do you want to do?")
  print("1.Insert Money (PRESS 1)")
  print("2.Buy Product (PRESS 2)")
  print("3.Refund and Exit (PRESS 3)")

  # Get user menu choice
  choice = int(input("Enter your choice: "))

  # Validate main menu choice
  if choice not in [1,2,3]:
    print("***ERROR*** Invalid choice")
    continue

  # OPTION 1: INSERT MONEY
  elif choice == 1:
    print("Type of money: $0.10\t$0.20\t$0.50\t$1.00\t$2.00\t$5.00\t$10.00\t$20.00")
    money = float(input("Enter the amount of money to insert: "))

    # Check if the entered coin/bill is valid
    if money not in [0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00]:
      print("***ERROR*** Invalid money")
      continue

    machine.insert_money(money)

  # OPTION 2: BUY PRODUCT
  elif choice == 2:
    product_index = int(input("Enter the index of the product you want to buy? "))
    machine.buy_product(product_index)

  # OPTION 3: REFUND AND EXIT
  elif choice == 3:
    print(f"Here's your refund: ${machine.total_money:.2f}")
    print("Thank you for using the vending machine! Goodbye!!")
    break