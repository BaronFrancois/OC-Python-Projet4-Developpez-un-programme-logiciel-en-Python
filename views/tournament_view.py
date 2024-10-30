import re
from utils.error_util import ErrorType

class View:
    @staticmethod
    def register_player(details = {}):
        if not details:
            details = {
                    "country":None,
                    "club_name": None,
                    "chess_id": None,
                    "last_name": None,
                    "first_name": None,
                    "birthday":None
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
                    "tmt_name":None,
                    "tmt_location": None,
                    "tmt_start_date": None,
                    "tmt_end_date": None,
                    "tmt_description": None
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
        # if details:
        #     tmt_name = details["tmt_name"]
        #     tmt_location = details["tmt_location"]
        #     tmt_start_date = details["tmt_start_date"]
        #     tmt_end_date = details["tmt_end_date"]
        #     tmt_description = details["tmt_description"] 
        # else:
        #     tmt_name = tmt_location = tmt_start_date = tmt_end_date = tmt_description = None
            
        # if not tmt_name:
        #     tmt_name = input("Enter the tournament name (or press '0' to quit): ")
        # else:
        #     print(f"Enter the tournament name (or press '0' to quit): {tmt_name}")
        
        # if tmt_name and tmt_name != '0':
        #     print(f"Tournament Name: {tmt_name}")

            
        #     if not tmt_location:
        #         tmt_location = input("Enter the tournament location (or press '0' to quit): ")
        #     else:
        #         print(f"Enter the tournament location (or press '0' to quit): {tmt_location}")

        #     if tmt_location and tmt_location != '0':
        #         print(f"Tournament Location: {tmt_location}")

                
        #         if not tmt_start_date:
        #             tmt_start_date = input("Enter the tournament start date (or press '0' to quit): ")
        #         else:
        #             print(f"Enter the tournament start date (or press '0' to quit): {tmt_start_date}")

        #         if tmt_start_date and tmt_start_date != '0':
        #             print(f"Tournament Start Date: {tmt_start_date}")

                    
        #             if not tmt_end_date:
        #                 tmt_end_date = input("Enter the tournament end date (or press '0' to quit): ")
        #             else:
        #                 print(f"Enter the tournament end date (or press '0' to quit): {tmt_end_date}")

        #             if tmt_end_date and tmt_end_date != '0':
        #                 print(f"Tournament End Date: {tmt_end_date}")

                        
        #                 if not tmt_description:
        #                     tmt_description = input("Enter the tournament description (or press '0' to quit): ")
        #                 else:
        #                     print(f"Enter the tournament description (or press '0' to quit): {tmt_description}")

        #                 if tmt_description and tmt_description != '0':
        #                     print(f"Tournament Description: {tmt_description}")

        
        # if tmt_name == '0' or tmt_location == '0' or tmt_start_date == '0' or tmt_end_date == '0' or tmt_description == '0':
        #     print("Tournament creation process exited.")
        # else:
        #     print("Tournament created successfully.")
        
        # return (tmt_name, tmt_location, tmt_start_date, tmt_end_date, tmt_description)

        
        



    @staticmethod
    def show_all_players(players):
        for name, chess_id in players.items():
            print(f"Chess ID: {chess_id},\t\tName: {name}")
        report_ask = input("Do you want to save the players inside the report ?  Y/N :")
        return report_ask


    @staticmethod
    def show_all_tournaments(tournament):
        
            print(
                f"name:{tournament["name"]}, location :{tournament["location"]}, start_date:{tournament["start_date"]}, end_date:{tournament["end_date"]}"
            )
    @staticmethod
    def ask_for_report():
        ask_report = input("Do you want to save the report ? y/n :")
        return ask_report.lower()

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
        print(player1.first_name,"///VS///" ,player2.first_name)
        print(f'press 1 {player1.first_name} won the match ')
        print(f'press 2 {player2.first_name} won the match ')
        print('press 3 for draw')
        ask_result = int(input(""))
        return ask_result

# details = View.register_player({
#                     "country":"france",
#                     "club_name": "club_name",
#                     "chess_id": "0",
#                     "last_name": None,
#                     "first_name": None,
#                     "birthday":None
#                     })

# if "0" in details.values():
#     print("system exited")