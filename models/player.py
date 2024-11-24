
class Player:
    # initialising plyr_score to 0 and has_lost to False to use it into matches logic
    def __init__(self, last_name = None, first_name = None, date_of_birth = None,national_chess_id = None,federation = None,country = None,club_name = None, plyr_score = 0, has_lost = False, dictionary = None):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.federation = federation
        self.country = country
        self.club_name = club_name
        self.plyr_score = plyr_score
        self.has_lost = has_lost
        # __set_attributes : fist the "__" means it's supposed to be used only in the methods of this class, it's a convention "name mangling"
        # and set_attributes is meant to convert dynamicly dictionnary data into Player object
        if dictionary:
            self.__set_attributes(dictionary)
        
    def __set_attributes (self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)
   