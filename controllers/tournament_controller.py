from views.tournament_view import View
from datetime import datetime, timedelta
from utils.error_util import ErrorType, ResultType
from utils.backup_util import Backup
from models.tournament import Tournament
from views.round_view import RoundView
from controllers.data_controller import DataController

import os

class TournamentController(DataController):
    def __init__(self):
        DataController.__init__(self)
    
    def create_tournament(self, details = None, option_number = None):
        # Create a new tournament using user-provided details.
        details = self.clean_details(details)
        details = View.create_tournament(details)
        if "0" in details.values():
            Backup.pause(option_number, details, self.tournament)
            return ResultType.PAUSED
        
        file_path = f'resources/tournaments/{details["name"]}.json'
        if os.path.exists(file_path):
            print("ERROR:",ErrorType.TMT_ALREADY_EXISTS )
            return ResultType.ERROR 
        else:
            start_date = datetime.strptime(details["start_date"],"%d/%m/%Y")
            details["start_date"] = start_date.strftime("%Y-%m-%d %H:%M:%S")
            details["end_date"] = (start_date+timedelta(days = 7)).strftime("%Y-%m-%d %H:%M:%S")
            self.tournament = Tournament(dictionary = details)
            # print(self.tournament.name, self.tournament.location)
            self.tournament.save()
            return ResultType.SUCCES    
    # Register a player to the tournament.
                
    # Start the tournament and handle the rounds and matches.
    def start_tournament(self, details = None, option_number = None):
        self.tournament.reset_rounds()
        self.tournament.set_total_nbr_rounds()
        
        # Iterate through each round
        for round in range(self.tournament.number_of_rounds):
            self.tournament.generate_round()
            RoundView.show_round_details(self.tournament.rounds[round])
            for match in self.tournament.rounds[round].rnd_matches:
                    # Prompt the user for the match result
                ask_result = RoundView.ask_match_result(match.player1,match.player2)     
                match.play(ask_result)
            number_of_winners, winners = self.tournament.start_round()
            if number_of_winners == 1:
                View.show_winner(winners[0].first_name)
                break
            else:
                View.show_not_final_winner()
        return ResultType.SUCCES
