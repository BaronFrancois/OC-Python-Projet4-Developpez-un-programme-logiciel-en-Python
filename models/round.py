import random
from models.match import Match


class Round:
    def __init__ (self, rnd_name, rnd_start_datetime, rnd_end_datetime=None,rnd_matches= [] ):
        self.rnd_name = rnd_name
        self.rnd_start_datetime = rnd_start_datetime
        self.rnd_end_datetime = rnd_end_datetime
        self.rnd_matches = rnd_matches

    def set_matches (self,players, current_round_number):
        if current_round_number == 1 :
            random.shuffle(players)
            for p in range (0,len(players)-1,2):
                player1 = players[p]
                player2 = players[p+1]
                current_match = Match(player1,player2)
                self.rnd_matches.append(current_match)
        # implement : sort the players from their scores
        # Use a loop set matches 2 players

        else:
            sorted_player = {}
            for player in players:
                if player.has_lost == False:
                    sorted_player[player.plyr_score]= player
                
            sorted_player =dict(sorted(sorted_player.items())) 
            sorted_player = list(sorted_player.values())
            # update player_list

            for i in range(0, len(sorted_player)-1, 2):
                player1 = sorted_player[i]
                player2 = sorted_player[i + 1]
                current_match = Match(player1, player2)
                self.rnd_matches.append(current_match)
    
    def start_matches(self):
        for match in self.rnd_matches:
            match.play()
            print(match.player1.first_name,match.player1.plyr_score, "///VS///" ,match.player2.first_name,match.player2.plyr_score)
