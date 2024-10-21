import json


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
                ids = self.player_ids[index2]
                if details["chess_ids"] in ids:
                    return True
                # else:
                #     return False
                # can we check for all keys in once ? We need country, club_name and chess_id
            
            
club_details = Club()
print(club_details.player_ids)
# print(club_details.federations)
# print(club_details.countries)
# print(club_details.clubs)