from views.tournament_view import View
from models.tournament import Tournament
from utils.report_util import ReportUtil
from utils.error_util import ErrorType, ResultType
from models.club import Club
from datetime import datetime, timedelta
import json
import glob
import os



class TournamentController:
    def __init__(self):
        # Initialize the tournament attribute
        self.tournament = None
        self.club_details = Club()
    
    def load (self, name):
        # Load tournament data from a JSON file based on the tournament name.
        self.tournament = Tournament(name, None, None, None, None)
        is_data_loaded = self.tournament.load()
        if not is_data_loaded:
            self.tournament = None
            return False
        return True
    
    def remove_option_and_tournament(self, details):
        if details and "option_number" in details:
            details.pop("option_number")
        if details and "tournament" in details:
            details.pop("tournament")
        return details
    
    def pause(self,option_number,details):
        details["option_number"] = option_number
        if self.tournament:
            details["tournament"] = self.tournament.name
        self.save_backup(details)
        
    def create_tournament(self, details = None, option_number = None):
        # Create a new tournament using user-provided details.
        details = self.remove_option_and_tournament(details)
        details = View.create_tournament(details)
        if "0" in details.values():
            self.pause(option_number, details)
            return ResultType.PAUSED
        
        file_path = f'resources/tournaments/{details["name"]}.json'
        if os.path.exists(file_path):
            print("ERROR:",ErrorType.TMT_ALREADY_EXISTS )
            return ResultType.ERROR 
        else:
            details["start_date"] = datetime.strptime(details["start_date"],"%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")
            self.tournament = Tournament(dictionary = details)
            print(self.tournament.name, self.tournament.location)
            self.tournament.save()
            return ResultType.SUCCES 
            
        # Create and save the tournament
        
    # Register a player to the tournament.
        
    def register_player(self, details= None, option_number = None):
        details = self.remove_option_and_tournament(details)
        details = View.register_player(details)
        if "0" in details.values():
            self.pause(option_number, details)
            return ResultType.PAUSED
        
        is_result_valid = self.club_details.check_valid_player(details)
        if is_result_valid  == ErrorType.NO_ERROR:
            if details["national_chess_id"] in self.tournament.get_reg_player_ids():
                print("Player is already registered")
            else:
                self.tournament.register_player(details)
            return ResultType.SUCCES
            
        else:
            print("ERROR:",is_result_valid)
            return ResultType.ERROR
            
        
        
    def save_backup(self,data):
        # Assurer que le répertoire existe
        os.makedirs("resources", exist_ok=True)
        with open("resources/resume_file.json", "w") as file:
            json.dump(data, file, indent=4) 
    # Start the tournament and handle the rounds and matches.
    def start_tournament(self, details = None, option_number = None):
        self.tournament.reset_rounds()
        self.tournament.set_total_nbr_rounds()
        
        # Iterate through each round
        for round in range(self.tournament.number_of_rounds):
            self.tournament.generate_round()
            View.show_round_details(self.tournament.rounds[round])
            for match in self.tournament.rounds[round].rnd_matches:
                    # Prompt the user for the match result
                ask_result = View.ask_match_result(match.player1,match.player2)
                # print("before",[player.__dict__ for player in self.tournament.registered_players])        
                # Update the match based on the result        
                match.play(ask_result)
                # print("after",[player.__dict__ for player in self.tournament.registered_players])
                # print(match.player1.first_name,match.player1.plyr_score, "//" ,match.player2.first_name,match.player2.plyr_score)
            number_of_winners, winners = self.tournament.start_round()
            # self.tournament.add_rounds_to_file()
            if number_of_winners == 1:
                View.show_winner(winners)
                break
            print("no final winner yet")
        return True
    def find_longest(self,object_list,attribute =None):
        def get_attribute_len(obj):
            value = getattr(obj,attribute)
            lenght = len(value)
            return lenght
        longest_object = max(object_list,key=get_attribute_len)
        value = getattr(longest_object,attribute)
        longest_str = max(len(value),len(attribute))
        return longest_str
    def add_report_headings(self,headers):
        report = []
        row = "" 
        for header, spacing in headers.items():
            header = header.replace("_"," ").title()
            row += f" | {header:<{spacing}}"
        row += " |"
        report.append(row)
        row = ""
        for header, spacing in headers.items():
            row += f" | {"_"*spacing}"
        row += " |"
        report.append(row)
        return report  
    def sort_players(self,players,attribute):
        def get_attribute(player):
            value = getattr(player,attribute)
            return value
        sorted_players = sorted(players,key=get_attribute)
        return sorted_players
    def save_report_to_txt(self,report,file_name):
        with open(f"resources/reports/{file_name}.txt","w") as file:
            for line in report:
                file.write(line+"\n")
            print("report has been generated")
    def show_all_clubs_players(self,details = None, option_number = None):
        return self.show_all_players(self.club_details.players,"all_players_report")
    def show_all_players(self,players,file_name):
        sorted_players = self.sort_players(players, attribute = "last_name")
        headers = {"national_chess_id": None,
                   "last_name":None,
                   "first_name" : None,
                   "federation":None,
                   "club_name":None
                   }
        self.prepare_report(headers,sorted_players,file_name)
        return ResultType.SUCCES 
    def prepare_report(self,headers,obj_list,file_name):   
        for header in headers:
            headers[header] = self.find_longest(obj_list,attribute = header)
        # print(headers)
        
        report = self.add_report_headings(headers)
        # print(report)
        for obj in obj_list:
            row = "" 
            for header, spacing in headers.items():
                value = getattr(obj,header)
                row += f" | {value:<{spacing}}"
            row += " |"
            report.append(row)
        View.show_report(report)
        save_report = View.ask_for_report()
        if save_report:
            self.save_report_to_txt(report,file_name = file_name)
        
    # Display all tournaments and optionally generate a report.
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
        return self.show_tournaments (tournaments,"all_tournaments_report")
        
    def show_tournaments(self,tournaments,file_name):
        headers = {"name": None,
                    "location": None,
                    "start_date": None,
                    "end_date": None,
                    "description":None,
                    # "number_of_rounds":None
                   }
        self.prepare_report(headers,tournaments,file_name)
        return ResultType.SUCCES 
        
            
    # Search for a particular tournament and display its details.
    def show_particular_tournament(self,details = None, option_number = None):
        file_name = f"{self.tournament.name}_report"
        return self.show_tournaments ([self.tournament],file_name)
        
    
    # Display all players registered in a particular tournament.
    def show_tournament_players(self,details = None, option_number = None):
        file_name = f"{self.tournament.name}_reg_players_report"
        return self.show_all_players(self.tournament.registered_players,file_name)
        
        
    # Display all rounds and matches in the tournament.
    def show_tournament_report(self, details = None, option_number = None):
        longest_first_name = longest_last_name = 0
        for round in self.tournament.rounds:
            View.show_tournament_round(
                round.rnd_name, round.rnd_start_datetime, round.rnd_end_datetime
            )
            for match in round.rnd_matches:
                View.show_round_matches(match.player1, match.player2)
                # Update the maximum lengths for formatting
                longest_first_name = max(longest_first_name,len(match.player1.first_name),len(match.player2.last_name))
                longest_last_name = max(longest_last_name,len(match.player1.last_name),len(match.player2.last_name))
                
        ask_report = View.ask_for_report()
        if ask_report:
            # Generate a report
            report = []
            report.append(f'| Round n | {"Round SD":<{20}} | {"Round ED":<{20}} | P1 Chess Id | {"P1 LN":<{longest_last_name}} | {"P1 FN":{longest_first_name}} | {"P1 Score":<{7}} | P2 Chess Id | {"P2 LN":<{longest_last_name}} | {"P2 FN":{longest_first_name}} | {"P2 Score":<{8}} | \n')
            report.append(f'| {"_"*(7)} | {"_"*(20)} | {"_"*(20)} | {"_"*(11)} | {"_"*(longest_last_name)} | {"_"*(longest_first_name)} | {"_"*(8)} | {"_"*(11)} | {"_"*(longest_last_name)} | {"_"*(longest_first_name)} | {"_"*(8)} | \n')
            for round in self.tournament.rounds :
                for match in round.rnd_matches :
                    report.append(f'| {round.rnd_name:<{7}} | {round.rnd_start_datetime:<{20}} | {round.rnd_end_datetime:<{20}} | {match.player1.national_chess_id:<{11}} | {match.player1.last_name:<{longest_last_name}} | {match.player1.first_name:{longest_first_name}} | {match.player1.plyr_score:<{8}} | {match.player2.national_chess_id :<{11}} | {match.player2.last_name:<{longest_last_name}} | {match.player2.first_name:{longest_first_name}} | {match.player2.plyr_score:<{8}} | \n')
            # Write the report to a file
            with open(f"resources/reports/rounds_&_matches_{self.tournament.name}_report.txt","w") as file:
                file.writelines(report) 
                print(f"{self.tournament.name}'s rounds and matches report has been generated")
        return True