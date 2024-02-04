from datetime import datetime, timedelta
from typing import List
from bs4 import BeautifulSoup
import logging

from modele.GameData import GameData
from modele.Team import Team

TODAY = "Aujourd'hui"
TOMORROW = "Demain"
DONE = "Terminé"

def extract_game_data_from_html(entry_html: BeautifulSoup) -> GameData:
    teams = extract_teams(entry_html.find_all('tr', {'class': 'L5Kkcd'}))

    is_finished = bool(entry_html.find(class_='imspo_mt__match-status'))

    date = extract_date(entry_html, is_finished)

    winner = extract_winner(teams, is_finished)

    replay_link = extract_replay_link(entry_html)

    return GameData(
        teams,
        date,
        is_finished,
        winner,
        replay_link,
    )


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


def extract_date(soup: BeautifulSoup, is_finished: bool) -> datetime:
    if is_finished:
        date_element = soup.find(class_='imspo_mt__cmd')
        date = date_element.get_text(strip=True)
    else:
        date_element = soup.find(class_='imspo_mt__date')
        date = f"{date_element.get_text(strip=True)}"

    time_element = soup.find(class_='imspo_mt__ndl-p')
    time = time_element.get_text(strip=True) if time_element else None

    return convert_to_date(date, time)


def extract_winner(teams, is_finished):
    winner = None
    if is_finished:
        winner = max(teams[0], teams[1], key=lambda team: team.score)
    return winner


def extract_replay_link(soup: BeautifulSoup) -> str:
    replay_element = soup.find('a', class_='amp_r')
    replay_link = replay_element['data-amp'] if replay_element else None
    return replay_link


def convert_to_date(date_to_parse: str, time: str) -> datetime:
    try:
        if date_to_parse == TODAY:
            real_date = datetime.today()
        elif date_to_parse == TOMORROW:
            real_date = datetime.today() + timedelta(days=1)
        elif "." in date_to_parse: # day. dd/mm
            day, month = map(int, date_to_parse.split(". ")[1].split("/"))
            real_date = datetime(datetime.today().year, month, day)
        else:
            real_date = parse_date(date_to_parse)

        return set_correct_time(real_date, time)
    except Exception:
        logging.exception(f"Error occurred while parsing {date_to_parse}")
        return None


def parse_date(date_to_parse) -> datetime:
    parts = date_to_parse.split("/")
    if len(parts) == 2: # dd/mm
        day, month = map(int, parts)
        real_date = datetime(datetime.today().year, month, day)
    else: # day. dd/mm/aa
        day, month, year = map(int, parts)
        real_date = datetime(year, month, day)
    return real_date


def set_correct_time(real_date: datetime, time: str) -> datetime:
    if time == DONE:
        real_date = real_date.date()
    else:
        real_time = datetime.strptime(time, '%H:%M').time()
        real_date = real_date.replace(hour=real_time.hour, minute=real_time.minute)
    return real_date
