import random
# from player import Player

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def play(self):
        self.player1.plyr_score = random.choice([1,0,0.5])
        self.player2.plyr_score = 1-self.player1.plyr_score
    # def set_scores(self, score1, score2):
    #         self.score1 = score1
    #         self.score2 = score2


# player1 = Player("smith","bob","02/02/02","ab12345")
# player2 = Player("cruise","tom","03/03/03","ab23456")
# match1 = Match(player1,player2)
# match1.play()
# print(match1.player1.plyr_score, match1.player2.plyr_score)

