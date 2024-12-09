import json
from utils.error_util import ErrorType
from models.player import Player

class Club:
    def __init__(self):
        self.players = []
        # call load method to load player from json : when a club is created the data is automaticly loaded
        self.load()
    
    def load(self):
        with open("resources/clubs.json", "r") as file:
            # file content is loaded in a form of a dictionnary 
            details = json.load(file)
            # getting access to federation key from details dictionnary
            fed = details["federations"]
            for f in fed:
                for club in f["clubs"]:
                    for player in club["players"]:
                        player["federation"] = f["name"]
                        player["country"] = f["country"]
                        player["club_name"] = club["club_name"]
                        player_object = Player(dictionary = player)
                        self.players.append(player_object)
    
    # checking if the player data correspond to the details from clubs.json 
    def check_valid_player (self, details = {}):
        for player in self.players:
            if player.national_chess_id == details["national_chess_id"]:
                if player.first_name == details["first_name"]:
                    if player.last_name == details["last_name"]:
                        # print(player.date_of_birth , details["birthday"])
                        if player.date_of_birth == details["date_of_birth"]:
                            if player.country == details["country"]:
                                if player.club_name == details["club_name"]:
                                    if player.federation == details["federation"]:
                                        return ErrorType.NO_ERROR
                                    else:
                                        return ErrorType.PLAYER_FED_MISMATCH
                                else : 
                                    return ErrorType.CLUB_MISMATCH
                            else:
                                return ErrorType.COUNTRY_MISMATCH
                        else:
                            return ErrorType.PLAYER_BIRTHDAY_MISMATCH 
                    else:
                        return ErrorType.PLAYER_LAST_NAME_MISMATCH
                else:
                    return ErrorType.PLAYER_FIRST_NAME_MISMATCH
        return ErrorType.PLAYER_ID_MISMATCH