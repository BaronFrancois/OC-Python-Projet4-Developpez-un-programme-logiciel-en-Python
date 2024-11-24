import os
import json
from controllers.tournament_controller import TournamentController

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
        tournament_manager = TournamentController()
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
            is_loaded = tournament_manager.load(tournament_name)
            if not is_loaded:
                print("no such tournament exists")
                continue

        if user_input in range(1,9):
            func = getattr(tournament_manager,options[user_input])
            succes = func(details, user_input)
            if not succes:
                break
            # fix 
        else :
            print("please select a valid option:")
        details = None

if __name__== '__main__':
    main()