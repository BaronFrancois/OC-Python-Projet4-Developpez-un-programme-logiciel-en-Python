import os
import json
from controllers.tournament_controller import TournamentController

if os.path.exists("resources/resume_file.json"):
    with open("resources/resume_file.json","r") as file:
        details = json.load(file)
        for key in details:
            if details[key] == "0":
                details[key] = None
                break
    os.remove("resources/resume_file.json")
else:
    details = "empty"

# créer un menu à étape
while True:
    tournament_manager = TournamentController()
    if details == "empty":
        print("-----------------------------------------")
        print("press 1 to create tournament::")
        # implement a fucntion within tournament controller : see all   players - function call another function inside views = function  show all players, read clubs.json show first name of all the     player from all the clubs (chess id )
        print("press 2 to see the list of all players:")
        print("press 3 to see the list of all tournaments:")
        print("press 4 to register player:")
        print("press 5 to start the tournament:")
        print("press 6 search for particular tournament :")
        print("press 7 to see the list of all players in particular     tournament :")
        print("press 8 to see all rounds and matches in tournament :")
        print("press 9 to exit:")

        user_input = int(input("enter your choice (number):"))
        if user_input in [4,5,6,7,8]:
            tournament_name = input("enter the tournament name:")
            tournament_manager.load_tournament_data(tournament_name)
            # create the exit and save
        if user_input == 1:
            succes = tournament_manager.create_tournament()            
            if not succes:
                break
            else:
                print("the tournament has been created")
        elif user_input == 2:
            tournament_manager.see_all_players()

        elif user_input == 3:
            tournament_manager.see_all_tournaments()

        elif user_input == 4:
            if not tournament_manager.tournament:
                print("No tournament exists yet")
            else:
                succes = tournament_manager.register_player()
                if not succes:
                    break

        elif user_input == 5:
            if not tournament_manager.tournament:
                print("No tournament exists yet")
            else:
                tournament_manager.start_tournament()
        elif user_input == 6:
            tournament_manager.search_tournament()

        elif user_input == 7:
            tournament_manager.show_tournament_players()

        elif user_input == 8:
            tournament_manager.show_tournament_report()

        elif user_input == 9:
            print("thank you for using the application:")
            break
        else :
            print("please select a valid option:")

# if resume file is present
    else: 
        user_input = details["option_number"]
        if user_input in [4,5,6,7,8]:
            tournament_name = details["tournament"]
            tournament_manager.load_tournament_data(tournament_name)

        if user_input == 1:
            succes = tournament_manager.create_tournament(details)            
            if not succes:
                break
            else:
                print("the tournament has been created")
                
        elif user_input == 2:
            tournament_manager.see_all_players()

        elif user_input == 3:
            tournament_manager.see_all_tournaments()

        elif user_input == 4:
            if not tournament_manager.tournament:
                print("No tournament exists yet")
            else:
                succes = tournament_manager.register_player(details)
                if not succes:
                    break

        elif user_input == 5:
            if not tournament_manager.tournament:
                print("No tournament exists yet")
            else:
                tournament_manager.start_tournament()
        elif user_input == 6:
            tournament_manager.search_tournament()

        elif user_input == 7:
            tournament_manager.show_tournament_players()

        elif user_input == 8:
            tournament_manager.show_tournament_report()

        elif user_input == 9:
            print("thank you for using the application:")
            break
        else :
            print("please select a valid option:")
        details = "empty"

