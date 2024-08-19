from classes.match import Match
from classes.player import Player

def test_match_creation ():
    player1 = Player("smith","bob","02/02/02","ab12345")
    player2 = Player("cruise","tom","03/03/03","ab23456")
    match1 = Match(player1,player2)
    assert match1.player1.first_name == "bob"
    assert match1.player2.first_name == "tom"

def test_play_match ():
    player1 = Player("smith","bob","02/02/02","ab12345")
    player2 = Player("cruise","tom","03/03/03","ab23456")
    match1 = Match(player1,player2)
    match1.play()
    assert match1.player1.plyr_score + match1.player2.plyr_score == 1
