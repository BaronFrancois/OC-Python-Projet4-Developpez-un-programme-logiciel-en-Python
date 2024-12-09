# import random
# from player import Player

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def play(self, ask_result):
        # Using player 1 has reference :
            # input== 1 player 1 wins, input == 2 player 2 wins
        score1 = None
        if ask_result == 1:
            score1 = 1
        elif  ask_result == 2:
            score1 = 0
        # if player 1 wins = score2 = 1-1 =0
        # if player 2 wins = score2 = 1-0 =1
        score2 = 1-score1 
        if score1 == 0 or score2 == 0 :
            # update the score of the player
            self.player1.plyr_score += score1
            self.player2.plyr_score += score2
            if score1 == 0:
                self.player1.has_lost = True
            elif score2 == 0:
                self.player2.has_lost = True