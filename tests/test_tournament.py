import sys
# from datetime import datetime
sys.path.append('models')
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from datetime import datetime

def test_init():
    
    tournament_name = "Test Tournament"
    location = "Paris"
    start_date = "01/01/2024"
    end_date = "02/01/2024"
    description = "Test Tournament Description"
    number_of_rounds = 4

   
    tournament = Tournament(
        tournament_name,
        location,
        start_date,
        end_date,
        description,
        number_of_rounds
    )

    
    assert tournament.name == tournament_name
    assert tournament.location == location
    assert tournament.start_date == start_date
    assert tournament.end_date == end_date
    assert tournament.description == description
    assert tournament.number_of_rounds == number_of_rounds
    assert tournament.current_round == 0
    assert tournament.registered_players == []
    assert tournament.rounds == []

def test_register_player():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    tournament.register_player("EN12345", "Doe", "John", "1990-05-14", "Europe", "London Chess Club")

    
    assert len(tournament.registered_players) == 1
    player = tournament.registered_players[0]
    assert player.national_chess_id == "EN12345"
    assert player.last_name == "Doe"
    assert player.first_name == "John"
    assert player.date_of_birth == "1990-05-14"
    
def test_verify_player():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    is_verified = tournament.verify_player("EN12345", "Europe", "London Chess Club")
    assert is_verified
    
def test_verify_player_chess_id():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    is_verified = tournament.verify_player("FN12345", "Europe", "London Chess Club")
    assert not is_verified

def test_verify_player_country():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    is_verified = tournament.verify_player("EN12345", "Asia", "London Chess Club")
    assert not is_verified

def test_verify_player_club_name():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    is_verified = tournament.verify_player("EN12345", "Europe", "Paris chess club")
    assert not is_verified
    
def test_save_and_load():
    
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    tournament.save_tournament_details()

    
    loaded_tournament = Tournament("Test Tournament", None, None, None, None)
    loaded_tournament.load_data()

    
    assert loaded_tournament.name == "Test Tournament"
    assert loaded_tournament.location == "Paris"
    assert loaded_tournament.start_date == "01/01/2024"
    assert loaded_tournament.end_date == "02/01/2024"
    assert loaded_tournament.number_of_rounds == 4
    
def test_add_player_to_file():
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    
    tournament.save_tournament_details()
    
    player = Player( "Doe", "John", "1990-05-14","EN12345")
    tournament.add_player_to_file(player)
    loaded_tournament = Tournament("Test Tournament", None, None, None, None)
    loaded_tournament.load_data()
    loaded_player = loaded_tournament.registered_players[0]
    assert loaded_player.last_name == "Doe"
    assert loaded_player.first_name == "John"
    assert loaded_player.date_of_birth == "1990-05-14"
    assert loaded_player.national_chess_id == "EN12345"
    
def test_set_total_nbr_rounds():
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )
    tournament.save_tournament_details()
    
    tournament.register_player("EN12345", "Doe", "John", "1990-05-14", "Europe", "London Chess Club")
    tournament.register_player("EN67890", "Jane", "Smith","1988-11-20", "Europe", "London Chess Club")
    tournament.register_player("FR12345", "Pierre", "Dupont","1985-03-08", "Europe",  "Paris Chess Club")
    tournament.register_player("JP12345", "Taro", "Yamada","1992-07-10", "Asia", "Tokyo Chess Club")
    tournament.set_total_nbr_rounds()
    assert tournament.number_of_rounds == 2
    
def test_generate_round():
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )
    tournament.save_tournament_details()
    
    tournament.register_player("EN12345", "Doe", "John", "1990-05-14", "Europe", "London Chess Club")
    tournament.register_player("EN67890", "Jane", "Smith","1988-11-20", "Europe", "London Chess Club")
    tournament.register_player("FR12345", "Pierre", "Dupont","1985-03-08", "Europe",  "Paris Chess Club")
    tournament.register_player("JP12345", "Taro", "Yamada","1992-07-10", "Asia", "Tokyo Chess Club")
    tournament.set_total_nbr_rounds()
    tournament.generate_round()
    assert tournament.current_round == 1
    round = tournament.rounds[0]
    assert round.rnd_name == "Round 1"
    assert len(round.rnd_matches) == 2
    

def test_start_round():
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    tournament.register_player("EN12345", "Doe", "John", "1990-05-14", "Europe", "London Chess Club")
    tournament.register_player("EN67890", "Jane", "Smith", "1988-11-20", "Europe", "London Chess Club")
    tournament.register_player("FR12345", "Pierre", "Dupont", "1985-03-08", "Europe", "Paris Chess Club")
    tournament.register_player("JP12345", "Taro", "Yamada", "1992-07-10", "Asia", "Tokyo Chess Club")

    tournament.set_total_nbr_rounds()
    tournament.generate_round()
    tournament.start_round()

    round = tournament.rounds[0]

    assert round.rnd_end_datetime

    match = round.rnd_matches[0]

    player1 = match.player1
    player2 = match.player2

    total_score = player1.plyr_score + player2.plyr_score
    assert total_score == 1

def test_add_rounds_to_file():
    tournament = Tournament(
        "Test Tournament", "Paris", "01/01/2024", "02/01/2024", "Test Tournament Description", 4
    )

    tournament.register_player("EN12345", "Doe", "John", "1990-05-14", "Europe", "London Chess Club")
    tournament.register_player("EN67890", "Jane", "Smith", "1988-11-20", "Europe", "London Chess Club")
    tournament.register_player("FR12345", "Pierre", "Dupont", "1985-03-08", "Europe", "Paris Chess Club")
    tournament.register_player("JP12345", "Taro", "Yamada", "1992-07-10", "Asia", "Tokyo Chess Club")

    tournament.set_total_nbr_rounds()
    tournament.generate_round()
    tournament.start_round()
    tournament.add_rounds_to_file()

    loaded_tournament = Tournament("Test Tournament", None, None, None, None)
    loaded_tournament.load_data()
    assert len(loaded_tournament.rounds) == 1
    assert len(loaded_tournament.rounds[0].rnd_matches) == 2
    


