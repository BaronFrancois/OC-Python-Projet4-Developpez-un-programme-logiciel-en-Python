import sys
sys.path.append('models')
from models.player import Player


def test_player_creation ():
    player1 = Player("smith","bob","02/02/02","ab12345")
    assert player1.last_name == "smith"
    assert player1.first_name == "bob"
    assert player1.date_of_birth == "02/02/02"
    assert player1.national_chess_id == "ab12345"
    assert player1.plyr_score == 0
    assert player1.has_lost == False
    
def test_player_creation2 ():
    player1 = Player("smith","bob","02/02/02","ab12345", 2, True)
    assert player1.last_name == "smith"
    assert player1.first_name == "bob"
    assert player1.date_of_birth == "02/02/02"
    assert player1.national_chess_id == "ab12345"
    assert player1.plyr_score == 2
    assert player1.has_lost == True
