import re


def register_player_view(details = None):
    if details:
        country = details["country"]
        club_name =details["club_name"]
        chess_id = details["chess_id"]
        last_name = details["last_name"]
        first_name = details["first_name"]
        birthday = details["birthday"]
    else:    
    # Add exit condition to all, if user exits -> print a message
        country = club_name = chess_id = last_name = first_name =   birthday = None
    if not country:
        country = input("Enter your federation's country name here (or press '0' to quit): ")
    else:
        print(f"Enter your federation's country name here (or press '0' to quit):{country} ")
    if country and country != '0':
        print(f"Country: {country}")
        if not club_name:
            club_name = input("Enter your federation's club name here (or press '0' to quit): ")
        else:
            print(f"Enter your federation's club name here (or press '0' to quit):{club_name} ")
    if club_name and club_name != '0':
        print(f"Club name: {club_name}")

        while True:
            if not chess_id:
                chess_id = input("Enter your National Chess ID (or press '0' to quit): ")
            else:
                print(f"Enter your National Chess ID (or press '0' to quit):{chess_id}")
            if chess_id == '0':
                break

            is_valid = re.match(r"[A-Z]{2}[0-9]{5}", chess_id)
            if len(chess_id) == 7 and is_valid:
                print("Chess ID is valid")
                break
            else:
                print("Please enter a valid National Chess ID (2 uppercase letters followed by 5 digits).")

    if chess_id and chess_id != '0':
        if not last_name:
            last_name = input("enter your last name here (or press '0' to quit):")
        else:
            print("enter your last name here (or press '0' to quit):{last_name}")
            
    if last_name and last_name != '0':
        if not first_name:
            first_name = input("enter your first name here (or press '0' to quit):")
        else:
            print("enter your first name here (or press '0' to quit):{first_name}")
    if first_name and first_name != '0':
        if not birthday:
            birthday = input("enter your birthday's date here (or press '0' to quit):")  
        else: 
            print("enter your birthday's date here (or press '0' to quit):{birthday}")    
    if country == '0' or club_name == '0' or chess_id == '0' or first_name == '0' or last_name == '0' or birthday == '0':
        print("Registration process exited.")
    else:
        print("application closed")
    return (chess_id, last_name, first_name, birthday, country, club_name)

# implement when press 0, stop the code
def create_tournament_view():
    tmt_name = input("enter the tournament name:")
    tmt_location = input("enter the tournament location:")
    tmt_start_date = input("enter the tournament start date:")
    tmt_end_date = input("enter the tournament end date:")
    tmt_description = input("enter the tournament description:")
    return (tmt_name, tmt_location, tmt_start_date, tmt_end_date, tmt_description)


def show_all_players(players):
    for name, chess_id in players.items():
        print(f"Name: {name},\t\tChess ID: {chess_id}")


def show_all_tournaments(tournaments):
    for tournament in tournaments:
        print(
            f"name:{tournament["name"]}, location :{tournament["location"]}, start_date:{tournament["start_date"]}, end_date:{tournament["end_date"]}"
        )


def show_tournament_round(round_name, start_date_time, end_date_time):
    print(
        f"round name:{round_name}, start date time:{start_date_time}, end date time:{end_date_time}"
    )
# check all of the options main menu's, the files, start the tournament, check details
def show_round_matches(player1, player2):
    print("player 1 vs player 2")
    print(f"name {player1.last_name} {player1.first_name}, {player2.last_name} {player2.first_name}" )
    print(f"NCID {player1.national_chess_id}, {player2.national_chess_id}")
    print(f"DOB {player1.date_of_birth},  {player2.date_of_birth}")
    print(f"scores {player1.plyr_score}, {player2.plyr_score}")
    print(f"winner {not player1.has_lost}, {not player2.has_lost}")
    print("---------------------------")