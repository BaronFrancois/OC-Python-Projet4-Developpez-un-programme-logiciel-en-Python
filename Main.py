# ask the person press  1-register player
#                       2-start the tournament
#                       3-check tounrament report
from controllers.tournament_controller import TournamentController

tournament_manager = TournamentController()
tournament_manager.load_tournament_data()
while True:
    print("-----------------------------------------")
    print("press 1 to register player:")
    print("press 2 to start the tournament:")
    print("press 3 to check tournament report:")
    print("press 4 to create tournament:")
    print("press 5 to exit:")

    user_input = int(input("enter your choice (number):"))
    if user_input == 1:
        if not tournament_manager.tournament:
            print("No tournament exists yet")
        else:
            tournament_manager.register_player()

    elif user_input == 2:
        if not tournament_manager.tournament:
            print("No tournament exists yet")
        else:
            tournament_manager.start_tournament()
    elif user_input == 3:
        pass
    elif user_input == 4:
      tournament_manager.create_tournament()
      print("the tournament has been created")
    elif user_input == 5:
        print("thank you for using the application:")
        break
    else :
        print("please select a valid option:")

    # for the next time, generate report 

    