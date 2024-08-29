import os
import json
import math
from models.player import Player
from models.round import Round
import random
from datetime import datetime

class Tournament:
    def __init__ (self, name, location, start_date, end_date,description, number_of_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = 0
        self.rounds = []
        self.registered_players = []
        self.description = description
        self.number_of_rounds = number_of_rounds

    def save_tournament_details(self):
        details = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round_number,
            "rounds": self.rounds,
            "registered_players": self.registered_players,
            "description":self.description
        }
        with open(f"resources/{self.name}.json","w") as file :
               json.dump(details,file,indent=4)
               print("New tournament saved succesfully !")

    def load_data(self):
        if os.path.exists(f"resources/{self.name}.json"):
            with open(f"resources/{self.name}.json","r") as file :
               details = json.load(file)
               self.name = details["name"]
               self.location = details["location"]
               self.start_date = details["start_date"]
               self.end_date = details["end_date"]
               self.number_of_rounds = details["number_of_rounds"]
               self.current_round_number = details["current_round"]
               self.rounds = details["rounds"] 
               self.registered_players = details["registered_players"]
               self.description = details["description"]
            return True
        else:
            return False

    def register_player (self,chess_id, last_name, first_name, birthday, country, club_name):
        is_verified_player = self.verify_player(chess_id, country, club_name)
        if is_verified_player:
            new_player = Player(last_name, first_name, birthday, chess_id)
            self.registered_players.append(new_player)
            self.update_tournament_file(new_player)
        else:
            print("player is not verified")

    def verify_player (self,chess_id, country, club_name):
        with open("resources/clubs.json","r") as file :
               details = json.load(file)
               fed = details["federations"]
               for f in fed :
                   if f["country"] == country:
                       clubs = f["clubs"]
                       for club in clubs:
                           if club["club_name"] == club_name:
                               players = club["players"]
                               for player in players:
                                   if player["national_chess_id"] == chess_id:
                                       return True
        return False

    def update_tournament_file(self,new_player):
        player = {"national_chess_id":new_player.national_chess_id,
                "last_name": new_player.last_name,
                "first_name":new_player.first_name,
                "date_of_birth": new_player.date_of_birth
                }
       
        with open(f"resources/{self.name}.json","r") as file:
            tournament = json.load(file)
            # print(tournament)
        tournament["registered_players"].append(player)
        with open(f"resources/{self.name}.json","w") as file :
            json.dump(tournament,file,indent=4)
            print("New player saved succesfully !")

    def set_total_nbr_rounds(self):
        number_of_players = len(self.registered_players)
        self.number_of_rounds = int(math.log2(number_of_players))

    def generate_round (self):
        self.current_round_number += 1
        round_name = "Round " + str(self.current_round_number)
        start_date_time = datetime.now()
        current_round = Round(round_name,start_date_time)
        current_round.set_matches(self.registered_players, self.current_round_number)
        self.rounds.append(current_round)

    def start_round(self):
        self.rounds[self.current_round_number -1].start_matches()
        self.rounds[self.current_round_number -1].rnd_end_datetime = datetime.now()

    def calculate_score (self):
        pass
# We need to add tournaments into json format (multiple tournaments at the same time)