from typing import Optional

from pydantic import BaseModel

DEPUTIES = 460


class Party(BaseModel):
    name: str
    votes: float
    seats: Optional[int]
