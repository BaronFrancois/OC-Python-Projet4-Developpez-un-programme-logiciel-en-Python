import os
import json
import math
from datetime import datetime
from models.player import Player
from models.round import Round
from models.match import Match

class Tournament:
    def __init__(self, name, location, start_date, end_date, description, number_of_rounds=4):
        # Initialize a tournament with its details
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round_number = 0
        self.rounds = []
        self.registered_players = []
        self.current_players = []

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
            "current_round": self.current_round_number,
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
                self.name = details["name"]
                self.location = details["location"]
                self.start_date = details["start_date"]
                self.end_date = details["end_date"]
                self.number_of_rounds = details["number_of_rounds"]
                self.current_round_number = details["current_round"]
                self.rounds = []
                #    self.registered_players = details["registered_players"]
                # player is a dictionnary
                # print("loading data")
                for round in details["rounds"]:
                    round_matches = []
                    for match in round["rnd_matches"]:
                        player1 = match[0]
                        player2 = match[1]
                        #    print(player1)
                        #    print(player2)

                        player1 = Player(
                            player1["last_name"],
                            player1["first_name"],
                            player1["date_of_birth"],
                            player1["national_chess_id"],
                            player1["plyr_score"],
                            player1["has_lost"],
                        )

                        player2 = Player(
                            player2["last_name"],
                            player2["first_name"],
                            player2["date_of_birth"],
                            player2["national_chess_id"],
                            player2["plyr_score"],
                            player2["has_lost"],
                        )

                        match = Match(player1, player2)
                        round_matches.append(match)

                    round = Round(
                        round["rnd_name"],
                        round["rnd_start_datetime"],
                        round["rnd_end_datetime"],
                        round_matches,
                    )
                    self.rounds.append(round)

                for player in details["registered_players"]:
                    new_player = Player(
                        player["last_name"],
                        player["first_name"],
                        player["date_of_birth"],
                        player["national_chess_id"],
                    )
                    self.registered_players.append(new_player)

                self.description = details["description"]
            return True
        else:
            return False

    def register_player(self,details):
        new_player = Player(details["last_name"],
                            details["first_name"],
                            details["birthday"],
                            details["chess_id"]
                            )
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
        player = {
            "national_chess_id": new_player.national_chess_id,
            "last_name": new_player.last_name,
            "first_name": new_player.first_name,
            "date_of_birth": new_player.date_of_birth,
        }

        with open(f"resources/tournaments/{self.name}.json", "r") as file:
            tournament = json.load(file)
            # print(tournament)
        tournament["registered_players"].append(player)
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(tournament, file, indent=4)
            print("New player saved succesfully !")
    def generate_round(self):
        # Generate matches for the next round
        self.current_round_number += 1
        if self.current_round_number == 1:
            self.current_players = self.registered_players.copy()
        round_name = f"Round {self.current_round_number}"
        start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_round = Round(round_name, start_date_time)
        current_round.set_matches(self.current_players, self.current_round_number)
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
        self.current_round_number = 0
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