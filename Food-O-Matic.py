'''
Created on 3 Nov 2021
@author: FHentsch-Cowles24
Description:
        This program keeps a global balance($) and inventory for the user. They can select which item-O-Matic machine to use.
    Each machine costs a certain amount of money for each item bought from it. Machines output product items which are made
    up of 3 random values from 3 different lists. Each value has a cost value linked to it in a parallel list. The total cost
    of each item is added to equal the product item's total value.
        The global cart variable stores which items users choose to add to cart. After the machine spits out the product item,
    they can either add the item to cart or compost it. The compost bin is also a global variable which can store up to 10
    unused items. Once it reaches 10 the bin is reset and $50 is added to the player's balance.
    The player can sell or checkout the items in their carts (one cart for each machine). If sold, the items disappear and their
    total cost value is added to the user's balance. If checked out, the items are moved to the player's inventory list and the cart is reset.
        The bal and cart can be accessed and viewed from the menu. Quit will terminate the program.
Log:
    11/09/2021 Version 1.1 - Added upgrade option. Users can upgrade profit multiplier or O-Matic discounter
    11/09/2021 Version 1.2 - Added sound effects to sell and o-matic item selection as well as Pet-O-Matic
    11/16/2021 Version 1.3 - Added cancellation option when using O-Matic machiens
Bugs:
    
Initiatives:
    - Turned into a game with currency
    - Sound effects
    - Can sell, donate, or add items to inventory
    - Multiple O-Matic machines
    - Performance upgrades
    - Specific costs for each item combination
    - Game goal is to make profit
    - Quit program option
    - Loop to main menu
    - Global variables for balance, cart, inventory, upgrades, etc. (Things that don't reset within the game menu loop)
    - Cannot buy upgrades user can't afford
    - Game over if they spend too much on an O-Matic machine
Last edited on 11/16/2021
'''
import random
import winsound
from playsound import playsound

#Global Variables
balance = 100                                                                           #Stores user balance
inventory = []                                                                          #Stores user's purchases
food_cart = [""]                                                                        #Stores meals in cart
food_total = 0                                                                          #Stores total price of food cart
compost_bin = 0                                                                         #Stores meals in compost
pet_cart = [""]                                                                         #Stores pets in cart
pet_total = 0                                                                           #Stores total price of pet cart
pound = 0                                                                               #Stores pets in pound
sauce = 0.0                                                                             #Stores sauce upgrade multiplier value
discount = 0                                                                            #Stores discount upgrade total
sauce_cost = 125                                                                        #Sauce upgrade cost
discount_cost = 125                                                                     #Discount upgrade cost

