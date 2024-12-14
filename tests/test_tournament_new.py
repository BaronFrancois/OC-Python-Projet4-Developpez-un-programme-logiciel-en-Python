import sys
import os
sys.path.append('models')
sys.path.append('controllers')
sys.path.append('utils')
import unittest
from unittest.mock import patch
from controllers.main_controller import MainController
from utils.error_util import ResultType
import random

class TestMainController(unittest.TestCase):  
    main_controller = MainController()
        
    @patch('builtins.input',side_effect = ['tournamentUnittest','Paris','05/12/2024','description','tournamentUnittest','Paris','05/12/2024','description','tournamentUnittest2','0'])    
    def test_create_tournament(self,mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        result1 = self.main_controller.create_tournament(details = None, option_number = 1)
        result2 = self.main_controller.create_tournament(details = None, option_number = 1)
        result3 = self.main_controller.create_tournament(details = None, option_number = 1)
        self.assertEqual(result1, ResultType.SUCCES)
        self.assertEqual(result2, ResultType.ERROR)
        self.assertEqual(result3, ResultType.PAUSED)

    @patch('builtins.input',
        side_effect =['tournamentUnittest','Paris','05/12/2024','description',
                    "European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",
                    "European Chess Federation","Europe","London Chess Club","EN67890","Smith","Jane","1988-11-20",
                    "European Chess Federation","Europe","Paris Chess Club","FR12345","Dupont","Pierre","1985-03-08"
                    "Asian Chess Federation","Asia","Tokyo Chess Club","JP12345","Yamada","Taro","1992-07-10",
                    random.choice([1,2]),random.choice([1,2]),random.choice([1,2])])
    
    def test_start_tournament(self, mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        for i in range(4):
            self.main_controller.register_player(details = None, option_number = 4)
        result = self.main_controller.start_tournament(details = None, option_number = 5)
        self.assertEqual(result, ResultType.SUCCES)
        
        
        
    @patch('builtins.input',
    side_effect =['tournamentUnittest','Paris','05/12/2024','description',
                "European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",
                "European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",
                "0" 
                ])
    def test_register_player_succes_pause(self, mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        results = []
        for i in range(3):
            result = self.main_controller.register_player(details = None, option_number = 4)
            results.append(result)
        self.assertEqual(results[0], ResultType.SUCCES)
        self.assertEqual(results[1], ResultType.SUCCES)
        self.assertEqual(results[2], ResultType.PAUSED)
            
    # build error testes
    @patch('builtins.input',
    side_effect =['tournamentUnittest','Paris','05/12/2024','description',
                "wrong Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",
                "European Chess Federation","Europe","wrong Club","EN12345","Doe","John","1990-05-14",
                "European Chess Federation","wrong country","London Chess Club","EN12345","Doe","John","1990-05-14",
                "European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","wrong bd",
                "European Chess Federation","Europe","London Chess Club","EN12345","wrong LN","John","1990-05-14",
                "European Chess Federation","Europe","London Chess Club","EN12345","Doe","wrong FN","1990-05-14",
                "European Chess Federation","Europe","London Chess Club","ENenen1","Doe","John","1990-05-14",
                ])
    def test_register_player_error(self, mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        for i in range(7):
            result = self.main_controller.register_player(details = None, option_number = 4)
            self.assertEqual(result, ResultType.ERROR)
    
    @patch("builtins.input",side_effect=['n','y'])    
    def test_show_all_clubs_players(self, mock_input):
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        for i in range(2):
            result = self.main_controller.show_all_clubs_players(details = None, option_number = 2)
            self.assertEqual(result, ResultType.SUCCES)
        self.assertTrue(os.path.exists(r"resources/reports/all_players_report.txt"))

    @patch("builtins.input",side_effect=['n','y'])
    def test_show_all_tournaments(self, mock_input):
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        for i in range(2):
            result = self.main_controller.show_all_tournaments (details = None, option_number = 3)
            self.assertEqual(result, ResultType.SUCCES)
        self.assertTrue(os.path.exists(r"resources/reports/all_tournaments_report.txt"))

    @patch("builtins.input",side_effect=['tournamentUnittest','Paris','05/12/2024','description','n','y'])
    def test_show_particular_tournament(self,mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        for i in range(2):
            result = self.main_controller.show_particular_tournament(details = None, option_number = 6)
            self.assertEqual(result, ResultType.SUCCES)
        self.assertTrue(os.path.exists(r"resources/reports/tournamentUnittest_report.txt"))
    
    @patch("builtins.input",side_effect=['tournamentUnittest','Paris','05/12/2024','description',"European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",'n','y'])
    def test_show_tournament_players(self,mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        self.main_controller.register_player(details = None, option_number = 4)
        for i in range(2):
            result = self.main_controller.show_tournament_players(details = None, option_number = 7)
            self.assertEqual(result, ResultType.SUCCES)
        self.assertTrue(os.path.exists(r"resources/reports/tournamentUnittest_reg_players_report.txt"))
        
    
    @patch("builtins.input",side_effect=['tournamentUnittest','Paris','05/12/2024','description',
                    "European Chess Federation","Europe","London Chess Club","EN12345","Doe","John","1990-05-14",
                    "European Chess Federation","Europe","London Chess Club","EN67890","Smith","Jane","1988-11-20",
                    "European Chess Federation","Europe","Paris Chess Club","FR12345","Dupont","Pierre","1985-03-08",
                    "Asian Chess Federation","Asia","Tokyo Chess Club","JP12345","Yamada","Taro","1992-07-10",
                    random.choice([1,2]),random.choice([1,2]),random.choice([1,2]),'n','y'])
    def test_show_tournament_report(self,mock_input):
        if os.path.exists(r'resources\tournaments\tournamentUnittest.json'):
            os.remove(r'resources\tournaments\tournamentUnittest.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        self.main_controller.create_tournament(details = None, option_number = 1)
        self.main_controller.load('tournamentUnittest')
        for i in range(4):
            result = self.main_controller.register_player(details = None, option_number = 4)
            self.assertEqual(result, ResultType.SUCCES)
        self.main_controller.start_tournament(details = None, option_number = 5)
        for i in range (2):
            result = self.main_controller.show_tournament_report(details=None, option_number=8)
            self.assertEqual(result, ResultType.SUCCES)
        self.assertTrue(os.path.exists(r"resources/reports/rounds_&_matches_tournamentUnittest_report.txt"))
# ---------------------------------------------------------------------------------        
    @patch("builtins.input", side_effect=['n','y'])
    def test_show_particular_tournament_wrong_name(self, mock_input): 
        if os.path.exists(r'resources\tournaments\tournamentUnittestWrong.json'):
            os.remove(r'resources\tournaments\tournamentUnittestWrong.json')
        if os.path.exists(r"resources/resume_file.json"):
            os.remove(r"resources/resume_file.json")
        result = self.main_controller.load('tournamentUnittestWrong')
        self.assertNotEqual(result, ResultType.SUCCES)
        
    
if __name__ == '__main__' :
    unittest.main()