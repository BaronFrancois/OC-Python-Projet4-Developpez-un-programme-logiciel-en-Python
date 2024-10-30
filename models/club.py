import json
from utils.error_util import ErrorType

class Club:
    def __init__(self):
        self.federations = []
        self.countries = []
        self.clubs = []
        self.players = []
        self.player_ids = []
        self.load()
        
    def load(self):
        with open("resources/clubs.json", "r") as file:
            details = json.load(file)
            fed = details["federations"]
            for f in fed:
                self.federations.append(f["name"])
                self.countries.append(f["country"])
                # print(f["name"], f["country"])
                fed_clubs = []
                ids_in_clubs = []
                for club in f["clubs"]:
                    fed_clubs.append(club["club_name"])
                    ids = []
                    for player in club["players"]:
                        # print(player) for the birthday error (raj)
                        self.players.append(player)
                        ids.append(player["national_chess_id"])
                    #first the directory, then appends what we want inside it 
                    ids_in_clubs.append(ids)
                # print(fed_clubs)
                # print("check for append",ids_in_clubs)
                self.clubs.append(fed_clubs)
                self.player_ids.append(ids_in_clubs)
    def check_valid_player (self, details = {}):
        if details["country"] in self.countries:
            index1 = self.countries.index(details["country"]) 
            clubs = self.clubs[index1]
            if details["club_name"] in clubs:
                index2 = clubs.index(details["club_name"])
                ids = self.player_ids[index1][index2]
                # print(ids)
                if details["chess_id"] in ids:
                    # print("player matched")
                    return self.match_player_details(details)
                else:
                    return ErrorType.PLAYER_ID_MISMATCH
            else:
                return ErrorType.CLUB_MISMATCH
        else:
            return ErrorType.COUNTRY_MISMATCH
            # print("player not matched")
            # return False
    def match_player_details(self,details):
        for player in self.players:
            if player["national_chess_id"] == details["chess_id"]:
                if player["first_name"] == details["first_name"]:
                    if player["last_name"] == details["last_name"]:
                        print(player["date_of_birth"] , details["birthday"])
                        if player["date_of_birth"] == details["birthday"]:
                            return ErrorType.NO_ERROR
                        else:
                            return ErrorType.PLAYER_BIRTHDAY_MISMATCH 
                    else:
                        return ErrorType.PLAYER_LAST_NAME_MISMATCH
                else:
                    return ErrorType.PLAYER_FIRST_NAME_MISMATCH
            
                
# club_details = Club()
# print(club_details.player_ids)
# details = {
#                     "country":"Europe",
#                     "club_name": "London Chess Club",
#                     "chess_id": "EN12245",
#                     "last_name": "Doe",
#                     "first_name": "Jon",
#                     "birthday":"1990-05-14"
#                     }
# print(club_details.check_valid_player(details))
# print(club_details.federations)
# print(club_details.countries)
# print(club_details.clubs)