from datetime import date, datetime
from typing import List
from bs4 import BeautifulSoup

from modele.GameData import GameData
from modele.Team import Team


def extract_game_data_from_html(tableHtml: str) -> GameData:
    body = BeautifulSoup(tableHtml, 'html.parser')

    teams = extract_teams(body.find_all('tr', {'class': 'L5Kkcd'}))

    is_finished = bool(body.find(class_='imspo_mt__match-status'))

    date = extract_date(body, is_finished)

    winner = extract_winner(teams, is_finished)

    replay_link = extract_replay_link(body)
    
    return GameData(
        teams,
        date,
        is_finished,
        winner,
        replay_link,
    )

def extract_winner(teams, is_finished):
    winner = None
    if is_finished:
        winner = max(teams[0], teams[1], key=lambda team: team.score)
    return winner

def extract_replay_link(soup):
    replay_element = soup.find('a', class_='amp_r')
    replay_link = replay_element['data-amp'] if replay_element else None
    return replay_link


def extract_date(soup: BeautifulSoup, is_finished: bool) -> datetime:
    if is_finished:
        date_element = soup.find(class_='imspo_mt__cmd')
        date = date_element.get_text(strip=True)
    else:
        date_element = soup.find(class_='imspo_mt__date')
        date = f"{date_element.get_text(strip=True)}"

    time_element = soup.find(class_='imspo_mt__ndl-p')
    time = time_element.get_text(strip=True) if time_element else None

    date = convert_to_date(date.split(".")[1], time)
    return date


def convert_to_date(date:str, time: str) -> datetime:
    real_date = datetime.strptime(date, ' %d/%m')
    real_date = real_date.replace(year=datetime.now().year)
    
    if time != "Terminé":
        real_time = datetime.strptime(time, '%H:%M').time()
        real_date = real_date.replace(hour=real_time.hour, minute=real_time.minute)
    
    return real_date

    
def extract_teams(teams_element: BeautifulSoup) -> List[Team]:
    teams = []
    for team_element in teams_element:
        name = team_element.find('div', {'class': 'liveresults-sports-immersive__hide-element'}).get_text(strip=True)

        score_element = team_element.find_next('div', {'class': 'imspo_mt__t-sc'})
        score = int(score_element.get_text(strip=True)) if score_element else None

        logo_element = team_element.find_next('img', {'class': 'imso_btl__mh-logo'})
        logo = logo_element['src'] if logo_element else None

        teams.append(Team(name=name, score=score, logo=logo))
    return teams