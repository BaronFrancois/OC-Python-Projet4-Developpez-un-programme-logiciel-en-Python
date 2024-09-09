import random
# from player import Player

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def play(self):
        score1 = random.choice([0,0.5,1])
        score2 = 1-score1 
        if score1 == 0:
            self.player1.has_lost = True
        elif score2 == 0:
            self.player2.has_lost = True
        self.player1.plyr_score += score1
        self.player2.plyr_score += score2


