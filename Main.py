# ask the person press  1-register player
#                       2-start the tournament
#                       3-check tounrament report
from views.registration_view import register_player
while True:
    print("-----------------------------------------")
    print("press 1 to register player:")
    print("press 2 to start the tournament:")
    print("press 3 to check tournament report:")
    print("press 4 to exit:")

    user_input = int(input("enter your choice (number):"))
    if user_input == 1:
        register_player()
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        print("thank you for using the application:")
        break
    else :
        print("please select a valid option:")
    