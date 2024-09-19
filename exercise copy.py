import re
import os

def register_player_view():
    os.system('cls')
    # Add exit condition to all, if user exits -> print a message
    while True:
        country = input("Enter your federation's country name here (or press '0' to quit): ")
        if country == '0':
            print("Registration process exited.")
            break
        print(f"Country: {country}")

        club_name = input("Enter your federation's club name here (or press '0' to quit): ")
        if club_name == '0':
            print("Registration process exited.")
            break
        print(f"Club name: {club_name}")

        while True:
            chess_id = input("Enter your National Chess ID (or press '0' to quit): ")
            if chess_id == '0':
                print("Registration process exited.")
                break

            is_valid = re.match(r"[A-Z]{2}[0-9]{5}", chess_id)
            if len(chess_id) == 7 and is_valid:
                print("Chess ID is valid")
                break
                
            else:
                print("Please enter a valid National Chess ID (2 uppercase letters followed by 5 digits).")
        
        if chess_id == '0':
            break
        # how to break loop here ? if chess_id is valid ?

    print("Application closed")

register_player_view()
