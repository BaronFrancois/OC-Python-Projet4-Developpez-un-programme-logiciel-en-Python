from views.registration_view import *
from models.tournament import Tournament




class TournamentController:
    def __init__ (self):
        self.tournament = None

    def load_tournament_data (self):
        self.tournament = Tournament(None,None,None,None,None)
        is_data_loaded = self.tournament.load_data()
        if not is_data_loaded :
            self.tournament = None

    
    def create_tournament (self):
        tmt_name,tmt_location,tmt_start_date, tmt_end_date,tmt_description = create_tournament_view()
        self.tournament = Tournament(tmt_name,tmt_location,tmt_start_date, tmt_end_date,tmt_description)
        self.tournament.save_tournament_details()
        

    def register_player(self):
        chess_id, last_name, first_name, birthday, country,club_name = register_player_view()
        self.tournament.register_player(chess_id, last_name, first_name, birthday, country, club_name)

    def start_tournament(self):
        self.tournament.set_total_nbr_rounds()
        self.tournament.generate_round()