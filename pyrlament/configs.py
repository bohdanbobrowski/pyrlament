from functools import lru_cache

from pydantic_settings import BaseSettings


class PyrlamentProperties(BaseSettings):
    DEPUTIES: int = 460

    class Config:
        env_prefix: str = "PYRLAMENT_"


@lru_cache(maxsize=1)
def get_pyrlament_properties() -> PyrlamentProperties:
    return PyrlamentProperties()


PYRLAMENT_PROPERTIES = get_pyrlament_properties()
