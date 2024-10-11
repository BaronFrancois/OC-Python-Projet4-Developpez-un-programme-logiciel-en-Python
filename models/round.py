import random
from models.match import Match


class Round:
    def __init__ (self, rnd_name, rnd_start_datetime, rnd_end_datetime=None,rnd_matches= [] ):
        self.rnd_name = rnd_name
        self.rnd_start_datetime = rnd_start_datetime
        self.rnd_end_datetime = rnd_end_datetime
        self.rnd_matches = rnd_matches

    def set_matches (self,players, current_round_number):
        self.rnd_matches= []
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
                # if player.has_lost == False:
                # if not player.has_lost:
                sorted_player[player]= player.plyr_score
            # def get_value(item):   -> lamda
            #     return item[1]        
            sorted_player =dict(sorted(sorted_player.items(), key = lambda item:item[1] )) 
            # print("sorted player", sorted_player)
            sorted_player = list(sorted_player.keys())
            # update player_list

            for i in range(0, len(sorted_player)-1, 2):
                player1 = sorted_player[i]
                player2 = sorted_player[i + 1]
                current_match = Match(player1, player2)
                self.rnd_matches.append(current_match)
    
    def check_round_winners(self):
        players = []
        for match in self.rnd_matches:
            if not match.player1.has_lost:
                players.append(match.player1)
            if not match.player2.has_lost:
                players.append(match.player2)
        # for player in players:
        #     print(player.first_name)
        return players
    # def start_matches(self):
    #     for match in self.rnd_matches:
    #         match.play()       
