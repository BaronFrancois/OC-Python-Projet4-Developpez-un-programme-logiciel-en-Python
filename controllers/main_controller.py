from controllers.report_controller import ReportController
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from models.tournament import Tournament
from models.club import Club

import glob
import os

class MainController:
    def __init__(self):
        # Initialize the tournament attribute
        self.tournament = None
        self.club_details = Club()
        self.report_controller = ReportController()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
    
    def load (self, name):
        # Load tournament data from a JSON file based on the tournament name.
        self.tournament = Tournament(name, None, None, None, None)
        is_data_loaded = self.tournament.load()
        if not is_data_loaded:
            self.tournament = None
            return False
        return True

    def create_tournament(self, details = None, option_number = None):
        return self.tournament_controller.create_tournament(details, option_number)
    
    def start_tournament(self, details = None, option_number = None):
        self.tournament_controller.tournament = self.tournament
        return self.tournament_controller.start_tournament(details, option_number)
    
    def register_player(self, details= None, option_number = None):
        self.player_controller.tournament = self.tournament
        return self.player_controller.register_player(details,option_number)

    def show_all_clubs_players(self,details = None, option_number = None):
        return self.report_controller.show_all_players(self.club_details.players,"all_players_report")

    # Display all tournaments and optionally generate a report
    def show_all_tournaments(self, details = None, option_number = None):
        path = os.path.join("resources/tournaments", "*.json")
        file_names = glob.glob(path)
        # print(file_names)
        tournaments = []
        for file_name in file_names:
            file_name = file_name.replace("resources/tournaments\\", "").replace(".json", "")
            # print(file_name)
            
            self.load(file_name)
            tournaments.append(self.tournament)
        return self.report_controller.show_tournaments (tournaments,"all_tournaments_report")

    # Search for a particular tournament and display its details.
    def show_particular_tournament(self,details = None, option_number = None):
        file_name = f"{self.tournament.name}_report"
        return self.report_controller.show_tournaments ([self.tournament],file_name)
        
    # Display all players registered in a particular tournament.
    def show_tournament_players(self,details = None, option_number = None):
        file_name = f"{self.tournament.name}_reg_players_report"
        return self.report_controller.show_all_players(self.tournament.registered_players,file_name)
        
    # Display all rounds and matches in the tournament.
    def show_tournament_report(self, details = None, option_number = None):
        rounds = self.tournament.get_flat_rounds_dict()
        file_name = f"rounds_&_matches_{self.tournament.name}_report"
        return self.report_controller.show_rounds_and_matches(rounds,file_name)
