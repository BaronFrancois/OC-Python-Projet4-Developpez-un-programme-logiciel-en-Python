import re


def register_player_view():
    country = input("enter your federation's country name here:")
    club_name = input("enter your federation's club name here:")
    # get chess ID
    while True:
        chess_id = input("enter your National Chess ID:")
        is_valid = re.match("[A-Z]{2}[0-9]{5}", chess_id)
        if len(chess_id) == 7 and is_valid:
            print("Chess Id is valid")
            break

        else:
            print("please enter a valide national chess Id:")

    # get remaining details
    last_name = input("enter your last name here :")
    first_name = input("enter your first name here :")
    birthday = input("enter your birthday's date here :")

    return (chess_id, last_name, first_name, birthday, country, club_name)


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