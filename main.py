##############################################################################
# Title: Continuous Game Play/RPG Simple menu                                  
# Class: Computer Science 30                                                                  
# Date: March 25, 2023
# Coders Name: Saubaan Shaikh                                             
# Version: 001   
##############################################################################
'''This code creates a Game Menu that continuously loops'''
##############################################################################

# Available characters the player can choose
characters = ["Bowser", "Mario", "Luigi", "Toad"]

# Available items that can be stored in the inventory
inventory = ["Axe", "Spear", "Sword", "Knife"]


def Game_Menu():
    '''Function for the main menu where all the option are'''
    print("Welcome to the Game Menu!")
    print("1. Start Game!")
    print("2. Choose your charachter")
    print("3. View Inventory")
    print("4. Save Game")
    print("5. Quit game")


def Start_Game():
    '''Message to the player before game starts'''
    print("The Game Has Started!")


def Choose_Characters():
    '''Asking the player what character they would like to play as'''
    print("Choose Your character")


def View_Inventory():
    '''Telling the player what is in their inventory'''
    print("This is your inventory")


def Save_Game():
    '''Function so user can come back to where he left off'''
    print("Checkpoint Set, Game Saved")


def Quit_Game():
    '''Function so user can quit the game'''
    print("You have quit the game, thanks for playing!")


def Invalid_Choice():
    '''Function if user chooses an option that does not exist'''
    print("Invalid choice, please try another option")


while True:
    # Continous loop for the Game Menu itself
    Game_Menu()
    choice = input("Enter your choice: ")
    # 
    if choice == "1":
      Start_Game()
    elif choice == "2":
      Choose_Characters()
    elif choice == "3":
      View_Inventory()
    elif choice == "4":
      Save_Game()
    elif choice == "5":
      Quit_Game()
      break
    else:
      Invalid_Choice()
