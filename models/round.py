import random
from models.match import Match


class Round:
    def __init__ (self, rnd_name=None, rnd_start_datetime=None, rnd_end_datetime=None,rnd_matches= [], dictionary = None ):
        self.rnd_name = rnd_name
        self.rnd_start_datetime = rnd_start_datetime
        self.rnd_end_datetime = rnd_end_datetime
        self.rnd_matches = rnd_matches
        # as Player.py, set_attributes convert dictionnary data (if there is) key , value into the Round object
        if dictionary:
            self.__set_attributes(dictionary)
            
    def __set_attributes(self,dictionary):
        #  .items() is used to create Tupple key,value from dictionnary 
        for key,value in dictionary.items():
            setattr(self,key,value)
            
    # creating a list of matches for a round, while taking players and round number as parameter
    def set_matches (self,players, current_round_number):
        self.rnd_matches= []
        if current_round_number == 1 :
            random.shuffle(players)
            # we go through players list 2 by 2 (last number), using -1 because of the total number of the players converting into index. for exemple player1 has index[0] so len(player) -1 index
            for p in range (0,len(players)-1,2):
                player1 = players[p]
                # creating couple of player from index (side by side) in random shuffle
                player2 = players[p+1]
                # creating Match object with player1 and player 2 argument
                current_match = Match(player1,player2)
                self.rnd_matches.append(current_match)

        else:
            sorted_player = {}
            for player in players:
                # we use player object as a key ex: key obj player1 =(Bob,Doe,...,1) the name and the rest and finally the score, and then taking the score as value, So the key will be : player and the value player.plyr_score
                sorted_player[player]= player.plyr_score  
            #Trying Lambda function:
                # Step 1 : sorted_player.items() = create a list of tupple for player obj (key) and his score (value) 
                # Step2 : sorted(..., key=lambda item: item[1]) = We are using item[1] as sorted "value" from the tupple created by .items() just before instead of creating another function to create a special key
                    # ex: def get_score(item):
                    #         return item[1]
                    # sorted_list = sorted(sorted_player.items(), key=get_score)
                # Step 3 : dict to convert the sorted that converts into a list into a dictionnary again to re-use key value
            sorted_player =dict(sorted(sorted_player.items(), key = lambda item:item[1] )) 
            # creating a list of players after the sorted() so we can assign pair of player for next matches
            sorted_player = list(sorted_player.keys())
            # same process as before to create pair of players for matches from their indexes
            for i in range(0, len(sorted_player)-1, 2):
                player1 = sorted_player[i]
                player2 = sorted_player[i + 1]
                current_match = Match(player1, player2)
                self.rnd_matches.append(current_match)
        # print("all matches look like", self.rnd_matches)
    def check_round_winners(self):
        # creating an empty list to stock players that didn't lost
        players = []
        
        # enumerate is a python function that is used to go through itterable (like a list) element per element, and gives the index from the element.
        # So we are getting through all matches with index i, and get the players.
        # if one wins, it'll be into players list
        for i, match in enumerate(self.rnd_matches):
            # print("match number : ", i)
            if not match.player1.has_lost:
                players.append(match.player1)
            if not match.player2.has_lost:
                players.append(match.player2)
        # for player in players:
        #     print(player.first_name)
        return players
