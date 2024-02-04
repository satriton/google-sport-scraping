from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from extractData import extract_game_data_from_html
from modele.GameData import GameData

def get_next_games(team_name: str, sport: str = "rugby") -> List[GameData]:
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox()
    url = f'https://google.com/search?q={team_name} {sport}'

    driver.get(url)

    data = BeautifulSoup(driver.page_source, 'html.parser')

    games = data.find_all('table', class_='KAIX8d')
    print(len(games))

    extracted_games = []
    for game_html in games:
        extracted_games.append(extract_game_data_from_html(game_html))

    driver.quit()
    return extracted_games

if __name__ == '__main__':
    games = get_next_games("stade toulousain")
    print(games)
