import re

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
                details[key] = input(f'enter {key.replace("_", " ")} or press "0" to quit :')
                if details[key] == '0':
                    break
            else:
                print(f'enter {key.replace("_", " ")} or press "0" to quit :{value}')
        return details
        # if not country:
        #     country = input("Enter your federation's country name here (or press '0' to quit): ")
        # else:
        #     print(f"Enter your federation's country name here (or press '0' to quit):{country} ")
        # if country and country != '0':
        #     print(f"Country: {country}")
        #     if not club_name:
        #         club_name = input("Enter your federation's club name here (or press '0' to quit): ")
        #     else:
        #         print(f"Enter your federation's club name here (or press '0' to quit):{club_name} ")
        # if club_name and club_name != '0':
        #     print(f"Club name: {club_name}")

        #     while True:
        #         if not chess_id:
        #             chess_id = input("Enter your National Chess ID (or press '0' to quit): ")
        #         else:
        #             print(f"Enter your National Chess ID (or press '0' to quit):{chess_id}")
        #         if chess_id == '0':
        #             break

        #         is_valid = re.match(r"[A-Z]{2}[0-9]{5}", chess_id)
        #         if len(chess_id) == 7 and is_valid:
        #             print("Chess ID is valid")
        #             break
        #         else:
        #             print("Please enter a valid National Chess ID (2 uppercase letters followed by 5 digits).")
        #             chess_id = None

        # if chess_id and chess_id != '0':
        #     if not last_name:
        #         last_name = input("enter your last name here (or press '0' to quit):")
        #     else:
        #         print("enter your last name here (or press '0' to quit):{last_name}")
                
        # if last_name and last_name != '0':
        #     if not first_name:
        #         first_name = input("enter your first name here (or press '0' to quit):")
        #     else:
        #         print("enter your first name here (or press '0' to quit):{first_name}")
        # if first_name and first_name != '0':
        #     if not birthday:
        #         birthday = input("enter your birthday's date here (or press '0' to quit):")  
        #     else: 
        #         print("enter your birthday's date here (or press '0' to quit):{birthday}")    
        # if country == '0' or club_name == '0' or chess_id == '0' or first_name == '0' or last_name == '0' or birthday == '0':
        #     print("Registration process exited.")
        # else:
        #     print("application closed")
        # return (chess_id, last_name, first_name, birthday, country, club_name)

    @staticmethod
    def create_tournament(details = None):
        if details:
            tmt_name = details["tmt_name"]
            tmt_location = details["tmt_location"]
            tmt_start_date = details["tmt_start_date"]
            tmt_end_date = details["tmt_end_date"]
            tmt_description = details["tmt_description"] 
        else:
            tmt_name = tmt_location = tmt_start_date = tmt_end_date = tmt_description = None
            
        if not tmt_name:
            tmt_name = input("Enter the tournament name (or press '0' to quit): ")
        else:
            print(f"Enter the tournament name (or press '0' to quit): {tmt_name}")
        
        if tmt_name and tmt_name != '0':
            print(f"Tournament Name: {tmt_name}")

            
            if not tmt_location:
                tmt_location = input("Enter the tournament location (or press '0' to quit): ")
            else:
                print(f"Enter the tournament location (or press '0' to quit): {tmt_location}")

            if tmt_location and tmt_location != '0':
                print(f"Tournament Location: {tmt_location}")

                
                if not tmt_start_date:
                    tmt_start_date = input("Enter the tournament start date (or press '0' to quit): ")
                else:
                    print(f"Enter the tournament start date (or press '0' to quit): {tmt_start_date}")

                if tmt_start_date and tmt_start_date != '0':
                    print(f"Tournament Start Date: {tmt_start_date}")

                    
                    if not tmt_end_date:
                        tmt_end_date = input("Enter the tournament end date (or press '0' to quit): ")
                    else:
                        print(f"Enter the tournament end date (or press '0' to quit): {tmt_end_date}")

                    if tmt_end_date and tmt_end_date != '0':
                        print(f"Tournament End Date: {tmt_end_date}")

                        
                        if not tmt_description:
                            tmt_description = input("Enter the tournament description (or press '0' to quit): ")
                        else:
                            print(f"Enter the tournament description (or press '0' to quit): {tmt_description}")

                        if tmt_description and tmt_description != '0':
                            print(f"Tournament Description: {tmt_description}")

        
        if tmt_name == '0' or tmt_location == '0' or tmt_start_date == '0' or tmt_end_date == '0' or tmt_description == '0':
            print("Tournament creation process exited.")
        else:
            print("Tournament created successfully.")
        
        return (tmt_name, tmt_location, tmt_start_date, tmt_end_date, tmt_description)

        
        



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