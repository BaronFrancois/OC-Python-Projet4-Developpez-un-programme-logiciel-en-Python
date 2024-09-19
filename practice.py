import os
import time

# print("hello")
# time.sleep(5)
# # Clearing the Screen
# os.system('cls')

# print("hello hello")
# input("Press Enter to Exit...")

def update_number():
    os.system('cls')
    print()
    print('\t'*5, "-----------------------")
    print('\t'*5, 'Number has been updated')
    print('\t'*5, "-----------------------")
    print()
    input("Press Enter to Exit...")

def delete_number():
    os.system('cls')
    print()
    print('\t'*5, "-----------------------")
    print('\t'*5, 'Number has been deleted')
    print('\t'*5, "-----------------------")
    print()
    input("Press Enter to Exit...")

def see_number():
    os.system('cls')
    print()
    print('\t'*5, "-----------------------")
    print('\t'*5, "Number is hidden so you can't see")
    print('\t'*5, "-----------------------")
    print()
    input("Press Enter to Exit...")

def exit_message():
    os.system('cls')
    print()
    print('\t'*5, "-----------------------")
    print('\t'*5, "Thank you for using the app")
    print('\t'*5, "-----------------------")
    print()
    input("Press Enter to Exit...")

def main_menu():
    while True:
        os.system('cls')
        print()
        print('\t'*5, "-----------------------")
        print('\t'*5, 'Press 1 - Update Number')
        print('\t'*5, 'Press 2 - Delete Number')
        print('\t'*5, 'Press 3 - See Number')
        print('\t'*5, 'Press 4 - Exit')
        print('\t'*5, "-----------------------")
        print()
        choice = int(input('\t'*5 + " Enter your choice or 0 to Quit:\t"))
        
        if choice == 1:
            update_number()
        elif choice == 2:
            delete_number()
        elif choice == 3:
            see_number()
        else:
            exit_message()
            break


main_menu()
