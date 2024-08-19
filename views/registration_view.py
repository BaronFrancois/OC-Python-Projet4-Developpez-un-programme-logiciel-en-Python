import re
import os
import json
# create a function

def register_player ():
# get chess ID
    while True:
        chess_id = input("enter your National Chess ID:")
        is_valid = re.match("[A-Z]{2}[0-9]{5}",chess_id)
        if len(chess_id) == 7 and is_valid:
            print("Chess Id is valid")
            break

        else :
            print("please enter a valide national chess Id:")

    # get remaining details
    last_name = input("enter your last name here :")
    first_name = input("enter your first name here :")
    birtday = input("enter your birthday's date here :")

    player = {"chess_id":chess_id,
              "last_name": last_name,
              "first_name":first_name,
              "birthday": birtday
              }

    if os.path.exists("resources/players.json"):
        with open("resources/players.json","r") as file:
            players = json.load(file)
            print(players)
        players.append(player)
        with open("resources/players.json","w") as file :
            json.dump(players,file,indent=4)
            print("New player saved succesfully !")
    else :
        with open("resources/players.json","w") as file :
            json.dump([player],file,indent=4)
            print("succesfull file creation")
    print("registration succefull")