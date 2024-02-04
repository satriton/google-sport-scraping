from dataclasses import dataclass
import datetime
from typing import Optional

from modele.Team import Team

@dataclass
class GameData:
    teams: list[Team]
    date: Optional[datetime.datetime]
    is_finished: bool = False
    winner: Optional[Team] = None
    replay_link: Optional[str] = None
