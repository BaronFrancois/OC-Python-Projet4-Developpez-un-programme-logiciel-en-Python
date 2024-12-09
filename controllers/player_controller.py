from views.tournament_view import View
from utils.backup_util import Backup
from utils.error_util import ResultType, ErrorType
from controllers.data_controller import DataController

class PlayerController(DataController):
    def __init__(self):
        DataController.__init__(self)
        
    def register_player(self, details= None, option_number = None):
        details = self.clean_details(details)
        details = View.register_player(details)
        if "0" in details.values():
            Backup.pause(option_number, details, self.tournament)
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