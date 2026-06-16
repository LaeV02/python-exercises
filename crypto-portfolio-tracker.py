# Initial database representing the user's crypto holdings
portfolio = {
    "bitcoin": 3.50,
    "ethereum": 5.00,
    "tether": 300.00
    }

while True:
    print("\n--------------------------------------------------------------------------")
    print("TO VIEW YOUR PORTFOLIO PRESS 1")
    print("TO ADD OR REMOVE COINS FROM YOUR PORTFOLIO PRESS 2")
    print("TO EXIT PRESS 3")

    # Input conversion to integer for menu selection
    choice = int(input("\nWhat would you like to do? "))

    # Input validation for the main menu
    if choice != 1 and choice != 2 and choice != 3:
      print("\n***ERROR*** Invalid choice, please try again.")
      continue


    # OPTION 1: View current balances
    if choice == 1:
      print("\nYour Current Portfolio:\n")
      for crypto, quantity in portfolio.items():
        print(f"\t{crypto.upper()}: \t{quantity}")
  
    # OPTION 2: Add or Remove coins
    elif choice == 2:
      while True:
        action_choice = str(input("\nWould you like to add or remove coins?(add/remove): ")).lower()
        if action_choice!="add" and action_choice!="remove":
          print("\n***ERROR*** Invalid choice, please try again.")
        else:
          break
    
      # Logic for adding or updating a coin in the portfolio
      if action_choice == "add":
          crypto_name = str(input("Enter the name of the cryptocurrency you want to add: ")).lower()
          quantity = float(input("Enter the quantity of the cryptocurrency you want to add: "))
          if crypto_name in portfolio:
            portfolio[crypto_name] += quantity
          else:
            portfolio[crypto_name] = quantity
    

      elif action_choice == "remove":
        crypto_name = str(input("Enter the name of the cryptocurrency you want to remove: ")).lower()
        if crypto_name not in portfolio:
          print("***ERROR*** The cryptocurrency is not in your portfolio.")
        else:
          quantity = float(input("Enter the quantity of the cryptocurrency you want to remove: "))
          if quantity > portfolio[crypto_name]:
            print("\n***ERROR*** Insufficient balance.")
          elif quantity == portfolio[crypto_name]:
            del portfolio[crypto_name] # Remove the coin entirely if balance hits zero
          elif quantity > 0:
            portfolio[crypto_name] -= quantity
          else:
            portfolio[crypto_name] += quantity

    # OPTION 3: Exit the program
    elif choice == 3:
      print("\nGoodbye!")
      break





