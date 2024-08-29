import re
import json

def register_player_view ():
    
    country = input("enter your federation's country name here:")
    club_name = input("enter your federation's club name here:")
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
    birthday = input("enter your birthday's date here :")

   
    return (chess_id, last_name, first_name, birthday, country, club_name)

def create_tournament_view ():
    tmt_name = input("enter the tournament name")
    tmt_location = input("enter the tournament location")
    tmt_start_date = input("enter the tournament start date")
    tmt_end_date = input("enter the tournament end date")
    tmt_description = input("enter the tournament description")
    return (tmt_name,tmt_location,tmt_start_date, tmt_end_date,tmt_description)

def get_players():
    with open("resources/club.json","r") as file :
        details = json.load(file)
        first_name = details["first_name"]
        last_name = details["last_name"]
        date_of_birth = details["date_of_birth"]
        national_chess_id = details["national_chess_id"]