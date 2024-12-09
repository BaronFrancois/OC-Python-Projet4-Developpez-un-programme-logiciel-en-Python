from models.club import Club

class DataController:
    def __init__(self):
        self.tournament = None
        self.club_details = Club()
        
    # remove_option_and_tournament <-before
    def clean_details(self, details):
        if details and "option_number" in details:
            details.pop("option_number")
        if details and "tournament" in details:
            details.pop("tournament")
        return details