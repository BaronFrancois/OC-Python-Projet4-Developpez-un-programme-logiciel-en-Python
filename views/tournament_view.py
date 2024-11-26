import re
from utils.error_util import ErrorType

class View:
    @staticmethod
    def register_player(details = {}):
        if not details:
            details = {
                    "federation":None,
                    "country":None,
                    "club_name": None,
                    "national_chess_id": None,
                    "last_name": None,
                    "first_name": None,
                    "date_of_birth":None
                    }
        for key,value in details.items():
            # print(key,value)
            if not value or value == "0":
                while True :
                    details[key] = input(f'enter {key.replace("_", " ")} or press "0" to quit :')
                    if key == "chess_id" :
                        is_valid = re.match(r"[A-Z]{2}[0-9]{5}", details[key])
                        if not is_valid:
                            print(ErrorType.INVALID_CHESS_ID)
                            continue
                    break 
                    # while break
                if details[key] == '0':
                    break
                    # for loop break
            else:
                print(f'enter {key.replace("_", " ")} or press "0" to quit :{value}')
        return details

    @staticmethod
    def create_tournament(details = {}):
        if not details:
            details = {
                    "name":None,
                    "location": None,
                    "start_date": None,
                    # "end_date": None,
                    "description": None
                    }
        for key,value in details.items():
            # print(key,value)
            if not value or value == "0":
                details[key] = input(f'enter {key.replace("_", " ")} or press "0" to quit :')
                if details[key] == '0':
                    break
                    # for loop break
            else:
                print(f'enter {key.replace("_", " ")} or press "0" to quit :{value}')
        return details  
        
    @staticmethod
    def show_all_players(players):
        for name, chess_id in players.items():
            print(f"Chess ID: {chess_id},\t\tName: {name}")
        report_ask = input("Do you want to save the players inside the report ?  Y/N :")
        return report_ask
    
    @staticmethod
    def show_report(report):
        for line in report:
            print(line)
            
    @staticmethod
    def show_winner(winner):
        print("")
        # convert if statement into view
        print("final winner decided") 
        print("the tournament winner is", winner)
        
    @staticmethod
    def show_not_final_winner():   
         print()
         print("no final winner yet")
    @staticmethod
    def show_all_tournaments(tournament):
        
            print(
                f"name:{tournament["name"]}, location :{tournament["location"]}, start_date:{tournament["start_date"]}, end_date:{tournament["end_date"]}"
            )
    @staticmethod
    def ask_for_report():
        ask_report = input("Do you want to save the report ? y/n :")
        if ask_report.lower() == "y":
            return True
        else:
            return False

    @staticmethod
    def show_tournament_round(round_name, start_date_time, end_date_time):
        print(
            f"round name:{round_name}, start date time:{start_date_time}, end date time:{end_date_time}"
        )

    @staticmethod
    def show_round_matches(player1, player2):
        print("player 1 vs player 2")
        print(f"name {player1.last_name} {player1.first_name}, {player2.last_name} {player2.first_name}" )
        print(f"NCID {player1.national_chess_id}, {player2.national_chess_id}")
        print(f"DOB {player1.date_of_birth},  {player2.date_of_birth}")
        print(f"scores {player1.plyr_score}, {player2.plyr_score}")
        print(f"winner {not player1.has_lost}, {not player2.has_lost}")
        print("---------------------------")
        
    @staticmethod
    def ask_match_result(player1, player2):
        while True:
            # Prompt the user for the match result
            print("")
            print(player1.first_name,"///VS///" ,player2.first_name)
            print(f'press 1 {player1.first_name} won the match ')
            print(f'press 2 {player2.first_name} won the match ')
            print('press 3 for draw')
            ask_result = int(input("Choose match winner :"))
            if ask_result == 1 or ask_result == 2 :
                break
            elif ask_result != 3:
                print("please enter a valid option:")
            elif ask_result == 3:
                print("match is draw, the players are playing again.")
        
        return ask_result

    @staticmethod
    def show_round_details(round):
        print("---------------------------")
        print("Round Name       :",round.rnd_name)
        print("Round Start Date :",round.rnd_start_datetime)
        print("Round End Date   :",round.rnd_end_datetime)
        # print("")
        