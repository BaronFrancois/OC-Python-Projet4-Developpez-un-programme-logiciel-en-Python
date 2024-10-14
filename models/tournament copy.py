import os
import json
import math
from models.player import Player
from models.round import Round
from models.match import Match
import random
from datetime import datetime


class Tournament:
    def __init__(
        self, name, location, start_date, end_date, description, number_of_rounds=4
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round_number = 0
        self.rounds = []
        self.registered_players = []
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_players = []

    def __str__(self):
        details = (
            f"name:{self.name}, start_date:{self.start_date}, end_date:{self.end_date}"
        )
        return details

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
            "description": self.description,
        }
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(details, file, indent=4)
            print("New tournament saved succesfully !")

    def load_data(self):
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

    def register_player(
        self, chess_id, last_name, first_name, birthday, country, club_name
    ):
        is_verified_player = self.verify_player(chess_id, country, club_name)
        if is_verified_player:
            new_player = Player(last_name, first_name, birthday, chess_id)
            self.registered_players.append(new_player)
            self.add_player_to_file(new_player)
        else:
            print("player is not verified")

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

    def set_total_nbr_rounds(self):
        number_of_players = len(self.registered_players)
        self.number_of_rounds = int(math.log2(number_of_players))

    def generate_round(self):
        self.current_round_number += 1
        if self.current_round_number == 1:
            self.current_players = self.registered_players
        # print("generate round function", self.current_players)
        round_name = "Round " + str(self.current_round_number)
        print(round_name)
        start_date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        current_round = Round(round_name, start_date_time)
        current_round.set_matches(self.current_players, self.current_round_number)
        self.rounds.append(current_round)
        
    
        
# ----- 10/09/2024 first generate and then (round end time =/= None)
# check plyr_score first match within the round
# sum(score_plyr1 + score_plyr2) == 1
    def start_round(self):
        # self.rounds[self.current_round_number - 1].start_matches()
        self.rounds[
            self.current_round_number - 1
        ].rnd_end_datetime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.current_players = self.rounds[self.current_round_number - 1].check_round_winners()
        return len(self.current_players), self.current_players
        
    def add_rounds_to_file(self):
        with open(f"resources/tournaments/{self.name}.json", "r") as file:
            tournament = json.load(file)
        # for round in self.rounds:
        round = self.rounds[self.current_round_number -1]
        tournament_round = {
            "rnd_name": round.rnd_name,
            "rnd_start_datetime": round.rnd_start_datetime,
            "rnd_end_datetime": round.rnd_end_datetime,
        }
        tournament_round_matches = []
        # print(len(round.rnd_matches))
        for match in round.rnd_matches:
            round_match = [
                {
                    "last_name": match.player1.last_name,
                    "first_name": match.player1.first_name,
                    "date_of_birth": match.player1.date_of_birth,
                    "national_chess_id": match.player1.national_chess_id,
                    "plyr_score": match.player1.plyr_score,
                    "has_lost": match.player1.has_lost,
                },
                {
                    "last_name": match.player2.last_name,
                    "first_name": match.player2.first_name,
                    "date_of_birth": match.player2.date_of_birth,
                    "national_chess_id": match.player2.national_chess_id,
                    "plyr_score": match.player2.plyr_score,
                    "has_lost": match.player2.has_lost,
                },
            ]
            tournament_round_matches.append(round_match)
        tournament_round["rnd_matches"] = tournament_round_matches
        tournament["rounds"].append(tournament_round)
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(tournament, file, indent=4)
    def reset_rounds(self):
        self.rounds = []        
        with open(f"resources/tournaments/{self.name}.json", "r") as file:
            tournament = json.load(file)
        tournament["rounds"]= []
        with open(f"resources/tournaments/{self.name}.json", "w") as file:
            json.dump(tournament, file, indent=4)