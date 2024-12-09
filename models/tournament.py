import os
import json
import math
from datetime import datetime, timedelta
from models.player import Player
from models.round import Round
from models.match import Match
from copy import deepcopy

class Tournament:
    def __init__(self, name = None, location= None, start_date= None, end_date= None, description= None, number_of_rounds=4, dictionary = None):
        # Initialize a tournament with its details
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.registered_players = []
        self.current_players = []
        if dictionary :
            self.__set_attributes(dictionary)
            
    def __set_attributes (self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

    def get_reg_player_dict(self):
        return [player.__dict__ for player in self.registered_players]
    
    def get_rounds_dict(self):
        rounds = []
        for round in deepcopy(self.rounds):
            round = round.__dict__
            rnd_matches = []
            for match in round["rnd_matches"]:
                match =[match.player1.__dict__,match.player2.__dict__]
                rnd_matches.append(match)
            round["rnd_matches"] = rnd_matches    
            rounds.append(round)    
        return rounds
    
    # check for the function to cut it into Round
    def add_flat_player(self,round,player,player_number):
        player.pop("federation")
        player.pop("country")
        player.pop("club_name")
        player.pop("plyr_score")
        player.pop("date_of_birth")
        if player["has_lost"]:
            player["has_lost"] = "yes"
        else:
            player["has_lost"] = "no"
        for key,value in player.items():
            round[f"{player_number}_{key}"] = value
            
    def get_flat_rounds_dict(self):
        rounds = []
        for round in deepcopy(self.rounds):
            round = round.__dict__
            for match in round["rnd_matches"]:
                round_copy  = deepcopy(round)
                round_copy.pop("rnd_matches")    
                self.add_flat_player(round_copy,match.player1.__dict__,"p1")
                self.add_flat_player(round_copy,match.player2.__dict__,"p2")
                rounds.append(round_copy)  
        return rounds
    
    def save(self):
        # Save the tournament details to a JSON file
        data = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "rounds":self.get_rounds_dict(),
                # [self._round_to_dict(rnd) for rnd in self.rounds]
            "registered_players": self.get_reg_player_dict()
        }
        os.makedirs('resources/tournaments', exist_ok=True)
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(data, file, indent=4)
            print("Tournament details saved successfully!")

    def load(self):
        if os.path.exists(f"resources/tournaments/{self.name}.json"):
            with open(f"resources/tournaments/{self.name}.json", "r") as file:
                details = json.load(file)
                self.__set_attributes(details)
                self.rounds = []
                self.registered_players = []
                for round in details["rounds"]:
                    round_matches = []
                    for match in round["rnd_matches"]:
                        player1 = match[0]
                        player2 = match[1]
                        player1 = Player(dictionary = player1)
                        # the dictionary is going to be "player1" instead of None to run the __set_attributes into player.py to transform player inscription dictionary details into class object.
                        player2 = Player(dictionary = player2)
                        match = Match(player1, player2)
                        round_matches.append(match)
                    round["rnd_matches"] = round_matches
                    round = Round(dictionary = round)
                    self.rounds.append(round)
                for player in details["registered_players"]:
                    # print("///")
                    # print(player)
                    new_player = Player(dictionary = player)
                    self.registered_players.append(new_player)
            return True
        else:
            return False

    def register_player(self,details):
        new_player = Player(dictionary = details)
        self.registered_players.append(new_player)
        # self.add_player_to_file(new_player)
        self.save()

    def set_total_nbr_rounds(self):
        number_of_players = len(self.registered_players)
        self.number_of_rounds = int(math.log2(number_of_players))
        self.end_date = (datetime.now()+timedelta(days = self.number_of_rounds)).strftime("%Y-%m-%d %H:%M:%S")
        self.save()
            
    def generate_round(self):
        # Generate matches for the next round
        self.current_round += 1
        if self.current_round == 1:
            self.current_players = deepcopy(self.registered_players)
            # print("I am here")
        else :
            self.current_players = deepcopy(self.current_players)
        round_name = f"Round {self.current_round}"
        start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        end_date_time = (datetime.now()+timedelta(days = 1)).strftime("%Y-%m-%d %H:%M:%S")
        current_round = Round(round_name, start_date_time, end_date_time)
        current_round.set_matches(self.current_players, self.current_round)
        self.rounds.append(current_round)

    def start_round(self):
        self.current_players = self.rounds[self.current_round - 1].check_round_winners()
        self.save()
        return len(self.current_players), self.current_players

    def reset_rounds(self):
        self.rounds = []
        self.current_round = 0
        self.save()

    def get_reg_player_ids(self):
        ids = []
        for player in self.registered_players:
            ids.append(player.national_chess_id)
        return  ids