import os
import json
import math
from models.player import Player
from models.round import Round
import random
from datetime import datetime

class Tournament:
    def __init__ (self, tmt_name, tmt_location, tmt_start_date, tmt_end_date,tmt_description, tmt_number_of_rounds=4):
        self.tmt_name = tmt_name
        self.tmt_location = tmt_location
        self.tmt_start_date = tmt_start_date
        self.tmt_end_date = tmt_end_date
        self.tmt_current_round_number = 0
        self.tmt_rounds = []
        self.tmt_registered_players = []
        self.tmt_description = tmt_description
        self.tmt_number_of_rounds = tmt_number_of_rounds

    def save_tournament_details(self):
        details = {
            "name": self.tmt_name,
            "location": self.tmt_location,
            "start_date": self.tmt_start_date,
            "end_date": self.tmt_end_date,
            "number_of_rounds": self.tmt_number_of_rounds,
            "current_round": self.tmt_current_round_number,
            "rounds": self.tmt_rounds,
            "registered_players": self.tmt_registered_players,
            "description":self.tmt_description
        }
        with open("resources/tournament.json","w") as file :
               json.dump(details,file,indent=4)
               print("New tournament saved succesfully !")

    def load_data(self):
        if os.path.exists("resources/tournament.json"):
            with open("resources/tournament.json","r") as file :
               details = json.load(file)
               self.tmt_name = details["name"]
               self.tmt_location = details["location"]
               self.tmt_start_date = details["start_date"]
               self.tmt_end_date = details["end_date"]
               self.tmt_number_of_rounds = details["number_of_rounds"]
               self.tmt_current_round_number = details["current_round"]
               self.tmt_rounds = details["rounds"] 
               self.tmt_registered_players = details["registered_players"]
               self.tmt_description = details["description"]
            return True
        else:
            return False

    def register_player (self,chess_id, last_name, first_name, birthday, country, club_name):
        is_verified_player = self.verify_player(chess_id, country, club_name)
        if is_verified_player:
            new_player = Player(last_name, first_name, birthday, chess_id)
            self.tmt_registered_players.append(new_player)
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
       
        with open("resources/tournament.json","r") as file:
            tournament = json.load(file)
            print(tournament)
        tournament["registered_players"].append(player)
        with open("resources/tournament.json","w") as file :
            json.dump(tournament,file,indent=4)
            print("New player saved succesfully !")

    def set_total_nbr_rounds(self):
        number_of_players = len(self.tmt_registered_players)
        self.tmt_number_of_rounds = int(math.log2(number_of_players))

    def generate_round (self):
        self.tmt_current_round_number += 1
        round_name = "Round " + str(self.tmt_current_round_number)
        start_date_time = datetime.now()
        current_round = Round(round_name,start_date_time)
        current_round.set_matches(self.tmt_registered_players, self.tmt_current_round_number)
        self.tmt_rounds.append(current_round)


    def calculate_score (self):
        pass

    # change or remove tmt from