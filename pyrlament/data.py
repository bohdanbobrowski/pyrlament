from typing import List

from pydantic import BaseModel


class Party(BaseModel):
    name: str
    votes: float


class Election(BaseModel):
    parties: List[Party]
