from dataclasses import dataclass
from typing import Optional

@dataclass
class Team:
    name: str
    score: Optional[int]
    logo: Optional[str]