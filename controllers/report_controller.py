from utils.report_util import Report
from utils.error_util import ResultType

class ReportController:
    def __init__(self):
        pass
    
                
    def sort_players(self,players,attribute):
        def get_attribute(player):
            value = getattr(player,attribute)
            return value
        sorted_players = sorted(players,key=get_attribute)
        return sorted_players
    
    # options 2,3,6,7,8
    
    def show_all_players(self,players,file_name):
        sorted_players = self.sort_players(players, attribute = "last_name")
        headers = {"national_chess_id": None,
                "last_name":None,
                "first_name" : None,
                "federation":None,
                "club_name":None
                }
        Report.prepare(headers,sorted_players,file_name)
        return ResultType.SUCCES 
    
    def show_tournaments(self,tournaments,file_name):
        headers = {"name": None,
                    "location": None,
                    "start_date": None,
                    "end_date": None,
                    "description":None,
                    # "number_of_rounds":None
                }
        Report.prepare(headers,tournaments,file_name)
        return ResultType.SUCCES
    
    def show_rounds_and_matches(self,rounds,file_name):
        headers = {}
        for key in rounds[0].keys():
            headers[key] = None,
        Report.prepare(headers,rounds,file_name) 
        return ResultType.SUCCES