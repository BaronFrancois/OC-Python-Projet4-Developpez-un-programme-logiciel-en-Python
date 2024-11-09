

class ErrorType:
    COUNTRY_MISMATCH = "Country name does not match"
    CLUB_MISMATCH = "Club name does not match"
    PLAYER_ID_MISMATCH = "Player id does not match"
    INVALID_CHESS_ID = "Invalid Chess Id format (AB12345)"
    PLAYER_FIRST_NAME_MISMATCH = "The Player First name is not matching"
    PLAYER_LAST_NAME_MISMATCH = "The Player Last name is not matching"
    PLAYER_BIRTHDAY_MISMATCH = "The Player Birthday is not matching"
    PLAYER_FED_MISMATCH = "The player's federation is not matching"
    NO_ERROR = "No error found"
    
    TMT_ALREADY_EXISTS = "The tournament already exists"
    
    
class ResultType:
    SUCCES = "Succes"
    PAUSED = "Paused"
    ERROR = "Error"