from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class PyrlamentProperties(BaseSettings):
    DEPUTIES: int = 460
    SEATS: int = 467
    COLORS: List[str] = [
        "8a281e",
        "c53f29",
        "dcb44b",
        "719ab7",
        "5778a2",
    ]

    class Config:
        env_prefix: str = "PYRLAMENT_"


@lru_cache(maxsize=1)
def get_pyrlament_properties() -> PyrlamentProperties:
    return PyrlamentProperties()


PYRLAMENT_PROPERTIES = get_pyrlament_properties()
