import random
from models.match import Match


class Round:
    def __init__ (self, rnd_name, rnd_start_datetime, rnd_end_datetime=None ):
        self.rnd_name = rnd_name
        self.rnd_start_datetime = rnd_start_datetime
        self.rnd_end_datetime = rnd_end_datetime
        self.rnd_matches = []

    def set_matches (self,players, current_round_number):
        if current_round_number == 1 :
            random.shuffle(players)
            for p in range (0,len(players)-1,2):
                player1 = players[p]
                player2 = players[p+1]
                current_match = Match(player1,player2)
                self.rnd_matches.append(current_match)
            
        else:
            pass
    
    def start_matches(self):
        for match in self.rnd_matches:
            match.play()
        