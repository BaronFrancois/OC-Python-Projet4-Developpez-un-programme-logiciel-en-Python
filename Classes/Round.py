import random


class Round:
    def __init__ (self, rnd_name, rnd_start_datetime, rnd_end_datetime ):
        self.rnd_name = rnd_name
        self.rnd_start_datetime = rnd_start_datetime
        self.rnd_end_datetime = rnd_end_datetime
        self.rnd_matches = []

    # function = set_match
    def set_match (self,players, previous_round_winners=None):
        # for first round : random 
        if previous_round_winners is None :
            random.shuffle(players)
            self.rnd_matches = [(player[i], player[i+1]) for i in range(0, len(players),2)]
            
        else:
            # Next rounds: pair winners of previous round randomly
            random.shuffle(previous_round_winners)
            self.rnd_matches = [(previous_round_winners[i], previous_round_winners[i + 1]) for i in range(0, len(previous_round_winners), 2)]
