from classes.player import Player

def test_player_creation ():
    player1 = Player("smith","bob","02/02/02","ab12345")
    assert player1.last_name == "smith"
    assert player1.first_name == "bob"
    assert player1.date_of_birth == "02/02/02"
    assert player1.national_chess_id == "ab12345"
