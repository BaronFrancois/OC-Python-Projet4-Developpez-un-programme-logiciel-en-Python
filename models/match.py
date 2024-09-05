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
    # def set_scores(self, score1, score2):
    #         self.score1 = score1
    #         self.score2 = score2


# player1 = Player("smith","bob","02/02/02","ab12345")
# player2 = Player("cruise","tom","03/03/03","ab23456")
# match1 = Match(player1,player2)
# match1.play()
# print(match1.player1.plyr_score, match1.player2.plyr_score)

