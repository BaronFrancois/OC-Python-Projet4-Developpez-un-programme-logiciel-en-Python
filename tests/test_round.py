import sys
from datetime import datetime
sys.path.append('models')
from models.match import Match
from models.player import Player
from models.round import Round

def test_init ():
    start_date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    end_date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    round1 = Round("Round1", start_date_time,end_date_time )
    assert round1.rnd_name == "Round1"
    assert round1.rnd_start_datetime == start_date_time
    assert round1.rnd_end_datetime == end_date_time
    assert round1.rnd_matches == []

def test_set_matches():
    # create list of 4 players, send the list. test it for rnd n1 and then n2. Call the function set_matches = if self.rnd_matches.()
    pass