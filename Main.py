import os
import json
from controllers.main_controller import MainController
from utils.error_util import ResultType

def show_menu():
    print("-----------------------------------------")
    print("press 1 to create tournament :")
    print("press 2 to see the list of all players :")
    print("press 3 to see the list of all tournaments :")
    print("press 4 to register player :")
    print("press 5 to start the tournament :")
    print("press 6 show particular tournament details :")
    print("press 7 to see the list of all players in particular tournament :")
    print("press 8 to see all rounds and matches in tournament :")
    print("press 9 to exit :")

def resume_app():
    if os.path.exists("resources/resume_file.json"):
        with open("resources/resume_file.json","r") as file:
            details = json.load(file)
            for key in details:
                if details[key] == "0":
                    details[key] = None
                    break
        os.remove("resources/resume_file.json")
    else:
        details = None
    return details

def main(): 
    details = resume_app()
    options = {
                1:'create_tournament',
                2:'show_all_clubs_players',
                3:'show_all_tournaments',
                4:'register_player',
                5:'start_tournament',
                6:'show_particular_tournament',
                7:'show_tournament_players',
                8:'show_tournament_report'
            }

    while True:
        main_controller = MainController()
        if details :
            user_input = details["option_number"]
        else:
            show_menu()
            user_input = int(input("enter your choice (number):"))

        if user_input == 9:
            print("thank you for using the application:")
            break
        if user_input in range (4,9):
            if details:
                tournament_name = details["tournament"]
            else:
                tournament_name = input("enter the tournament name:")
            is_loaded = main_controller.load(tournament_name)
            if not is_loaded:
                print("no such tournament exists")
                continue

        if user_input in range(1,9):
            func = getattr(main_controller,options[user_input])
            result = func(details, user_input)
            if result != ResultType.SUCCES:
                break
            # fix 
        else :
            print("please select a valid option:")
        details = None

if __name__== '__main__':
    main()