# ask the person press  1-register player
#                       2-start the tournament
#                       3-check tounrament report
from controllers.tournament_controller import TournamentController


while True:
    tournament_manager = TournamentController()
    print("-----------------------------------------")
    print("press 1 to create tournament::")
    # implement a fucntion within tournament controller : see all players - function call another function inside views = function show all players, read clubs.json show first name of all the player from all the clubs (chess id )
    print("press 2 to see the list of all players:")
    print("press 3 to see the list of all tournaments:")
    print("press 4 to register player:")
    print("press 5 to start the tournament:")
    print("press 6 search for particular tournament :")
    print("press 7 to see the list of all players in particular tournament :")
    print("press 8 to see all rounds and matches in tournament :")
    print("press 9 to exit:")

    user_input = int(input("enter your choice (number):"))
    if user_input in [4,5,6,7,8]:
        tournament_name = input("enter the tournament name:")
        tournament_manager.load_tournament_data(tournament_name)
    if user_input == 1:
        tournament_manager.create_tournament()
        print("the tournament has been created")
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass

    elif user_input == 4:
        if not tournament_manager.tournament:
            print("No tournament exists yet")
        else:
            tournament_manager.register_player()

    elif user_input == 5:
        if not tournament_manager.tournament:
            print("No tournament exists yet")
        else:
            tournament_manager.start_tournament()
    elif user_input == 6:
        pass

    elif user_input == 7:
        pass

    elif user_input == 8:
        pass

    elif user_input == 9:
        print("thank you for using the application:")
        break
    else :
        print("please select a valid option:")

    # for the next time, generate report 

    