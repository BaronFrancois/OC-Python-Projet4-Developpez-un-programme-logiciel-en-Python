import os
import json
import math
from datetime import datetime
from models.player import Player
from models.round import Round
from models.match import Match

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
            # print(key, value)
   
    def __str__(self):
        # Return a string representation of the tournament
        return f"Tournament '{self.name}' from {self.start_date} to {self.end_date}"

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
            "rounds": [self._round_to_dict(rnd) for rnd in self.rounds],
            "registered_players": [self._player_to_dict(p) for p in self.registered_players],
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
                # print("details",details["registered_players"])
                # print("len",len(details["registered_players"]))
                # print("datatype",type(details["registered_players"][0]))
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
        self.add_player_to_file(new_player)

    def verify_player(self, chess_id, country, club_name):
        with open("resources/clubs.json", "r") as file:
            details = json.load(file)
            fed = details["federations"]
            for f in fed:
                if f["country"] == country:
                    clubs = f["clubs"]
                    for club in clubs:
                        if club["club_name"] == club_name:
                            players = club["players"]
                            for player in players:
                                if player["national_chess_id"] == chess_id:
                                    return True
        return False

    def add_player_to_file(self, new_player):
        # player = {
        #     "national_chess_id": new_player.national_chess_id,
        #     "last_name": new_player.last_name,
        #     "first_name": new_player.first_name,
        #     "date_of_birth": new_player.date_of_birth,
        #         }
        player = new_player.__dict__
        

        with open(f"resources/tournaments/{self.name}.json", "r") as file:
            tournament = json.load(file)
            # print(tournament)
        tournament["registered_players"].append(player)
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(tournament, file, indent=4)
            print("New player saved succesfully !")
    def generate_round(self):
        # Generate matches for the next round
        self.current_round += 1
        if self.current_round == 1:
            self.current_players = self.registered_players.copy()
        round_name = f"Round {self.current_round}"
        start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_round = Round(round_name, start_date_time)
        current_round.set_matches(self.current_players, self.current_round)
        self.rounds.append(current_round)

    def start_round(self):
        # Start the current round and update the tournament stats
        current_round = self.rounds[-1]
        # Play each match in the round
        for match in current_round.rnd_matches:
            match.play()
        # Update current players based on match results
        self.current_players = current_round.check_round_winners()
        # Set the end time for the round
        current_round.rnd_end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save()

    def reset_rounds(self):
        # Reset the rounds of the tournament
        self.rounds = []
        self.current_round = 0
        self.save()

    def _player_to_dict(self, player):
        # Convert a Player object to a dictionary for serialization
        return {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "date_of_birth": player.date_of_birth,
            "national_chess_id": player.national_chess_id,
            "plyr_score": player.plyr_score,
            "has_lost": player.has_lost,
        }

    def _dict_to_player(self, data):
        # Create a Player object from a dictionary
        return Player(
            data["last_name"],
            data["first_name"],
            data["date_of_birth"],
            data["national_chess_id"],
            data.get("plyr_score", 0),
            data.get("has_lost", False),
        )

    def _round_to_dict(self, rnd):
        # Convert a Round object to a dictionary for serialization
        return {
            "rnd_name": rnd.rnd_name,
            "rnd_start_datetime": rnd.rnd_start_datetime,
            "rnd_end_datetime": rnd.rnd_end_datetime,
            "rnd_matches": [self._match_to_dict(m) for m in rnd.rnd_matches],
        }

    def _dict_to_round(self, data):
        # Create a Round object from a dictionary
        rnd = Round(
            data["rnd_name"],
            data["rnd_start_datetime"],
            data["rnd_end_datetime"],
        )
        rnd.rnd_matches = [self._dict_to_match(m) for m in data["rnd_matches"]]
        return rnd

    def _match_to_dict(self, match):
        # Convert a Match object to a dictionary for serialization.
        return {
            "player1": self._player_to_dict(match.player1),
            "player2": self._player_to_dict(match.player2),
        }

    def _dict_to_match(self, data):
        # Create a Match object from a dictionary
        player1 = self._dict_to_player(data["player1"])
        player2 = self._dict_to_player(data["player2"])
        return Match(player1, player2)
    
    def get_reg_player_ids(self):
        ids = []
        for player in self.registered_players:
            ids.append(player.national_chess_id)
        return  ids