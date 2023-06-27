from typing import List, Optional

from pydantic import BaseModel


class Party(BaseModel):
    name: str
    votes: float
    seats: Optional[int]


class Election(BaseModel):
    parties: List[Party]
