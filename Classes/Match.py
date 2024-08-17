class Match:
    def __init__(self, player1, player2, score1=0.0, score2=0.0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def set_scores(self, score1, score2):
            self.score1 = score1
            self.score2 = score2