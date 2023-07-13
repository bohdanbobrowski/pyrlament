from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class PyrlamentProperties(BaseSettings):
    DEPUTIES: int = 460
    COLORS: List[str] = [
        "FF69B4",
        "FE2020",
        "FFA500",
        "FFFF00",
        "008000",
        "40E0D0",
        "4B0082",
        "9400D3",
    ]

    class Config:
        env_prefix: str = "PYRLAMENT_"


@lru_cache(maxsize=1)
def get_pyrlament_properties() -> PyrlamentProperties:
    return PyrlamentProperties()


PYRLAMENT_PROPERTIES = get_pyrlament_properties()
