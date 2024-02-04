from datetime import date, datetime, timedelta
import os
import unittest
import Fixture
from parameterized import parameterized
from bs4 import BeautifulSoup
import sys

sys.path.append( f'{os.getcwd()}/sport-scrapper' )

import modele.GameData as GameData
from modele.Team import Team
from extractData import convert_to_date, extract_game_data_from_html

class TestHTMLParsing(unittest.TestCase):

    def test_parse_teams_for_played_game(self):
        game: GameData = extract_game_data_from_html(BeautifulSoup(Fixture.past_game, 'html.parser'))

        self.assertEqual(
            game.teams,
            [Team(name="Bayonne", score=26, logo="data:image/png;base64,ljfUHUI"), Team(name="Toulouse", score=7, logo="data:image/png;base64,jdshkfjhskjocxvJNKJ")]
        )

    def test_parse_teams_for_futur_game(self):
        game: GameData = extract_game_data_from_html(BeautifulSoup(Fixture.futur_game, 'html.parser'))

        self.assertEqual(
            game.teams,
            [Team(name="Oyonnax", score=None, logo="data:image/png;base64,iVBORw0=="), Team(name="Toulouse", score=None, logo="data:image/png;base64,iVBORw0")]
        )

    def test_parse_the_date_for_past_game(self):
        game: GameData = extract_game_data_from_html(BeautifulSoup(Fixture.past_game, 'html.parser'))

        self.assertEqual(
            game.date,
            date(2024, 8, 18)
        )
        self.assertEqual(
            game.is_finished,
            True
        )

    def test_parse_the_date_for_futur_game(self):
        game: GameData = extract_game_data_from_html(BeautifulSoup(Fixture.futur_game, 'html.parser'))

        self.assertEqual(
            game.date,
            datetime(2024, 9, 2, 15, 0)
        )
        self.assertEqual(
            game.is_finished,
            False
        )

    def test_define_winner_team_and_replay_for_past_game(self):
        game: GameData = extract_game_data_from_html(BeautifulSoup(Fixture.past_game, 'html.parser'))

        self.assertEqual(
            game.winner,
            Team(name="Bayonne", score=26, logo="data:image/png;base64,ljfUHUI")
        )
        self.assertEqual(
            game.replay_link,
            "https://stories.canalplus.com/games/126001-20230818-Bayonne-vs-Stade-Toulousain.html"
        )

    @parameterized.expand([
        ["Aujourd'hui", date.today()],
        ["Demain", (datetime.today() + timedelta(days=1)).date()],
        ["Dim. 21/01", date(datetime.today().year, 1, 21)],
        ["16/04/23", date(23, 4, 16)],
        ["16/04", date(datetime.today().year, 4, 16)],
    ])
    def test_parse_different_date_format(self, date, expected_date):
        parsed_date = convert_to_date(date, "Terminé")

        self.assertEqual(
            parsed_date,
            expected_date
        )


if __name__ == '__main__':
    unittest.main()
