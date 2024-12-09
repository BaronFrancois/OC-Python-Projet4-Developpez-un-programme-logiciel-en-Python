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
    def show_winner(winner):
        print("")
        # convert if statement into view
        print("final winner decided") 
        print("the tournament winner is", winner)
        
    @staticmethod
    def show_not_final_winner():   
        print()
        print("no final winner yet")
        

        