def main():
    
    global balance
    global inventory
    global food_cart
    global food_total
    global compost_bin
    global pet_cart
    global pet_total
    global pound
    global sauce
    global discount
    global sauce_cost
    global discount_cost
    
    menu_options = ["food","pet","cart","bal","checkout","sell","upgrade","quit"]       #Defines accepted inputs for user menu
    menu = "Undecided"                                                                  #Sets menu choice to Undecided
    
    #Main Menu Interface - Loop that only breaks when an accepted input is entered
    while menu != menu_options:
        menu = input("Menu\n"\
                     "'Help' - How to play\n"
                     "'Food' - Food-O-Matic\n"\
                     "'Pet' - Pet-O-Matic\n"\
                     "'Cart' - View carts\n"\
                     "'Bal' - Check balance and inventory\n"\
                     "'Checkout' - Checkout cart items to inventory\n"\
                     "'Sell' - Sell a cart\n"\
                     "'Upgrade' - Upgrades available!\n"
                     "'Quit' - Quit program\n")
        menu = menu.lower()
        if menu == "help":                                                              #Explains the rules
            print("O-Matic Mania\n"\
                  "Objective: Make profit\n"\
                  "How:\n"\
                  "1) Roll the O-Matic machines\n"\
                  "2) Add the item(s) to your cart to sell later, or compost/pound\n"\
                  "    What do compost and pound do? When filled they return 90% expenses!\n"\
                  "3) Go to sell and sell your cart, hopefully you made a profit\n"\
                  "4) Check your balance\n"\
                  "Repeat the process until you feel ready to upgrade! Then repeat.\n"\
                  "WARNING: Spending more than you have on O-Matics means game over.\n"\
                  "Usage: Just type one of the words in the prompt. Not case-sensitive\n")
        elif menu == "food":                                                            #If food is chosen, loop breaks
            break
        elif menu == "pet":
            break                                                                       #If pet is chosen, loop breaks
        #If cart is chosen, prints the cart contents and price
        elif menu == "cart":
            #Print the food cart
            print("Food-O-Matic Cart:")
            for i in range(0, len(food_cart), 9999):
                print(*food_cart[i:i+9999], sep="\n    - ")                             #Lists each cart item on single row, with hyphen points
            print("Cart Total: $" + str(food_total) + "\n")
            #Print the pet cart
            print("\nPet-O-Matic Cart:")
            for i in range(0, len(pet_cart), 9999):
                print(*pet_cart[i:i+9999], sep="\n    - ")                              #Lists each cart item on single row, with hyphen points
            print("Cart Total: $" + str(pet_total) + "\n")
            break
        #If bal is chosen, prints the user's balance and inventory contents
        elif menu == "bal":
            print("Your balance is: $" + str(balance))
            print("Your inventory consists of:")
            for i in range(0, len(inventory), 9999):
                print(*inventory[i:i+9999], sep="\n    - ")                             #Lists each cart item on single row, with hyphen points
        #If buy is chosen, asks which machine's cart they want to checkout
        elif menu == "checkout":
            cart_selections = ["food","pet","cancel"]                                   #Defines accepted inputs for cart selection
            cart_selection = "Undecided"
            #Cart Selection Interface
            while cart_selection != cart_selections:
                cart_selection = input("Which cart would you like to checkout?\n"\
                                       "'Food' - Checkout the Food-O-Matic cart\n"\
                                       "'Pet' - Checkout the Pet-O-Matic cart\n"\
                                       "'Cancel' - Go back to menu\n")
                cart_selection = cart_selection.lower()
                if cart_selection == "food":
                    inventory.extend(food_cart)                                         #Adds cart contents to inventory
                    print(inventory)
                    food_cart = [""]                                                    #Resets cart contents
                    food_total = 0                                                      #Resets cart price
                    print("Food items moved to inventory")
                    break
                if cart_selection == "pet":
                    inventory.extend(pet_cart)                                          #Adds cart contents to inventory
                    print(inventory)
                    pet_cart = [""]                                                     #Resets cart contents
                    pet_total = 0                                                       #Resets cart price
                    print("Pets moved to inventory")
                    break
                elif cart_selection == "cancel":                                        #Option to cancel and return to menu
                    main()
                else:
                    print("Please select a cart or cancel.")            #Prompts user to enter an accepted input
        #If sell is chosen, asks which machine's cart they want to sell
        elif menu == "sell":
            cart_selections = ["food","pet","cancel"]                                   #Defines accepted inputs for cart selection
            cart_selection = "Undecided"
            #Cart Selection Interface
            while cart_selection != cart_selections:
                cart_selection = input("Which cart would you like to sell?\n"\
                                       "'Food' - Sell the Food-O-Matic cart for $"\
                                       + str(food_total + food_total*sauce) + "\n"\
                                       "'Pet' - Sell the Pet-O-Matic cart for $"\
                                       + str(pet_total + pet_total*sauce) + "\n"\
                                       "'Cancel' - Go back to menu\n")
                cart_selection = cart_selection.lower()
                if cart_selection == "food":
                    winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\mixkit-coins-handling-1939.wav",\
                                       winsound.SND_ASYNC)                              #Plays chaching noise
                    balance = balance + (food_total + food_total*sauce)                 #Adds cart price to balance
                    food_cart = [""]                                                    #Resets cart contents
                    food_total = 0                                                      #Resets cart price
                    print("Food cart sold")
                    break
                elif cart_selection == "pet":
                    winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\mixkit-coins-handling-1939.wav",\
                                       winsound.SND_ASYNC)                              #Plays chaching noise
                    balance = balance + (pet_total + pet_total*sauce)                   #Adds cart price to balance
                    pet_cart = [""]                                                     #Resets cart contents
                    pet_total = 0                                                       #Resets cart price
                    print("Pet cart sold")
                    break
                elif cart_selection == "cancel":                                        #Option to cancel and return to menu
                    main()
                else:
                    print("Please select a cart or cancel.")            #Prompts user to enter an accepted input
        #If upgrades is chosen, asks which upgrade user would like to buy
        elif menu == "upgrade":
            upgrade_list = ["sauce","discount"]                                         #List of valid upgrades
            upgrade = "Undecided"
            #Upgrade Selection Interface
            while upgrade != upgrade_list:
                upgrade = input("Select an upgrade:\n"\
                                "'Sauce' - Awesome sauce multiplies earnings by +10%. (PRICE: $" + str(sauce_cost) + ")\n"\
                                "'Discount' - Dirty discount reduces O-Matic prices by $0.50. (PRICE: $" + str(discount_cost) + ")\n"\
                                "'Cancel' - Go back to menu\n"\
                                "\n"\
                                "Current Awesome Sauce Multiplier: " + str(sauce) + "\n"\
                                "Current Dirty Discount Reduction: " + str(discount) + "\n")
                upgrade = upgrade.lower()
                if upgrade == "sauce" and balance >= sauce_cost:                        #Upgrading sauce option, if they can afford it
                    balance = balance - sauce_cost
                    sauce = sauce + 0.1
                    sauce_cost = sauce_cost + sauce_cost*.5                             #Increasing future upgrade price
                    print("Awesome Sauce upgraded to +" + str(sauce) + "x multiplier for all earnings.\n"\
                          "Your balance is now " + str(balance))
                    break
                elif upgrade == "discount" and balance >= discount_cost:                #Upgrading discount option, if they can afford it
                    balance = balance - discount_cost
                    discount = discount + 0.50
                    discount_cost = discount_cost + discount_cost*.5                    #Increasing future upgrade price
                    print("Dirty Discount upgraded to $" + str(sauce) + " discount on O-Matic machines.\n"\
                          "Your balance is now " + str(balance))
                    break
                elif upgrade == "sauce" and balance < sauce_cost:                       #If sauce selected but can't afford
                    print("You cannot afford this upgrade.")
                    main()
                elif upgrade == "discount" and balance < discount_cost:                 #If discount selected but can't afford
                    print("You cannot afford this upgrade.")
                    main()
                elif upgrade == "cancel":                                               #Cancel back to menu
                    main()
                else:                                                                   #If unaccepted input, re-prompt
                    print("Please select an upgrade or cancel.")
        #Quit option, will terminate program
        elif menu =="quit":
            print("Quitting program.")
            quit()
        else:
            print("Please enter an option from the main menu.")         #If menu input is invalid, prompts user to re-input
    
    #The Food-O-Matic Machine
    while menu == "food":
        ItemsA = ["local","roasted","grilled","garlic mashed",\
                  "oven dried","spiced","stewed","assorted",\
                  "iced","sliced","braised","free-range","baby",\
                  "teriyaki glazed","steamed"]                                          #Sets 15 possible ItemA values in list
        
        ItemsB = ["cauliflower","tilapia fillet", "pork loin",\
                  "green beans","basmati rice","rainbow carrots",\
                  "fingerling potatoes","three color squash","potatoes",\
                  "eggplant","drumstick","short rib",\
                  "duck breast","eye round of beef","baguette"]                         #Sets 15 possible ItemB values in list
        CostsB = [6, 8, 8, 5, 5, 5, 6, 4, 4, 5, 4, 5, 10, 9, 5]                         #Gives parallel cost values to the 15 ItemB's
        
        ItemsC = ["with fennel","gratin","bengali style","with peas",\
                  "pizza","with balsamico","with garlic and olive oil",\
                  "with pigeon peas","with minted yogurt","soup","chutney",\
                  "salad","with tropical fruit salsa","over sticky rice",\
                  "au jus"]                                                             #Sets 15 possible ItemC values in list

        CostsC = [3, 4, 5, 4, 6, 4, 5, 3, 5, 6, 5, 6, 4, 5, 3]                          #Gives parallel cost values to the 15 ItemC's
        
        items = 0                                                                       #Determines number of product items later
        valid = "No"                                                                    #Forces loop to run which gets user input
        desired_items = 0
        
        #Food-O-Matic/Meal Quantity Selection Interface
        while valid == "No":
            try:
                desired_items = int(input("How many meals would you like?\n"\
                                          "$" + str(10-discount) + " per meal, 14 meals max. '0' to cancel.\n"))
                if desired_items > 0 and desired_items <= 14:                           #If input is within range of acceptable quantities
                    winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\SlotMachine.wav",\
                                       winsound.SND_ASYNC)                              #Plays slot machine noise
                    meal_expense = (10 * desired_items) - discount                      #Defines expense according to amount desired( $10x)
                    balance = balance - meal_expense                                    #Deducts expense from player's balance
                    if balance < 0:                                                     #If player over spent, game over
                        print("Your balance dropped below $0. You are bankrupt. GAME OVER")
                        winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\mixkit-arcade-video-game-explosion-2810.wav", winsound.SND_FILENAME)
                        quit()
                    valid = "Yes"                                                       #Ends the forced loop
                    print("$" + str(meal_expense) + " was deducted from your balance.\n"\
                          "Your balance is now: $" + str(balance))
                    break
                elif desired_items == 0:                                                #Can press 0 to return to menu
                    main()
                else:                                                                   #If unacceptable quantity entered, re-prompt
                    print("Must be an integer between 1-15.")
            except ValueError:                                                          #If input is not an integer, re-prompt
                print("Must be an integer between 1-15.")

        #Randomly selects Items A,B,C from their lists. Also pulls the parallel cost values of B and C
        while items != desired_items:                                                   #Loop will repeat until it has reached desired item count
            ItemA = random.choice(ItemsA)
            ItemB = random.choice(ItemsB)
            ItemC = random.choice(ItemsC)
            IndexB = int(ItemsB.index(ItemB))                                           #Grabs index number of ItemB
            IndexC = int(ItemsC.index(ItemC))                                           #Grabs index number of ItemC
            CostB = CostsB[IndexB]                                                      #Finds ItemB's cost with its index
            CostC = CostsC[IndexC]                                                      #Finds ItemC's cost with its index
            
            #Removes Items/Costs A,B,C from their lists to prevent repeats
            ItemsA.remove(ItemA)
            ItemsB.remove(ItemB)
            ItemsC.remove(ItemC)
            CostsB.remove(CostB)
            CostsC.remove(CostC)
            
            ItemA = ItemA.capitalize()                                                  #Capitalise ItemA for looks
            
            ItemProduct = ItemA + " " + ItemB + " " + ItemC                             #Merges Items A,B,C into product item
            
            print(ItemProduct + "\nItem Cost: $" + str(CostB + CostC))                  #Presents product item to user
            
            cart_options = ["add","com"]                                                #Acceptable cart option inputs
            cart_option = "Undecided"
            #Cart Option Interface
            while (cart_option != cart_options) and (items < desired_items):            #Loop repeats until acceptable input given and if there are more items to complete
                cart_option = input("'Add' to cart or 'Com' to compost\n")
                cart_option = cart_option.lower()
                #If chosen, adds the item to cart
                if cart_option == "add":
                    food_cart.append(ItemProduct)                                       #Adds product item to cart list
                    food_total = food_total + CostB + CostC                             #Adds product cost to cart price
                    print(ItemProduct + " added to cart.")
                    break
                #If chosen, adds item to compost bin
                elif cart_option == "com":
                    compost_bin = compost_bin + 1                                       #Increases compost count by 1
                    print("Compost Bin: " + str(compost_bin) + "/10")
                    #If compost count reaches 10 (fills the bin)
                    if compost_bin == 10:
                        print("You filled the compost bin! $90 added to balance.")
                        compost_bin = 0                                                 #Resets compost count
                        balance = balance + 90                                          #Adds $90 to player balance for filling the bin
                    break
                else:                                                                   #If unacceptable input, re-prompt user
                    print("Please enter 'Add' or 'Com'.")
            
            items = items + 1                                                           #Increases items count by 1, 1 closer to reaching desired
            #If items count reaches desired amount, returns to main menu
            if items == desired_items:
                main()
    #The Pet-O-Matic Machine
    while menu == "pet":
        ItemsA = ["one-eyed","two-eyed","three-eyed","handicapped",\
                  "odorous","mischievous","beautiful","dangerous",\
                  "wild","tame","talented","lazy","scaly",\
                  "blind","deaf"]                                                       #Sets 15 possible ItemA values in list
        
        ItemsB = ["grackle","tardigrade", "among us creature",\
                  "stallion","charmander","frog",\
                  "shark","cobra","demon",\
                  "blobfish","mammoth","human",\
                  "water jug","parrot","crab"]                                          #Sets 15 possible ItemB values in list
        CostsB = [10, 15, 15, 20, 20, 23, 25, 25, 30, 30, 35, 36, 40, 45, 50]           #Gives parallel cost values to the 15 ItemB's
        
        ItemsC = ["with problems","without emotion","under stress","with moral values",\
                  "and a half","without logic","with trauma",\
                  "from Wakanda","made in China","that sucks","that eats people",\
                  "that likes the cold","that hates freedom","that killed its family",\
                  "that knows how to write"]                                            #Sets 15 possible ItemC values in list

        CostsC = [12, 14, 15, 14, 20, 23, 25, 25, 30, 30, 35, 36, 44, 45, 53]           #Gives parallel cost values to the 15 ItemC's
        
        items = 0                                                                       #Determines number of product items later
        valid = "No"                                                                    #Forces loop to run which gets user input
        desired_items = 0
        
        #Pet-O-Matic/Meal Quantity Selection Interface
        while valid == "No":
            try:
                desired_items = int(input("How many pets would you like?\n"\
                                          "$" + str(50-discount) + " per pet, 14 pets max. '0' to cancel.\n"))
                if desired_items > 0 and desired_items <= 14:                           #If input is within range of acceptable quantities
                    winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\SlotMachine.wav",\
                                       winsound.SND_ASYNC)                              #Plays slot machine noise
                    pet_expense = (50 * desired_items) - discount                       #Defines expense according to amount desired( $50x)
                    balance = balance - pet_expense   
                    if balance < 0:                                                     #If player over spent, game over
                        print("Your balance dropped below $0. You are bankrupt. GAME OVER")
                        winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\mixkit-arcade-video-game-explosion-2810.wav",\
                                           winsound.SND_FILENAME)
                        quit()
                    valid = "Yes"                                                       #Deducts expense from player's balance
                    valid = "Yes"                                                       #Ends the forced loop
                    print("$" + str(pet_expense) + " was deducted from your balance.\n"\
                          "Your balance is now: $" + str(balance))
                    break
                elif desired_items == 0:                                                #Can press 0 to return to menu
                    main()
                else:                                                                   #If unacceptable quantity entered, re-prompt
                    print("Must be an integer between 1-15.")
            except ValueError:                                                          #If input is not an integer, re-prompt
                print("Must be an integer between 1-15.")

        #Randomly selects Items A,B,C from their lists. Also pulls the parallel cost values of B and C
        while items != desired_items:                                                   #Loop will repeat until it has reached desired item count
            ItemA = random.choice(ItemsA)
            ItemB = random.choice(ItemsB)
            ItemC = random.choice(ItemsC)
            IndexB = int(ItemsB.index(ItemB))                                           #Grabs index number of ItemB
            IndexC = int(ItemsC.index(ItemC))                                           #Grabs index number of ItemC
            CostB = CostsB[IndexB]                                                      #Finds ItemB's cost with its index
            CostC = CostsC[IndexC]                                                      #Finds ItemC's cost with its index
            
            #Removes Items/Costs A,B,C from their lists to prevent repeats
            ItemsA.remove(ItemA)
            ItemsB.remove(ItemB)
            ItemsC.remove(ItemC)
            CostsB.remove(CostB)
            CostsC.remove(CostC)
            
            ItemA = ItemA.capitalize()                                                  #Capitalise ItemA for looks
            
            ItemProduct = ItemA + " " + ItemB + " " + ItemC                             #Merges Items A,B,C into product item
            
            print(ItemProduct + "\nItem Cost: $" + str(CostB + CostC))                  #Presents product item to user
            
            cart_options = ["add","pound"]                                              #Acceptable cart option inputs
            cart_option = "Undecided"
            #Cart Option Interface
            while (cart_option != cart_options) and (items < desired_items):            #Loop repeats until acceptable input given and if there are more items to complete
                cart_option = input("'Add' to cart or 'Pound' to send to pound\n")
                cart_option = cart_option.lower()
                #If chosen, adds the item to cart
                if cart_option == "add":
                    pet_cart.append(ItemProduct)                                        #Adds product item to cart list
                    pet_total = pet_total + CostB + CostC                               #Adds product cost to cart price
                    print(ItemProduct + " added to cart.")
                    break
                #If chosen, adds item to pound
                elif cart_option == "pound":
                    pound = pound + 1                                                   #Increases pound count by 1
                    print("Pound: " + str(pound) + "/20")
                    #If pound count reaches 20 (fills the pound)
                    if pound == 20:
                        print("You filled the pound! All the animals are free! $900 added to balance.")
                        pound = 0                                                       #Resets pound count
                        balance = balance + 900                                         #Adds $900 to player balance for filling the pound
                    break
                else:                                                                   #If unacceptable input, re-prompt user
                    print("Please enter 'Add' or 'Pound'.")
            
            items = items + 1                                                           #Increases items count by 1, 1 closer to reaching desired
            #If items count reaches desired amount, returns to main menu
            if items == desired_items:
                main()
    while menu == "cart":
        
        
        main()
        
            

if __name__ == '__main__':
    main()