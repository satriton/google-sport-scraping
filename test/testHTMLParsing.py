import datetime
import os
import unittest
import Fixture

# In order to import files from src
import sys

sys.path.append( f'{os.getcwd()}/src' )

import modele.GameData as GameData
from modele.Team import Team
from extractData import extract_game_data_from_html
from bs4 import BeautifulSoup

class TestHTMLParsing(unittest.TestCase):

    def test_parse_teams_for_played_game(self):
        game: GameData = extract_game_data_from_html(Fixture.past_game)

        self.assertEqual(
            game.teams, 
            [Team(name="Bayonne", score=26, logo="data:image/png;base64,ljfUHUI"), Team(name="Toulouse", score=7, logo="data:image/png;base64,jdshkfjhskjocxvJNKJ")]
        )

    def test_parse_teams_for_futur_game(self):
        game: GameData = extract_game_data_from_html(Fixture.futur_game)

        self.assertEqual(
            game.teams, 
            [Team(name="Oyonnax", score=None, logo="data:image/png;base64,iVBORw0=="), Team(name="Toulouse", score=None, logo="data:image/png;base64,iVBORw0")]
        )

    def test_parse_the_date_for_past_game(self):
        game: GameData = extract_game_data_from_html(Fixture.past_game)

        self.assertEqual(
            game.date, 
            datetime.datetime(2024, 8, 18)
        )
        self.assertEqual(
            game.is_finished, 
            True
        )

    def test_parse_the_date_for_futur_game(self):
        game: GameData = extract_game_data_from_html(Fixture.futur_game)

        self.assertEqual(
            game.date, 
            datetime.datetime(2024, 9, 2, 15, 0)
        )
        self.assertEqual(
            game.is_finished, 
            False
        )

    def test_define_winner_team_and_replay_for_past_game(self):
        game: GameData = extract_game_data_from_html(Fixture.past_game)

        self.assertEqual(
            game.winner, 
            Team(name="Bayonne", score=26, logo="data:image/png;base64,ljfUHUI")
        )
        self.assertEqual(
            game.replay_link, 
            "https://stories.canalplus.com/games/126001-20230818-Bayonne-vs-Stade-Toulousain.html"
        )

    def test_winner_team_and_replay_for_futur_game(self):
        game: GameData = extract_game_data_from_html(Fixture.futur_game)

        self.assertEqual(
            game.winner, 
            None
        )
        self.assertEqual(
            game.replay_link, 
            None
        )


if __name__ == '__main__':
    unittest.main()